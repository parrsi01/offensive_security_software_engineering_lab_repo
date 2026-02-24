#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char buffer[16];
    uint32_t guard;
} Frame;

static void handle_input(const char *user_input) {
    Frame frame;
    frame.guard = 0xB16B00B5u;

    /* Intentionally vulnerable for training. */
    strcpy(frame.buffer, user_input);

    printf("buffer='%s'\n", frame.buffer);
    printf("guard=0x%08x\n", frame.guard);
    if (frame.guard != 0xB16B00B5u) {
        puts("OVERFLOW_SIMULATED: adjacent stack data was modified.");
        exit(2);
    }
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input>\n", argv[0]);
        return 1;
    }
    handle_input(argv[1]);
    puts("No overflow observed for this input length.");
    return 0;
}
