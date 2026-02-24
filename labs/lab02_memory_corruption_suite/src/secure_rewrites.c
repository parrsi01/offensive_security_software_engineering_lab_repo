#include <limits.h>
#include <stdbool.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

static bool multiply_would_overflow_u32(uint32_t a, uint32_t b) {
    return (a != 0 && b > UINT32_MAX / a);
}

static void safe_format_output(const char *user_input) {
    printf("[secure] User input: %s\n", user_input);
}

static int safe_allocation_calculation(uint32_t count, uint32_t bytes_per_record) {
    if (multiply_would_overflow_u32(count, bytes_per_record)) {
        fprintf(stderr, "Rejected: allocation size overflow risk.\n");
        return 1;
    }
    printf("safe_total=%u\n", count * bytes_per_record);
    return 0;
}

int main(int argc, char **argv) {
    char *endptr = NULL;
    unsigned long count_ul;

    if (argc != 3) {
        fprintf(stderr, "Usage: %s <string> <record_count>\n", argv[0]);
        return 1;
    }

    count_ul = strtoul(argv[2], &endptr, 10);
    if (*argv[2] == 0 || *endptr != 0 || count_ul > UINT32_MAX) {
        fprintf(stderr, "Invalid record_count.\n");
        return 1;
    }

    safe_format_output(argv[1]);
    return safe_allocation_calculation((uint32_t)count_ul, 1024);
}
