// #include "fx.c"

// double f(double x);

double dfapp_forward(double x, double h){
    double appval = (f(x + h) - f(x)) / h;
    return appval;
}