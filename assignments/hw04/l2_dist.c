#include <math.h>
#include <stdio.h>

double l2_dist(double v1[], double v2[], int v1_len, int v2_len){

    if(v1_len != v2_len){
        printf("ERROR: length of vectors not the same. Result will not be accurate\n");
    }
    double sum = 0;

    for(int i = 0; i < v1_len; i++){
        double distance = v1[i] - v2[i];

        sum += distance * distance;
    }
    sum = sqrt(sum);

    return sum;
}