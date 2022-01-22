
#include "leapsImageLib.h"
#include <iostream>

void decodeOneStep(const char* filename) {
  std::vector<unsigned char> image;
  unsigned width, height;

  unsigned error = lodepng::decode(image, width, height, filename);

  if(error) std::cout << "decoder error " << error << ": " << lodepng_error_text(error) << std::endl;

  //the pixels are now in the vector "image", 4 bytes per pixel, ordered RGBARGBA..., use it as texture, draw it, ...
  printf("%d %d %d %d\n", image[0], image[1], image[2], image[3]);
}

//Example 2
//Load PNG file from disk to memory first, then decode to raw pixels in memory.
void decodeTwoSteps(const char* filename) {
  std::vector<unsigned char> png;
  std::vector<unsigned char> image; //the raw pixels
  unsigned width, height;

  //load and decode
  unsigned error = lodepng::load_file(png, filename);
  if(!error) error = lodepng::decode(image, width, height, png);

  //if there's an error, display it
  if(error) std::cout << "decoder error " << error << ": " << lodepng_error_text(error) << std::endl;

  //the pixels are now in the vector "image", 4 bytes per pixel, ordered RGBARGBA..., use it as texture, draw it, ...
}

//Example 3
//Load PNG file from disk using a State, normally needed for more advanced usage.
void decodeWithState(const char* filename) {
  std::vector<unsigned char> png;
  std::vector<unsigned char> image; //the raw pixels
  unsigned width, height;
  lodepng::State state; //optionally customize this one

  unsigned error = lodepng::load_file(png, filename); //load the image file with given filename
  if(!error) error = lodepng::decode(image, width, height, state, png);

  //if there's an error, display it
  if(error) std::cout << "decoder error " << error << ": "<< lodepng_error_text(error) << std::endl;

  //the pixels are now in the vector "image", 4 bytes per pixel, ordered RGBARGBA..., use it as texture, draw it, ... 
}

int main(int argc, char *argv[]) {
  const char* filename = argc > 1 ? argv[1] : "Lenna.png";
  
  decodeOneStep(filename);
}
