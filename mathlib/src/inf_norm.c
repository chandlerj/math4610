#include <math.h>

double inf_norm(double v[], int vec_len){
    double max = 0;

    for(int i = 0; i < vec_len; i++){
        double curr_element = fabs(v[i]);
        if(curr_element > max){
            max = curr_element;
        }
    }
    return max; 
}