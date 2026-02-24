#include <stdio.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input>\n", argv[0]);
        return 1;
    }
    puts("[vulnerable] About to print user-controlled format string:");
    printf(argv[1]);
    putchar('\n');
    return 0;
}
