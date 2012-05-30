#include "fillrow.h"
#include <string.h> /* strlen      */
#include <stdlib.h> /* srand, rand */
#include <stdio.h>  /* fprintf     */

void fill_row(char *row, int fbit, int width) {
    int i = 0;
    while(i < width) {
        *(row + i) = fbit;
        i++;
    }
    return;
}

void fill_row_random(char *row, int pct, int fbit, int width, int seed) {
    int i = 0;
    int onbit = !fbit;
    int percentile;

    fill_row(row,fbit,width);
    srand(seed);
    while(i < width) {
        percentile = (int)(100.0*rand()/RAND_MAX+1.0);
        if (pct >= percentile) {
            *(row + i) = onbit;
        }
        i++;
    }
    return;
}

void fill_row_center(char *row, const char *str, int fbit, int width) {
    int i = 0;
    int j = 0;
    int length = strlen(str);

    fill_row(row, fbit, width);
    if (length > width) {
        fprintf(stderr,"fill_row_center: Warning: String longer than width.\n");
    } else {
        i = (width - length) / 2;
    }

    while((i < width) && (j < length)) {
        *(row + i) = (*(str + j) == '0') ? 0 : 1;
        i++;
        j++;
    }
    return;
}

void fill_row_repeat(char *row, const char *str, int width) {
    int i = 0;
    int j = 0;
    int length = strlen(str);

    if (length > width) {
        fprintf(stderr,"fill_row_repeat: Warning: String longer than width.\n");
    } else if (length <= 0) {
        fprintf(stderr,"fill_row_repeat: Error: String is 0 length!\n");
        return;
    } 

    while( i < width ) {
        *(row + i) = (*(str + j) == '0') ? 0 : 1;
        i++;
        j++;
        if (j >= length) {
            j = 0;
        }
    }

    return;
}

