#include <stdio.h>
#include <math.h>
#include "l2_norm.c"
#include "l1_norm.c"
#include "inf_norm.c"
#include "l2_dist.c"
#include "l1_dist.c"
#include "linf_dist.c"
#include "linreg.c"
#include "fx.c"
#include "dfapp_forward.c"
#include "dfapp_backward.c"
#include "dfapp_central.c"
#include "reduce_matrix.c"
#include "smaceps.c"
#include "dmaceps.c"

double l2_norm(double v[], int vec_len);
double l1_norm(double v[], int vec_len);
double inf_norm(double v[], int vec_len);
double l2_dist(double v1[], double v2[], int v1_len, int v2_len);
double l1_dist(double v1[], double v2[], int v1_len, int v2_len);
double linf_dist(double v1[], double v2[], int v1_len, int v2_len);
double f(double x);
double dfapp_forward(double x, double h);
double dfapp_backward(double x, double h);
double dfapp_central(double x, double h);
const char* linreg(double x_vec[], double y_vec[], int length);
void reduce_matrix();
int main(){
    //maceps tests
    printf("32 bit macepts value: %g\n", smaceps());
    printf("64 bit macepts value: %g\n", dmaceps());
    //vector operations
    double vector[4] = {2.4, 4.0, 3.14, 2.0};
    double vector2[4] = {4.0, 6.7, 4.9, -4.5};
    printf("l2-norm: %g\n", l2_norm(vector, 4));
    printf("l1-norm: %g\n", l1_norm(vector, 4));
    printf("inf-norm: %g\n", inf_norm(vector, 4));
    printf("l2-dist: %g\n", l2_dist(vector, vector2, 4, 4));
    printf("l1-dist: %g\n", l1_dist(vector, vector2, 4, 4));
    printf("linf-dist: %g\n", linf_dist(vector, vector2, 4, 4));
    printf("forward approx of derivative of x * x at x = 10, h = 0.01: %g\n", dfapp_forward(10, 0.01));
    printf("central approx of derivative of x * x at x = 10, h = 1: %g\n", dfapp_central(10, 1));
    printf("backwards approx of derivative of x * x at x = 10, h = 0.01: %g\n", dfapp_backward(10, 0.01));

    //test linear regression
    double vec1[] = {2,3,5,7,9};
    double vec2[] = {4,5,7,10,15};

    const char* best_fit = linreg(vec1, vec2, 5);
    printf("linear regression of (2,4), (3,5), (5,7), (7,10), (9,15): %s",best_fit);

    //test matrix
    //input this matrix
    // 3 0 0 0 0 0 0 0 0 0
    // 0 1 0 0 0 0 0 0 0 0
    // 0 0 3 0 0 0 0 0 0 0
    // 0 0 0 5 0 0 0 0 0 0
    // 0 0 0 0 5 0 0 0 0 0
    // 0 0 0 0 0 2 0 0 0 0
    // 0 0 0 0 0 0 6 0 0 0
    // 0 0 0 0 0 0 0 2 0 0
    // 0 0 0 0 0 0 0 0 9 0
    // 0 0 0 0 0 0 0 0 0 5

    reduce_matrix();

    return 0;
}