#include <stdio.h>
#include <stdlib.h>
#include <math.h>

//helper function to reduce repeated code
double sum_vector(double vec[], int length){
    double sum = 0;
    for(int i = 0; i < length; i++){
        sum += vec[i];
    }

    return sum;
}

const char* linreg(double x_vec[], double y_vec[], int length){
    //calculate sum of x^2
    double x_squared_sum = 0;
    for(int i = 0; i < length; i++){
        x_squared_sum += x_vec[i] * x_vec[i];
    }

    //calculate sum of xy
    double xy_sum = 0;
    for(int i = 0; i < length; i++){
        xy_sum += x_vec[i] * y_vec[i];
    }

    //calculate x and y sums
    double x_sum = sum_vector(x_vec, length);
    double y_sum = sum_vector(y_vec, length);

    //calculate slope of linreg
    double slope_numerator = ((length * xy_sum) - (x_sum * y_sum));
    double slope_denominator = ((length * x_squared_sum) - (x_sum * x_sum));
    double slope = slope_numerator / slope_denominator;


    //calculate the intercept
    double intercept = (y_sum - (slope * x_sum)) / length;

    char* linreg_result = malloc(sizeof(char) * 50);
    sprintf(linreg_result, "y = %fx + %f\n", slope, intercept);

    return linreg_result;
}
