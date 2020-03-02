#ifndef __CA1D_H
#define __CA1D_H 1
#endif

#define CA_MAX_WIDTH 8192

typedef struct {
    int width;
    char *f_row;
    char *l_row;;
    char *c_row;
    int rule_set;
} CA;


extern CA *new_ca(int x, int r, char *start_row);
extern void free_ca(CA *ca_ptr);
extern void ca_gen_next_row(CA *ca_ptr);
