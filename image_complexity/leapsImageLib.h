
#ifndef __LEAPS_IMAGE_LIB__
#define __LEAPS_IMAGE_LIB__

#include "./lodepng.h"

namespace LeapsImageLib{
    class Image
    {
        using uchar = unsigned char;
    public:
        Image();
        Image(int,int);
        Image(const char*);
    private:
        uchar* buffer;
        unsigned width, height;
    };
}

#endif