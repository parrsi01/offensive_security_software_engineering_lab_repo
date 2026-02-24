#include <stdint.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    char buffer[16];
    uint32_t guard;
} Frame;

static int validate_input(const char *user_input) {
    size_t len = strlen(user_input);
    if (len >= sizeof(((Frame *)0)->buffer)) {
        fprintf(stderr, "Rejected input: length %zu exceeds safe buffer size %zu.\n",
                len, sizeof(((Frame *)0)->buffer) - 1);
        return 1;
    }
    return 0;
}

int main(int argc, char **argv) {
    Frame frame;

    if (argc != 2) {
        fprintf(stderr, "Usage: %s <input>\n", argv[0]);
        return 1;
    }
    if (validate_input(argv[1]) != 0) {
        return 1;
    }

    frame.guard = 0xB16B00B5u;
    memset(frame.buffer, 0, sizeof(frame.buffer));
    snprintf(frame.buffer, sizeof(frame.buffer), "%s", argv[1]);

    printf("buffer='%s'\n", frame.buffer);
    printf("guard=0x%08x\n", frame.guard);
    puts("Secure path completed without adjacent overwrite.");
    return 0;
}
