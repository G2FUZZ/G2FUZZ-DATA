
    #include <stdio.h>

    __asm__(".symver original_puts, puts@");
    __asm__(".symver new_puts, puts@@VERS_2");

    void original_puts() {
        puts("Original puts");
    }

    void new_puts() {
        puts("New puts");
    }

    int main() {
        original_puts();  // Call the original version
        new_puts();  // Call the new version
        return 0;
    }
    