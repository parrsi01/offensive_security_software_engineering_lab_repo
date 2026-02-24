#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    if (argc != 2) {
        fprintf(stderr, "Usage: %s <record_count>\n", argv[0]);
        return 1;
    }

    unsigned long requested = strtoul(argv[1], NULL, 10);
    uint16_t bytes_per_record = 1024;
    uint16_t total_size = (uint16_t)(requested * bytes_per_record);

    printf("requested=%lu bytes_per_record=%u total_size=%u\n",
           requested, bytes_per_record, total_size);

    if (requested > 0 && total_size < bytes_per_record) {
        puts("INTEGER_OVERFLOW_SIMULATED: total_size wrapped around.");
        return 2;
    }

    puts("No wrap detected for this input.");
    return 0;
}
