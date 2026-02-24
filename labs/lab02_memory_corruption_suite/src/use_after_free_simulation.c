#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
    char *heap_buf = malloc(32);
    if (heap_buf == NULL) {
        perror("malloc");
        return 1;
    }

    strcpy(heap_buf, "training-buffer");
    printf("allocated=%s\n", heap_buf);
    free(heap_buf);

    puts("USE_AFTER_FREE_SIMULATED: freed pointer must now be treated as invalid.");
    puts("Secure pattern: set pointer to NULL immediately after free and avoid reuse.");
    heap_buf = NULL;

    if (heap_buf == NULL) {
        puts("Pointer cleared after free (secure hygiene demonstrated).");
    }
    return 0;
}
