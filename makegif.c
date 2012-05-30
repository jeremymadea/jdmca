#ifndef __MAKEGIF_H
#include "makegif.h"
#endif

gdImagePtr ca_make_gif(CA *ca_ptr, int generations, 
                    int br, int bg, int bb,   
                    int wr, int wg, int wb )  {      
    gdImagePtr img;
    int black, white;
    int gen;
    int cell;

    img = gdImageCreate(ca_ptr->width, generations);
    if (!img) {
        fprintf(stderr,"Can't allocate image!\n");
        exit(1);
    }

    black = gdImageColorAllocate(img, br, bg, bb);
    white = gdImageColorAllocate(img, wr, wg, wb);

    for(gen=0; gen < generations; gen++) {
        for(cell=0; cell < ca_ptr->width; cell++) {
            gdImageSetPixel(img, cell, gen, 
                            *(ca_ptr->c_row + cell) ? white : black);
        }
        ca_gen_next_row(ca_ptr);
    }
    return img;    
}
