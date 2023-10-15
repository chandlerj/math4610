#include <stdio.h>
#include <math.h>

double l2_norm(double v[], int vec_len){
    double sum = 0.0;
    for(int i =0; i < vec_len; i++){
        sum += v[i] * v[i];
    }
    sum = sqrt(sum);
    return sum;
}