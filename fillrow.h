#ifndef __FILLROW_H
#define __FILEROW_H 1
#endif

extern void fill_row(char *row, int fbit, int width);
extern void fill_row_random(char *row, int pct, int fbit, int width, int seed);
extern void fill_row_center(char *row, const char *str, int fbit, int width);
extern void fill_row_repeat(char *row, const char *str, int width);
