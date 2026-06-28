#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char *argv[]) {
    if (argc < 2) return 1;

    // Task 1: Triangle Logic
    if (strcmp(argv[1], "triangle") == 0 && argc == 4) {
        int a1 = atoi(argv[2]);
        int a2 = atoi(argv[3]);
        int a3 = 180 - (a1 + a2);
        int is_right = (a1 == 90 || a2 == 90 || a3 == 90);
        
        printf("%d|%s", a3, is_right ? "The triangle IS a right-angled triangle. 🎉" : "Not a right-angled triangle.");
    }
    
    // Task 2: Palindrome Logic
    else if (strcmp(argv[1], "palindrome") == 0 && argc == 3) {
        char *num_str = argv[2];
        int len = strlen(num_str);
        int is_palindrome = 1;
        for(int i = 0; i < len/2; i++) {
            if(num_str[i] != num_str[len - 1 - i]) { is_palindrome = 0; break; }
        }
        if (is_palindrome) {
            printf("Yes! %s is a Palindrome. 🎉", num_str);
        } else {
            printf("%s is Not a Palindrome", num_str);
        }
    }

    return 0;
}
