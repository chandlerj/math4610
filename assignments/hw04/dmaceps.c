#include <stdio.h>
#include <math.h>

double dmaceps(){
    //float gives about 8 digits of precision. use double for double precision
    double one, appone, h, error; 
    one = 1.0;
    h = 1.0;
    appone = one + h;
    error = fabs(appone - one);
    while(error > 0.0){
        h = h / 2.0;
        appone = one + h;
        error = fabs(appone - one);
        printf("error = %g  h = %g\n", error, h);
    }
    return h;
}