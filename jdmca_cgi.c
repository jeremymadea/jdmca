#include <string.h> /* strncpy */
#include <unistd.h> /* getopt  */
#include <errno.h>  /* errno   */
#include <time.h>   /* time    */
#include <stdio.h>
#include <stdlib.h>

#include "cgic.h"

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

#define DEFAULT_WIDTH 100
#define CGI_MAX_WIDTH 400
#define DEFAULT_HEIGHT 100
#define CGI_MAX_HEIGHT 400
#define DEFAULT_RULES 1051758056

int cgiMain() {
    CA *ca_ptr; 
    gdImagePtr image;
    char start_row[CGI_MAX_WIDTH];

    char start_str[CGI_MAX_WIDTH];
    char rtmp[11];
    unsigned long ruleset;
    int width; 
    int gens;
    int mode;
    int blk_r, blk_g, blk_b;
    int wht_r, wht_g, wht_b;
    int  percentage;

    cgiFormString("r", rtmp, 11);
    ruleset = strtoul(rtmp, NULL, 10);
    cgiFormIntegerBounded("width", &width, 5, CGI_MAX_WIDTH, DEFAULT_WIDTH);
    cgiFormIntegerBounded("gens",  &gens,  5, CGI_MAX_HEIGHT, DEFAULT_HEIGHT);
    cgiFormIntegerBounded("p", &percentage, 0, 100, 50);
    cgiFormIntegerBounded("m", &mode, 0, 4, 0);

    cgiFormString("s", start_str, CGI_MAX_WIDTH);

    cgiFormIntegerBounded("br",  &blk_r,  0, 255, 0);
    cgiFormIntegerBounded("bg",  &blk_g,  0, 255, 0);
    cgiFormIntegerBounded("bb",  &blk_b,  0, 255, 0);
    cgiFormIntegerBounded("wr",  &wht_r,  0, 255, 255);
    cgiFormIntegerBounded("wg",  &wht_g,  0, 255, 255);
    cgiFormIntegerBounded("wb",  &wht_b,  0, 255, 255);
    

    if( mode == 0 ) {
        srand(0);
        fill_row_random(start_row, percentage, 0, width, 0);
    } else if (mode == 1) {
        srand(time(NULL));
        fill_row_random(start_row, percentage, 0, width, 0);
    } else if (mode == 2) {
        fill_row_center(start_row, start_str, 0, width);
    } else if (mode == 3) {
        fill_row_center(start_row, start_str, 1, width);
    } else if (mode == 4) {
        fill_row_repeat(start_row, start_str, width);
    } else {
        fill_row(start_row, 0, width);
    }

    ca_ptr = new_ca(width,ruleset,start_row);
    image = ca_make_gif(ca_ptr, gens, 
                        blk_r,blk_g,blk_b, wht_r,wht_g,wht_b);

    cgiHeaderContentType("image/gif");
    gdImageGif(image, cgiOut);
    gdImageDestroy(image);
    free_ca(ca_ptr);
    exit(0);
}

