#include <math.h>
#include <stdio.h>

double linf_dist(double v1[], double v2[], int v1_len, int v2_len){

    if(v1_len != v2_len){
        printf("ERROR: length of vectors not the same. Result will not be accurate\n");
    }
    double max = 0;

    for(int i = 0; i < v1_len; i++){
        double distance = fabs(v1[i] - v2[i]);

        if(distance > max){
            max = distance;
        }
    }

    return max;
}