#include <stdio.h>  // Standard input and output
#include <errno.h>  // Access to errno and Exxx macros
#include <stdint.h> // Extra fixed-width data types
#include <string.h> // String utilities
#include <err.h>    // Convenience functions for error reporting (non-standard)

static char const b64_alphabet[] =
  "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  "abcdefghijklmnopqrstuvwxyz"
  "0123456789"
  "+/";

int main(int argc, char *argv[]) {
    FILE *fp;

    if (argc > 2) {
        fprintf(stderr, "Usage: %s [FILE]\n", argv[0]);
        errx(1, "Too many arguments");
    } else if (argc == 2 && strcmp(argv[1], "-")) {
        fp = fopen(argv[1], "rb");
        if (!fp) {
            err(1, "Failed to open %s file", argv[1]);
        } /* open FILE */
    } else {
        fp = stdin;
        printf("Using stdin instead\n"); /* use stdin instead */
    }

    for (;;) {
        uint8_t input_bytes[3] = {0};
        size_t n_read = fread(input_bytes, 1, 3, fp);
        int alph_ind[4];

        alph_ind[0] = input_bytes[0] >> 2;
        alph_ind[1] = (input_bytes[0] << 4 | input_bytes[1] >> 4) & 0x3Fu;
        if (n_read < 2) {
            alph_ind[2] = alph_ind[3] = 64;
        } else {
            alph_ind[2] = (input_bytes[1] << 2 | input_bytes[2] >> 6) & 0x3Fu;
            if (n_read < 3) {
                alph_ind[3] = 64;
            } else {
                alph_ind[3] = input_bytes[2] & 0x3Fu;
            }
        }
        if (n_read < 3) {
        /* Got less than expected */
            if (feof(fp)) {
                break; /* End of file */
            }
            if (ferror(fp)) {
                err(1, "Read error"); /* Read error */
            }
        }

        char output[4];
        output[0] = b64_alphabet[alph_ind[0]];
        output[1] = b64_alphabet[alph_ind[1]];
        output[2] = b64_alphabet[alph_ind[2]];
        output[3] = b64_alphabet[alph_ind[3]];
        
        size_t n_write = fwrite(output, 1, 4, stdout);
        if (n_write != 4) {
            err(1, "Write error");
            }
        }
    if (fp != stdin) {
        fclose(fp); /* close opened files; */
    }
    return 0; /* any other cleanup tasks? */
}