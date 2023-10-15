// #include "fx.c"

// double f(double x);

double dfapp_central(double x, double h){
    double appval = (f(x + h) - f(x - h)) / 2.0 * h;
    return appval;
}