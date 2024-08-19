#define _POSIX_C_SOURCE 200809L
#define _GNU_SOURCE
#include <ctype.h>
#include <err.h>
#include <errno.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#ifndef MAX_WORDS
#define MAX_WORDS 512
#endif

/* the last foreground command PID */
int last_exit_status = 0;
/* process ID of the most recent background process */
pid_t last_bg_pid = -1;

char *words[MAX_WORDS];
size_t wordsplit(char const *line);
char *expand(char const *word);
void handle_exit(char **words, size_t nwords, char *line);
void handle_cd(char **words, size_t nwords);
void handle_redirection(char **words, size_t nwords);
void execute_command(char **words, size_t nwords);
int print_working_dir(char **words, size_t nwords);

int main(int argc, char *argv[]) {
  FILE *input = stdin;
  char *input_fn = "(stdin)";
  int is_background_operator = 0;
  if (argc == 2) {
    input_fn = argv[1];
    input = fopen(input_fn, "re");
    if (!input)
      err(1, "%s", input_fn);
  } else if (argc > 2) {
    errx(1, "too many arguments");
  }

  char *line = NULL;
  size_t n = 0;
  for (;;) {
    // prompt:;
    /* TODO: Manage background processes */

    /* TODO: prompt */
    if (input == stdin) {  // interactive mode
      printf("smallsh> "); // Print a prompt
      fflush(stdout);      // Make sure the prompt is displayed
    }
    ssize_t line_len = getline(&line, &n, input); // non interactive mode?
    if (line_len < 0)
      err(1, "%s", input_fn);

    size_t nwords = wordsplit(line);

    handle_redirection(words, nwords);

    // Check if the last word is the background operator
    if (nwords > 0 && strcmp(words[nwords - 1], "&") == 0) {
      // Handle the background operator
      is_background_operator = 1;
      // Remove the background operator from the words array
      free(words[nwords - 1]);
      words[nwords - 1] = NULL;
      --nwords;
    }

    if (strcmp(words[0], "exit") == 0) {
      // Handle exit command
      handle_exit(words, nwords, line);
    } else if (strcmp(words[0], "cd") == 0) {
      // Handle cd command
      handle_cd(words, nwords);
    } else {
      // Execute non-built-in command
      execute_command(words, nwords);
    }

    print_working_dir(words, nwords); // Print working directory)

    for (size_t i = 0; i < nwords; ++i) {
      fprintf(stderr, "Word %zu: %s\n", i, words[i]);
      char *exp_word = expand(words[i]);
      free(words[i]);
      words[i] = exp_word;
      fprintf(stderr, "Expanded Word %zu: %s\n", i, words[i]);
    }
    // Free memory allocated for words
    for (size_t i = 0; i < nwords; ++i) {
      free(words[i]);
      words[i] = NULL;
    }
    free(line);
    line = NULL;

    // Set exit status to 0 after successful execution
    last_exit_status = 0;
  }

  return 0;
}

char *words[MAX_WORDS] = {0};

/* Splits a string into words delimited by whitespace. Recognizes
 * comments as '#' at the beginning of a word, and backslash escapes.
 *
 * Returns number of words parsed, and updates the words[] array
 * with pointers to the words, each as an allocated string.
 */
size_t wordsplit(char const *line) {
  size_t wlen = 0;
  size_t wind = 0;

  char const *c = line;
  for (; *c && isspace(*c); ++c)
    ; /* discard leading space */

  for (; *c;) {
    if (wind == MAX_WORDS)
      break;
    /* read a word */
    if (*c == '#')
      break;
    for (; *c && !isspace(*c); ++c) {
      if (*c == '\\')
        ++c;
      void *tmp = realloc(words[wind], sizeof **words * (wlen + 2));
      if (!tmp)
        err(1, "realloc");
      words[wind] = tmp;
      words[wind][wlen++] = *c;
      words[wind][wlen] = '\0';
    }
    ++wind;
    wlen = 0;
    for (; *c && isspace(*c); ++c)
      ;
  }
  return wind;
}

/* Find next instance of a parameter within a word. Sets
 * start and end pointers to the start and end of the parameter
 * token.
 */
char param_scan(char const *word, char const **start, char const **end) {
  static char const *prev;
  if (!word)
    word = prev;

  char ret = 0;
  *start = 0;
  *end = 0;
  for (char const *s = word; *s && !ret; ++s) {
    s = strchr(s, '$');
    if (!s)
      break;
    switch (s[1]) {
    case '$':
    case '!':
    case '?':
      ret = s[1];
      *start = s;
      *end = s + 2;
      break;
    case '{':;
      char *e = strchr(s + 2, '}');
      if (e) {
        ret = s[1];
        *start = s;
        *end = e + 1;
      }
      break;
    }
  }
  prev = *end;
  return ret;
}

/* Simple string-builder function. Builds up a base
 * string by appending supplied strings/character ranges
 * to it.
 */
char *build_str(char const *start, char const *end) {
  static size_t base_len = 0;
  static char *base = 0;

  if (!start) {
    /* Reset; new base string, return old one */
    char *ret = base;
    base = NULL;
    base_len = 0;
    return ret;
  }
  /* Append [start, end) to base string
   * If end is NULL, append whole start string to base string.
   * Returns a newly allocated string that the caller must free.
   */
  size_t n = end ? end - start : strlen(start);
  size_t newsize = sizeof *base * (base_len + n + 1);
  void *tmp = realloc(base, newsize);
  if (!tmp)
    err(1, "realloc");
  base = tmp;
  memcpy(base + base_len, start, n);
  base_len += n;
  base[base_len] = '\0';

  return base;
}

/* Expands all instances of $! $$ $? and ${param} in a string
 * Returns a newly allocated string that the caller must free
 */
char *expand(char const *word) {
  char const *pos = word;
  char const *start, *end;
  char c = param_scan(pos, &start, &end);
  build_str(NULL, NULL);
  build_str(pos, start);
  while (c) {
    if (c == '!') { // $! == <BGPID>
      // Handle $!
      if (last_bg_pid != -1) {
        char pid_str[1000];
        snprintf(pid_str, sizeof(pid_str), "%d", last_bg_pid);
        build_str(pid_str, NULL);
      } else {
        // No background process ID available, default to empty string
        build_str("", NULL);
      }
    } else if (c == '$') { // $$ == <PID>
      // Handle $$
      pid_t pid = getpid();
      char pid_str[1000];
      snprintf(pid_str, sizeof(pid_str), "%d", pid);
      build_str(pid_str, NULL);
      pos = end;
    } else if (c == '?') { // $? == <STATUS> or last FG command exit status
      // Handle $?
      char status_str[1000];
      snprintf(status_str, sizeof(status_str), "%d", last_exit_status);
      build_str(status_str, NULL);
    } else if (c == '{') { // ${param} == <Parameter: param>
      // Handle ${param}
      char param_name[end - start]; // Extract parameter name
      strncpy(param_name, start + 2, end - start - 2);
      param_name[end - start - 2] = '\0';

      char *param_value = getenv(param_name); // Get environment variable value
      if (param_value) {
        build_str(param_value, NULL);
      } else {
        // Environment variable not found, default to empty string
        build_str("", NULL);
      }
    }
    pos = end;
    c = param_scan(pos, &start, &end);
    build_str(pos, start);
  }
  return build_str(start, NULL);
}

/* Handle the exit command */
void handle_exit(char **words, size_t nwords, char *line) {
  if (nwords > 0 && strcmp(words[0], "exit") == 0) {
    if (nwords > 2) {
      fprintf(stderr, "Usage: exit [status]\n");
    } else {
      int exit_status;
      if (nwords == 1) {
        exit_status = last_exit_status;
      } else {
        char *endptr;
        exit_status = (int)strtol(words[1], &endptr, 10);
        if (*endptr != '\0' || errno == ERANGE) {
          fprintf(stderr, "exit: Invalid argument: %s\n", words[1]);
          exit_status = 1; // Set exit status to indicate error
        }
      }
      last_exit_status = exit_status; // Update last_exit_status
      free(line);                     // Free allocated memory before exit
      exit(exit_status);
    }
  }
}

/* Handle the cd command */
void handle_cd(char **words, size_t nwords) {
  if (nwords > 0 && strcmp(words[0], "cd") == 0) {
    if (nwords > 2) {
      fprintf(stderr, "Usage: cd [directory]\n");
    } else {
      char *target_dir;
      if (nwords == 1) {
        target_dir = getenv("HOME");
        if (!target_dir) {
          fprintf(stderr, "cd: HOME environment variable not set\n");
          return; // Skip to next iteration of the loop
        }
      } else {
        target_dir = words[1]; // Expand any environment variables
      }

      if (chdir(target_dir) == -1) {
        perror("cd");
      }
    }
  }
}
int print_working_dir(char **words, size_t nwords) {
  if (nwords == 1 && strcmp(words[0], "pwd") == 0) {
    char cwd[1024];
    if (getcwd(cwd, sizeof(cwd)) != NULL) {
      printf("%s\n", cwd);
      return 0; // Success
    } else {
      perror("getcwd() error");
      return 1; // Failure
    }
  }
  return -1; // Indicate no action taken
}

void handle_redirection(char **words, size_t nwords) {
  int input_fd, output_fd;

  // Look for redirection operators
  for (size_t i = 0; i < nwords; ++i) {
    if (strcmp(words[i], ">") == 0) {
      // Output redirection
      output_fd = open(words[i + 1], O_WRONLY | O_CREAT | O_TRUNC, 0777);
      if (output_fd < 0) {
        perror("open");
        exit(
            EXIT_FAILURE); // Exit the child process with an error if open fails
      }
      if (dup2(output_fd, STDOUT_FILENO) < 0) {
        perror("dup2");
        exit(
            EXIT_FAILURE); // Exit the child process with an error if dup2 fails
      }
      close(output_fd);
      words[i] = NULL;     // Remove the redirection operator from the command
      words[i + 1] = NULL; // Remove the filename from the command
    } else if (strcmp(words[i], "<") == 0) {
      // Input redirection
      input_fd = open(words[i + 1], O_RDONLY);
      if (input_fd < 0) {
        perror("open");
        exit(
            EXIT_FAILURE); // Exit the child process with an error if open fails
      }
      if (dup2(input_fd, STDIN_FILENO) < 0) {
        perror("dup2");
        exit(
            EXIT_FAILURE); // Exit the child process with an error if dup2 fails
      }
      close(input_fd);
      words[i] = NULL;     // Remove the redirection operator from the command
      words[i + 1] = NULL; // Remove the filename from the command
    } else if (strcmp(words[i], ">>") == 0) {
      // Append redirection
      output_fd = open(words[i + 1], O_WRONLY | O_CREAT | O_APPEND, 0777);
      if (output_fd < 0) {
        perror("open");
        exit(
            EXIT_FAILURE); // Exit the child process with an error if open fails
      }
      if (dup2(output_fd, STDOUT_FILENO) < 0) {
        perror("dup2");
        exit(
            EXIT_FAILURE); // Exit the child process with an error if dup2 fails
      }
      close(output_fd);
      words[i] = NULL;     // Remove the redirection operator from the command
      words[i + 1] = NULL; // Remove the filename from the command
    }
  }
}

// Child process
void execute_command(char **words, size_t nwords) {
  pid_t pid = fork(); // Create a new child process
  if (pid == -1) {
    // Fork failed
    perror("fork");
    exit(EXIT_FAILURE);
  } else if (pid == 0) {
    // Child process
    // Handle redirection
    handle_redirection(words, nwords);

    // Remove redirection operators and their filename arguments
    size_t i = 0;
    while (i < nwords) {
      if (strcmp(words[i], "<") == 0 || strcmp(words[i], ">") == 0 ||
          strcmp(words[i], ">>") == 0) {
        // Remove the redirection operator and its filename argument
        free(words[i]);
        if (i + 1 < nwords) {
          free(words[i + 1]);
          words[i + 1] = NULL;
        }
        // Shift the remaining arguments
        for (size_t j = i + 2; j < nwords; ++j) {
          words[j - 2] = words[j];
        }
        nwords -= 2;
      } else if (strcmp(words[i], "&") == 0) {
        // Remove the "&" background operator
        free(words[i]);
        // Shift the remaining arguments
        for (size_t j = i + 1; j < nwords; ++j) {
          words[j - 1] = words[j];
        }
        nwords -= 1;
      } else {
        ++i;
      }
    }

    // Check if the command name contains a "/"
    if (strchr(words[0], '/') == NULL) {
      // If not, search for the command in the PATH environment variable
      char *path = getenv("PATH");
      if (path == NULL) {
        // If PATH is not set, use default path "/bin:/usr/bin"
        path = "/bin:/usr/bin";
      }

      // Tokenize the PATH variable and try executing the command
      char *path_copy = strdup(path);
      char *dir = strtok(path_copy, ":");
      while (dir != NULL) {
        char *command_path = malloc(strlen(dir) + strlen(words[0]) + 2);
        sprintf(command_path, "%s/%s", dir, words[0]);
        execv(command_path, words);
        free(command_path);
        dir = strtok(NULL, ":");
      }
      free(path_copy);

      // If the command is not found in any directory in PATH, print an error
      fprintf(stderr, "Command not found: %s\n", words[0]);
      exit(EXIT_FAILURE);
    } else {
      // If the command name contains "/", execute it directly
      execvp(words[0], words);
      // If execvp returns, an error occurred
      perror("execvp");
      exit(EXIT_FAILURE);
    }
  } else {
    // Parent process
    int status;
    waitpid(pid, &status, 0); // Wait for the child process to finish
    if (WIFEXITED(status)) {
      // Child process terminated normally
      last_exit_status = WEXITSTATUS(status); // Update last_exit_status
    } else {
      // Child process terminated abnormally
      last_exit_status = 1; // Set exit status to indicate error
    }
  }
}
