## MATH4610: HW04
Chandler Justice - A02313187

**Question 1**: Create files for the individual routeines we have discussed in class.

I created the following routines in the `src` directory of my `mathlib` directory:

```
dfapp_backward.c
dfapp_central.c
dfapp_forward.c
dmaceps.c
fx.c
inf_norm.c
l1_dist.c
l1_norm.c
l2_dist.c
l2_norm.c
linf_dist.c
linreg.c
reduce_matrix.c
smaceps.c
test-lib.c
```

which can be found on my github repositiory at [this link](https://github.com/chandlerj/math4610/tree/main/mathlib/src).

**Question 2**: Create object modules for the routines

I created the following object modules in the `out` directory of my `mathlib` directory.

```
dfapp_backward.o	
dmaceps.o		
l1_dist.o		
l2_norm.o		
dfapp_central.o		
fx.o			
l1_norm.o		
linf_dist.o		
reduce_matrix.o
dfapp_forward.o		
inf_norm.o		
l2_dist.o		
linreg.o		
smaceps.o
```
Which can be found on my github repository at [this link](https://github.com/chandlerj/math4610/tree/main/mathlib/out)

**Question 3**: Use the `ar` command to create your library of routines

My `mathlib.a` library can be found on my github at [this link](https://github.com/chandlerj/math4610/blob/main/mathlib/out/mathlib.a)

**Question 4**: Use the `ranlib` command to create an index of the library. Verify the results with `ar -t`.

Here is the output from my terminal when I run `ar -t mathlib.a`:

```
chandler@merci out % ar -t mathlib.a 
__.SYMDEF
dfapp_backward.o
dfapp_central.o
dmaceps.o
fx.o
inf_norm.o
l1_dist.o
l1_norm.o
l2_dist.o
l2_norm.o
linf_dist.o
linreg.o
reduce_matrix.o
smaceps.o
```

**Question 5**: compile and test your codes with the test routine you created

Here is the output of my test routine. The code for this routeine can be found at [this link](https://github.com/chandlerj/math4610/blob/main/mathlib/src/test-lib.c)

```
chandler@merci src % ./test
32 bit macepts value: 5.96046e-08
64 bit macepts value: 1.11022e-16
l2-norm: 5.96822
l1-norm: 11.54
inf-norm: 4
l2-dist: 7.42951
l1-dist: 12.56
linf-dist: 6.5
forward approx of derivative of x * x at x = 10, h = 0.01: 20.01
central approx of derivative of x * x at x = 10, h = 1: 20
backwards approx of derivative of x * x at x = 10, h = 0.01: 19.99
linear regression of (2,4), (3,5), (5,7), (7,10), (9,15): y = 1.518293x + 0.304878
```

**Question 6**: Create a software documentation page for each of the routeines you have created




