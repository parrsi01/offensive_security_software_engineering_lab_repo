#include <stdint.h>
#include <stdio.h>
#include <string.h>

static uint32_t score_input(const char *s) {
    uint32_t score = 0x1234u;
    for (size_t i = 0; s[i] != '\0'; ++i) {
        score = (score * 33u) ^ (unsigned char)s[i];
    }
    return score;
}

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <token>\n", argv[0]);
        return 1;
    }

    uint32_t score = score_input(argv[1]);
    printf("score=0x%08x\n", score);
    if (strlen(argv[1]) == 8 && (score & 0xffu) == 0x42u) {
        puts("ACCESS: training-success");
        return 0;
    }
    puts("ACCESS: denied");
    return 2;
}
