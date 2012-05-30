#ifndef __MAKEGIF_H
#define __MAKEGIF_H 1
#endif

#ifndef __CA1D_H
#include "ca1d.h"
#endif

#ifndef GD_H
#include "gd.h"
#endif

gdImagePtr ca_make_gif(CA *ca_ptr, int generations, 
                    int br, int bg, int bb,   
                    int wr, int wg, int wb );       
