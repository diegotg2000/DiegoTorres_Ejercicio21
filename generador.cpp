#include <iostream>
#include <random>
#include <stdlib.h>
#include <cmath>

int main(){
  int i;
  float theta;
  float dx;
  float dy; 
  float x=0;
  float y=0;
  srand48(17);
  float pi=3.1415192654;
  std::cout<<x<<' '<<y<<std::endl;
  for (i=1;i<1000;i++){  

      theta=2*pi*drand48();
      dx=cos(theta);
      dy=sin(theta);
      x=x+dx;
      y=y+dy;
      std::cout<<x<<' '<<y<<std::endl;
  }
  
  return 0;
}
