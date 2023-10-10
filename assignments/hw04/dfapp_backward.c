#include "fx.c"

double f(double x);

double dfapp_backward(double x, double h){
    double appval = (f(x) - f(x - h)) / h;
    return appval;
}