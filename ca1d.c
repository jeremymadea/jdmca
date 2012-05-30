#include <stdlib.h> /* malloc, free */
#include <string.h> /* memcpy, bzero */
#include "ca1d.h"


/***************************************
 *                                     *
 * Implementation (private) Prototypes *
 *                                     *
 ***************************************/
    
void _ca_get_next_row(char *row, char *new_row, int width, unsigned ruleset);



/**************************************
 *                                    *
 *    Interface (public) Functions    *
 *                                    *
 **************************************/
    
CA *new_ca(int width, int r, char *start_row) {
    CA *ca_ptr;
    int size = sizeof(CA);
    width = (width > CA_MAX_WIDTH) ? CA_MAX_WIDTH : width;

    /* reserve some memory. */
    ca_ptr = (CA *)malloc(size);
    ca_ptr->f_row = (char *)malloc(width); /* Always holds first row.  */
    ca_ptr->l_row = (char *)malloc(width); /* Holds last row computed. */
    ca_ptr->c_row = (char *)malloc(width); /* Holds current row.       */
    
    if (! start_row) { /* No start row provided... default is empty row. */
        bzero(ca_ptr->f_row, width);
    } else { /* Start row was provided, so use it. */
        memcpy(ca_ptr->f_row, start_row, width);
    }

    /* Immediately copy f_row to c_row because first row is current. */
    memcpy(ca_ptr->c_row, ca_ptr->f_row, width);

    ca_ptr->width = width;
    ca_ptr->rule_set = r;
    return(ca_ptr);
}

void free_ca(CA *ca_ptr) {
    free(ca_ptr->f_row);
    ca_ptr->f_row = NULL;
    free(ca_ptr->l_row);
    free(ca_ptr);
    return;
}

void ca_gen_next_row(CA *ca_ptr) {
    char *temp;
    temp = ca_ptr->l_row;
    ca_ptr->l_row = ca_ptr->c_row;
    ca_ptr->c_row = temp;
    _ca_get_next_row(ca_ptr->l_row, ca_ptr->c_row, 
                     ca_ptr->width, ca_ptr->rule_set);
    return;
}



/***************************************
 *                                     *
 * Implementation (private)  Functions *
 *                                     *
 ***************************************/
    
void _ca_get_next_row(char *row, char *new_row, int width, unsigned ruleset) {
    int bits = 0;
    int rule = 0;
    int idx = 0;
    char cur_bit;
    int lastbit = width - 1;

    /* 
       Set up first four bits of first rule from
           row[width-2],row[width-1],row[0],row[1]
    */
    bits += *(row + (lastbit - 1));
    bits = bits << 1;
    bits += *(row + lastbit);
    bits = bits << 1;
    bits += *row;
    bits = bits << 1;
    bits += *(row + 1);
  
    /* Figure out all but last two bits in new_row with this loop. */ 
    while (idx < (width - 2)) {

        /* Gather the next bit. */
        bits = bits << 1;
        bits += *(row + (idx + 2)); 

        /* Figure out the rule from the last five bits. */
        rule = bits & 0x1f;
        /* Set the current cell according to our rule. */
        cur_bit = (ruleset >> rule) % 2;
        *(new_row + idx) = cur_bit;

        idx++;
    }
    /* idx is width - 2  (next to last cell) */

    /* Gather next to last bit. */
    bits = bits << 1;
    bits += *row; 

    /* Set next to last cell. */
    rule = bits & 0x1f;
    cur_bit = (ruleset >> rule) % 2;
    *(new_row + idx) = cur_bit;

    idx++; /* now equals width-1 (last cell) */

    /* Gather last bit. */
    bits = bits << 1;
    bits += *(row + 1); 

    /* Set last cell. */
    rule = bits & 0x1f;
    cur_bit = (ruleset >> rule) % 2;
    *(new_row + idx) = cur_bit;

    return;
}
    
