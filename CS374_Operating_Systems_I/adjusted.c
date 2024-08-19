#include <stdio.h>
#include <errno.h>
#include <stdint.h>
#include <string.h>
#include <err.h>

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
        }
    } else {
        fp = stdin;
        printf("Using stdin instead\n");
    }

    for (;;) {
        uint8_t input_bytes[3] = {0};
        size_t n_read = fread(input_bytes, 1, 3, fp);

        // Check if we have less than 3 characters read
        if (n_read < 3) {
            if (feof(fp)) {
                break; // End of file
            }
            if (ferror(fp)) {
                err(1, "Read error");
            }
        }

        // Encode the characters based on how many were read
        int alph_ind[4];
        alph_ind[0] = input_bytes[0] >> 2;
        alph_ind[1] = (input_bytes[0] << 4 | input_bytes[1] >> 4) & 0x3Fu;

        // Check if n_read is less than 2 to avoid out-of-bounds array access
        if (n_read < 2) {
            alph_ind[2] = alph_ind[3] = 64; // Pad characters
        } else {
            alph_ind[2] = (input_bytes[1] << 2 | input_bytes[2] >> 6) & 0x3Fu;

            // Check if n_read is less than 3 to avoid out-of-bounds array access
            if (n_read < 3) {
                alph_ind[3] = 64; // Pad character
            } else {
                alph_ind[3] = input_bytes[2] & 0x3Fu;
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
        fclose(fp); // Close the file
    }

    return 0;
}
