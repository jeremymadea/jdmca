#include <string.h> /* strncpy */
#include <unistd.h> /* getopt  */
#include <errno.h>  /* errno   */
#include <time.h>   /* time    */
#include <stdio.h>
#include <stdlib.h>
#include "fillrow.h"

#ifndef __CA1D_H
#include "ca1d.h"
#endif

#ifndef __MAKEGIF_H
#include "makegif.h"
#endif

#ifndef GD_H
#include "gd.h"
#endif

#define VERSION "0.9.0"

#define DEFAULT_WIDTH 100
#define DEFAULT_HEIGHT 100
#define DEFAULT_RULES 1051758056

int main(int argc, char *argv[]) {
    int width        = DEFAULT_WIDTH;
    int generations  = DEFAULT_HEIGHT;
    unsigned long ruleset = DEFAULT_RULES;
    FILE *output_fh  = stdout;
    char start_row[CA_MAX_WIDTH];
    char start_str[CA_MAX_WIDTH];
    CA *ca_ptr; 
    gdImagePtr image;
    int idx;

    int opt;
    int init_cntr = 0;
    int blk_r = 0, 
        blk_g = 0, 
        blk_b = 0;
    int wht_r = 255, 
        wht_g = 255, 
        wht_b = 255;
    char *filename = NULL;
    long hexval;
    int  dimension;
    int  percentage=0;

    while( (opt = getopt(argc, argv, "s:p:x:y:b:w:o:r:123")) != -1 ) {
         switch(opt) {
             case 's':
                 strncpy(start_str, optarg,CA_MAX_WIDTH);
                 break;
             case 'p':
                 sscanf(optarg, "%d", &percentage);
                 if ( (percentage > 100) || (percentage < 0) ) {
                     percentage = 50;
                 }
                 break;
             case 'x':
                 sscanf(optarg, "%d", &dimension);
                 if (dimension <= 0) {
                     fprintf(stderr, "Width too small! Using default.\n");
                     width = DEFAULT_WIDTH;
                 } else if( dimension > CA_MAX_WIDTH) {
                     fprintf(stderr, "Width too big! Using default.\n");
                     width = DEFAULT_WIDTH;
                 } else {
                     width = dimension;
                 }
                 break;
             case 'y':
                 sscanf(optarg, "%d", &dimension);
                 if (dimension <= 0) {
                     fprintf(stderr, "Height too small! Using default.\n");
                     generations = DEFAULT_HEIGHT;
                     break;
                 } else {
                     generations = dimension;
                 }
                 break;
             case 'b': 
                 sscanf(optarg,"%lx", &hexval);
                 blk_r  = hexval & 0xff0000; blk_r = blk_r >> 16;
                 blk_g  = hexval & 0x00ff00; blk_g = blk_g >> 8;
                 blk_b  = hexval & 0x0000ff;
                 break; 
             case 'w': 
                 sscanf(optarg,"%lx", &hexval);
                 wht_r  = hexval & 0xff0000; wht_r = wht_r >> 16;
                 wht_g  = hexval & 0x00ff00; wht_g = wht_g >> 8;
                 wht_b  = hexval & 0x0000ff; 
                 break;
             case 'o': 
                 filename = optarg;
                 break;
             case 'r': 
                 sscanf(optarg, "%lu", &ruleset);
                 if (ruleset < 0 || ruleset > (unsigned long)(~0)) {
                     fprintf(stderr, "Bad rule [%lu] specified!\n", ruleset);
                     exit(1);
                 }
                 break; 
             case '1':
                 init_cntr = 1;
                 break; 
             case '2':
                 init_cntr = 2;
                 break; 
             case '3':
                 init_cntr = 3;
                 break; 
             case ':':
                 fprintf(stderr,"Option '%c' requires a value.\n", optopt);
                 exit(1);
             case '?': 
                 fprintf(stderr,"Unknown option '%c'.\n", optopt);
                 exit(1);
         }
    } /* End of command line processing. */


    srand(0);
    for (idx = 0; idx < width; idx++) {
        start_row[idx] = rand() % 2; 
    }

    if( ! init_cntr) {
        fill_row_random(start_row, percentage, 0, width, 0);
    } else if ( init_cntr == 1) {
        fill_row_center(start_row, start_str, 0, width);
    } else if (init_cntr == 2) {
        fill_row_center(start_row, start_str, 1, width);
    } else if (init_cntr == 3) {
        fill_row_repeat(start_row, start_str, width);
    } else {
        fill_row(start_row, 0, width);
    }

    ca_ptr = new_ca(width,ruleset,start_row);
    image = ca_make_gif(ca_ptr, generations, 
                        blk_r,blk_g,blk_b, wht_r,wht_g,wht_b);

    if (filename) {
        output_fh = fopen(filename, "w");
        if (! output_fh) {
            fprintf(stderr,"Unable to open %s for writing: %s\n", 
                    filename, strerror(errno));
            exit(errno);
        }
    }
    gdImagePng(image, output_fh);
    gdImageDestroy(image);
    free_ca(ca_ptr);
    exit(0);
}

