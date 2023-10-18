# Math 4610 Fundamentals of Computational Mathematics: `mathlib` manual

# Table of Contents
1. [smaceps](#smaceps)
2. [dmaceps](#dmaceps)
3. [fx](#fx)
4. [dfapp-forward](#dfapp_forward)
5. [dfapp-backward](#dfapp_backward)
6. [dfapp-central](#dfapp_central)
7. [l1-dist](#l1_dist)
8. [l1-norm](#l1_norm)
9. [l2-norm](#l2_norm)
10. [l2-dist](#l2_dist)
11. [inf-norm](#inf_norm)
12. [linf-dist](#linf_dist)
13. [reduce-matrix](#reduce-matrix)




## smaceps
**Routine Name:**           smaceps

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc smaceps.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o smaceps smaceps.c

**Description/Purpose:** This routine will compute the single precision value for the machine epsilon or the number of digits
in the representation of real numbers in single precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

**Input:** There are no inputs needed in this case.

**Output:** This routine returns a single precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

This routine will iteratively reduce the value of a divisor until the smallest value is obtained that be computed with a `32 bit float`

    printf("32 bit macepts value: %g\n", smaceps());

Output from the lines above:

    32 bit macepts value 5.96046e-08



**Implementation/Code:** The following is the code for smaceps()

```
#include <stdio.h>
#include <math.h>

float smaceps(){
    //float gives about 8 digits of precision. use double for double precision
    float one, appone, h, error; 
    one = 1.0;
    h = 1.0;
    appone = one + h;
    error = fabs(appone - one);
    while(error > 0.0){
        h = h / 2.0;
        appone = one + h;
        error = fabs(appone - one);
        // printf("error = %g  h = %g\n", error, h);
    }
    return h;
}
```

**Last Modified:** Oct/2023



## dmaceps
**Routine Name:**           dmaceps

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc dmaceps.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o smaceps smaceps.c

**Description/Purpose:** This routine will compute the double precision value for the machine epsilon or the number of digits
in the representation of real numbers in double precision. This is a routine for analyzing the behavior of any computer. This
usually will need to be run one time for each computer.

**Input:** There are no inputs needed in this case.

**Output:** This routine returns a double precision value for the number of decimal digits that can be represented on the
computer being queried.

**Usage/Example:**

This routine will iteratively reduce the value of a divisor until the smallest value is obtained that be computed with a `64 bit float`

    printf("64 bit macepts value: %g\n", dmaceps());

Output from the lines above:

    64 bit macepts value 1.11022e-16



**Implementation/Code:** The following is the code for dmaceps()

```
#include <stdio.h>
#include <math.h>

double dmaceps(){
    //float gives about 8 digits of precision. use double for double precision
    double one, appone, h, error; 
    one = 1.0;
    h = 1.0;
    appone = one + h;
    error = fabs(appone - one);
    while(error > 0.0){
        h = h / 2.0;
        appone = one + h;
        error = fabs(appone - one);
        // printf("error = %g  h = %g\n", error, h);
    }
    return h;
}
```

**Last Modified:** Oct/2023

## fx
**Routine Name:**           fx

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc fx.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o fx fx.c

**Description/Purpose:** This routine will return the value of a function `f(x)`. The funciton being evaluated must be modified in the source. This is primarily a helper function for the derivative approximation functions.

**Input:** `x`: the value you want to evaluate a function at.

**Output:** This function has no output, but will return the value of the function at a point `x`.

**Usage/Example:**

This routine will provide the value of a function at a point `x`

    printf("x^2 at x = 3: %g\n", f(3));

Output from the lines above:

    x^2 at x = 3: 9



**Implementation/Code:** The following is the code for f(x)

```
double f(double x){
    double fval = x * x;

    return fval; 
}
```

**Last Modified:** Oct/2023


## dfapp_forward
**Routine Name:**           dfapp_forward

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc dfapp_forward.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o dfapp_forward dfapp_forward.c

**Description/Purpose:** This routine will return a derivative approximation using the forward derivative approximation method at a given `x` and `h`.

**Input:** 
*   `x`: the value you want to evaluate a function at.
*   `h`: the `h` value you want to use for your approximation

**Output:** This function has no output, but will return the value of the approximation of the derivative of a function at a point `x`.

**Usage/Example:**

This routine will provide the value of a function at a point `x`

    printf("forward approx of derivative of x * x at x = 10, h = 0.01: %g\n", dfapp_forward(10, 0.01));

Output from the lines above:

    forward approx of derivative of x * x at x = 10, h = 0.01: 20.01



**Implementation/Code:** The following is the code for dfapp_forward

```
double dfapp_forward(double x, double h){
    double appval = (f(x + h) - f(x)) / h;
    return appval;
}
```

**Last Modified:** Oct/2023


## dfapp_backward
**Routine Name:**           dfapp_backward

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc dfapp_backward.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o dfapp_backward dfapp_backward.c

**Description/Purpose:** This routine will return a derivative approximation using the forward derivative approximation method at a given `x` and `h`.

**Input:** 
*   `x`: the value you want to evaluate a function at.
*   `h`: the `h` value you want to use for your approximation

**Output:** This function has no output, but will return the value of the approximation of the derivative of a function at a point `x`.

**Usage/Example:**

This routine will provide the value of a function at a point `x`

    printf("backwards approx of derivative of x * x at x = 10, h = 0.01: %g\n", dfapp_backward(10, 0.01));

Output from the lines above:

    backwards approx of derivative of x * x at x = 10, h = 0.01: 19.99



**Implementation/Code:** The following is the code for dfapp_forward

```
double dfapp_backward(double x, double h){
    double appval = (f(x) - f(x - h)) / h;
    return appval;
}
```

**Last Modified:** Oct/2023


## dfapp_central
**Routine Name:**           dfapp_central

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc dfapp_central.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o dfapp_central dfapp_central.c

**Description/Purpose:** This routine will return a derivative approximation using the forward derivative approximation method at a given `x` and `h`.

**Input:** 
*   `x`: the value you want to evaluate a function at.
*   `h`: the `h` value you want to use for your approximation

**Output:** This function has no output, but will return the value of the approximation of the derivative of a function at a point `x`.

**Usage/Example:**

This routine will provide the value of a function at a point `x`

    printf("central approx of derivative of x * x at x = 10, h = 1: %g\n", dfapp_central(10, 1));

Output from the lines above:

    central approx of derivative of x * x at x = 10, h = 1: 20



**Implementation/Code:** The following is the code for dfapp_central

```
double dfapp_central(double x, double h){
    double appval = (f(x + h) - f(x - h)) / 2.0 * h;
    return appval;
}
```

**Last Modified:** Oct/2023

## l1_dist
**Routine Name:**           l1_dist

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc l1_dist.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o l1_dist l1_dist.c

**Description/Purpose:** This function will return the sum of the absolute values of the components of the difference of two vectors

**Input:** 
*   `v1`: the first vector you want to use
*   `v2`: the second vector you want to use
*   `v1_len`: the length of the first vector
*   `v2_len`: the length of the second vector

**Output:** This function will return the sum of the sum of the absolute values of the components of the difference of two vectors as a `double`

**Usage/Example:**

    double vector[4] = {2.4, 4.0, 3.14, 2.0};
    double vector2[4] = {4.0, 6.7, 4.9, -4.5};
    printf("l1-dist: %g\n", l1_dist(vector, vector2, 4, 4));

Output from the lines above:

    l1-dist: 12.56



**Implementation/Code:** The following is the code for l1_dist

```
#include <math.h>
#include <stdio.h>

double l1_dist(double v1[], double v2[], int v1_len, int v2_len){

    if(v1_len != v2_len){
        printf("ERROR: length of vectors not the same. Result will not be accurate\n");
    }
    double sum = 0;

    for(int i = 0; i < v1_len; i++){
        double distance = v1[i] - v2[i];

        sum += fabs(distance);
    }

    return sum;
}
```

**Last Modified:** Oct/2023

## l1_norm
**Routine Name:**           l1_norm

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc l1_norm.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o l1_norm l1_norm.c

**Description/Purpose:** This function will return the sum of the absolute values of the components of two vectors

**Input:** 
*   `v`: the vector you want to use
*   `vec_len`: the length of the vector

**Output:** This function will return the sum of the sum of the components of the difference of two vectors as a `double`

**Usage/Example:**

    double vector[4] = {2.4, 4.0, 3.14, 2.0};
    printf("l1-norm: %g\n", l1_norm(vector, 4));

Output from the lines above:

    l1-norm: 11.54



**Implementation/Code:** The following is the code for l1_norm

```
#include <math.h>

double l1_norm(double v[], int vec_len){
    double sum = 0.0;
    for(int i =0; i < vec_len; i++){
        sum += fabs(v[i]);
    }
    return sum;
}
```

**Last Modified:** Oct/2023

## l2_norm
**Routine Name:**           l2_norm

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc l2_norm.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o l2_norm l2_norm.c

**Description/Purpose:** This function will return the euclidean length of a vector

**Input:** 
*   `v`: the vector you want to use
*   `vec_len`: the length of the vector

**Output:** This function will return the sum of the sum of the components of the difference of two vectors as a `double`

**Usage/Example:**

    double vector[4] = {2.4, 4.0, 3.14, 2.0};
    printf("l2-norm: %g\n", l2_norm(vector, 4));

Output from the lines above:

    l2-norm: 5.96822



**Implementation/Code:** The following is the code for l2_norm

```
#include <stdio.h>
#include <math.h>

double l2_norm(double v[], int vec_len){
    double sum = 0.0;
    for(int i =0; i < vec_len; i++){
        sum += v[i] * v[i];
    }
    sum = sqrt(sum);
    return sum;
}
```

**Last Modified:** Oct/2023

## l2_dist
**Routine Name:**           l2_dist

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc l2_dist.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o l2_dist l2_dist.c

**Description/Purpose:** This function will return the l2-norm of the difference of two vectors

**Input:** 
*   `v1`: the first vector you want to use
*   `v2`: the second vector you want to use
*   `v1_len`: the length of the first vector
*   `v2_len`: the length of the second vector

**Output:** This function will return the l2-norm of the difference of two vectors

**Usage/Example:**

    double vector[4] = {2.4, 4.0, 3.14, 2.0};
    double vector2[4] = {4.0, 6.7, 4.9, -4.5};
    printf("l2-dist: %g\n", l2_dist(vector, vector2, 4, 4));

Output from the lines above:

    l2-dist: 7.42951



**Implementation/Code:** The following is the code for l1_norm

```
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
```

**Last Modified:** Oct/2023


## inf_norm
**Routine Name:**           inf_norm

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc inf_norm.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o inf_norm inf_norm.c

**Description/Purpose:** This function will return the largest component in the magnitude of a vector

**Input:** 
*   `v`: the vector you want to use
*   `vec_len`: the length of the vector

**Output:** This function will return the largest component in the magnitude of a vector as a `double`

**Usage/Example:**

    double vector[4] = {2.4, 4.0, 3.14, 2.0};
    printf("inf-norm: %g\n", inf_norm(vector, 4));

Output from the lines above:

    inf-norm: 4



**Implementation/Code:** The following is the code for l2_norm

```
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
```

**Last Modified:** Oct/2023

## linf_dist
**Routine Name:**           linf_dist

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc linf_dist.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o linf_dist linf_dist.c

**Description/Purpose:** This function will return the largest component in the magnitude of a vector

**Input:** 
*   `v1`: the first vector you want to use
*   `v2`: the second vector you want to use
*   `v1_len`: the length of the first vector
*   `v2_len`: the length of the second vector

**Output:** This function will return the largest component in the magnitude of a vector as a `double`

**Usage/Example:**

    double vector[4] = {2.4, 4.0, 3.14, 2.0};
    printf("inf-norm: %g\n", inf_norm(vector, 4));

Output from the lines above:

    inf-norm: 4



**Implementation/Code:** The following is the code for l2_norm

```
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
```

**Last Modified:** Oct/2023

## linreg
**Routine Name:**           linreg

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc linreg.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o linreg linreg.c

**Description/Purpose:** This function will return the largest component in the magnitude of the difference between two vectors

**Input:** 
*   `x_vec`: vector representing the x components of a set of ordered pairs
*   `y_vec`: vector representing the y components of a set of ordered pairs
*   `length`: the length of the set of ordered pairs

**Output:** This function will return a string with the linear equation that best fits the set of ordered pairs as a `char*`

**Usage/Example:**

    double vec1[] = {2,3,5,7,9};
    double vec2[] = {4,5,7,10,15};

    const char* best_fit = linreg(vec1, vec2, 5);
    printf("linear regression of (2,4), (3,5), (5,7), (7,10), (9,15): %s",best_fit);

Output from the lines above:

    linear regression of (2,4), (3,5), (5,7), (7,10), (9,15): y = 1.518293x + 0.304878



**Implementation/Code:** The following is the code for linreg

```
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
```

**Last Modified:** Oct/2023

## reduce-matrix
**Routine Name:**           reduce-matrix

**Author:** Chandler Justice

**Language:** `C`; The code can be compiled using `gcc`.

For example,

    gcc reduce-matrix.c

will produce an executable `./a.o` than can be executed. If you want a different name, the following will work a bit
better

    gcc -o reduce-matrix reduce-matrix.c

**Description/Purpose:** This function will reduce a square matrix into upper triangular form allowing for a linear system to be solved

**Input:** 
This function takes no input, but uses the terminal to accept user input about the size and components of the matrix

**Output:** This will function will print the components of the resulting matrix `x`.

**Usage/Example:**
```
Enter the size of matrix: 3

Enter the elements of augmented matrix row-wise:
 A[1][1]:3
 A[1][2]:2 
 A[1][3]:-4
 A[1][4]:3
 A[2][1]:2
 A[2][2]:3
 A[2][3]:3
 A[2][4]:15
 A[3][1]:5
 A[3][2]:-3
 A[3][3]:1
 A[3][4]:14

 x1=3.000000

 x2=1.000000

 x3=2.000000
```




**Implementation/Code:** The following is the code for linreg

```
#include <stdio.h>
#include <stdlib.h>


void reduce_matrix(){
    int size;
    
    printf("\nEnter the size of matrix: ");
    scanf("%d",&size);
    double A[size + 2][size + 2],factor,x[size + 1];
    printf("\nEnter the elements of augmented matrix row-wise:\n");
    for(int i=1; i<= size; i++)
    {
        for(int j=1; j<=(size+1); j++)
        {
            printf(" A[%d][%d]:", i,j);
            scanf("%lf",&A[i][j]);
        }
    }

    for(int j = 1; j <= size; j++){

        for(int i = 1; i <= size; i++) {

        if(i!=j){
            factor=A[i][j]/A[j][j];
            for(int k = 1; k <= size + 1; k++)
            {
                
                A[i][k] = A[i][k] - factor * A[j][k];
                // printf("A[%d][%d] = %d\n", i, k, A[i][k]);
            }
        }
    }

    
    }

    for(int i = 1; i <= size; i++){
        x[i] = A[i][size + 1] / A[i][i];
        printf("\n x%d=%f\n",i,x[i]);
    }

}
```

**Last Modified:** Oct/2023