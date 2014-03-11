#include <stdio.h>
 
int main(int argc, char* argv[])
{
    FILE * in = fopen(argv[1], "r");
    FILE * out = fopen(argv[2], "w");
 
    char c;
    int i = 0;
    while (fread(&c, 1, 1, in) > 0) {
        if (i < 160) {
            c = ~c;
            i ++;
        }
        fwrite(&c, 1, 1, out);
    }
 
    return 0;
}