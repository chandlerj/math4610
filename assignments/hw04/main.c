#include <stdio.h>
#include <math.h>
#include "l2_norm.c"
#include "l1_norm.c"
#include "inf_norm.c"
#include "l2_dist.c"
#include "l1_dist.c"
#include "linf_dist.c"
#include "linreg.c"
#include "dfapp_forward.c"
#include "dfapp_backward.c"
#include "dfapp_central.c"

double l2_norm(double v[], int vec_len);
double l1_norm(double v[], int vec_len);
double inf_norm(double v[], int vec_len);
double l2_dist(double v1[], double v2[], int v1_len, int v2_len);
double l1_dist(double v1[], double v2[], int v1_len, int v2_len);
double linf_dist(double v1[], double v2[], int v1_len, int v2_len);
// double linreg(double v1[], double v2[], int v1_len, int v2_len);
double dfapp_forward(double x, double h);
double dfapp_backward(double x, double h);
double dfapp_central(double x, double h);

int main(){

    double vector[4] = {2.4, 4.0, 3.14, 2.0};
    double vector2[4] = {4.0, 6.7, 4.9, -4.5};
    printf("l2-norm: %g\n", l2_norm(vector, 4));
    printf("l1-norm: %g\n", l1_norm(vector, 4));
    printf("l1-norm: %g\n", inf_norm(vector, 4));
    printf("l2-dist: %g\n", l2_dist(vector, vector2, 4, 4));
    printf("l1-dist: %g\n", l1_dist(vector, vector2, 4, 4));
    printf("linf-dist: %g\n", linf_dist(vector, vector2, 4, 4));

    return 0;
}