#include <math.h>

double l1_norm(double v[], int vec_len){
    double sum = 0.0;
    for(int i =0; i < vec_len; i++){
        sum += fabs(v[i]);
    }
    return sum;
}