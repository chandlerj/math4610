# Questions for Homework 6

**Question 1:** Write code to solve the following root finding problem using
fixed point iteration.
$$
  f(x) = x^2 - 5\ x + 6
$$
For the iteration function, try the usual two cases to test the algorithm
$$
  g(x) = x + f(x)
$$
and
$$
  g(x) = x - f(x)
$$
You should be able to factor and find the roots easily. However, you need
an example where the solution is known. You might want to test the two
iteration functions above for the derivative condition. Show that the
behavior of the sequence of approximations, in fact, verifies what you
thought should happen.

**Question 2** Next, for the input situation in Question 1, try the
following iteration function
$$
  g(x) = x - \epsilon\ f(x)
$$
where $\epsilon>0$. Can the parameter be chosen so that the iteration
function work. Does this work for both root of the quadratic polynomial
in Question 1? Explain and verify the results of your work with the code 
you have written.

**Comment** You do not need to create a software page for the fixed point iteration problems above.

**Question 3**  Write a code that will use the Bisection method to
compute the roots of a function, $f(x)$. To test your code, use the
function in Question 1. Note that there are two roots. You should be able
to use this as a means to enforce the negativity of $f(a)\cdot f(b)<0$.
Write up the results obtained and add an entry with a software page
related to your Bisection method code.

**Question 4.** Repeat the work in Question 3 for Newton's method.

**Question 5.** Repeat the work in Question 3 for the Secant method.

**Question 6.** Repeat the work in Question 3 for a hybrid method that 
uses Bisection to narrow down the location of the root and uses the 
secant method to narrow down the root location at a faster rate.

**Question 7.** A potential user would like you to package a few of the
root finding routines that have been developed in class. The user would
like to primarily  work with a hybrid method that you developed in
determine roots in Question 6. In addition, the user wants a routine that
is guaranteed to converge if an interval actually contains at least one
root. This means a version of the Bisection method to verify the result.
Build this set of routines into a package that can help this used. Make
sure that the package has a test code in it to provide the user with a
known usage and results.

**Question 8.** The same user has actually defined a problem where the
logistic differential equation is being used to model thhe population of
some type of pest species. The Logisitic ODE is of the form
$$
  \frac{dP}{dt} = \alpha\ P - \beta\ P
$$
with an initial condition, $P(0)=P_0$. Playing the role of the user of the
codes, determine if the population density of the pest species reaches 
$\P_\infty$, for the situations given below. If the species reaches the given
level, determine the time at which the density hits the given level.

**a.** $\alpha=0.1, \beta=0.001, P_0=2, P_\infty=29.75$.

**b.** $\alpha=0.1, \beta=0.001, P_0=2, P_\infty=115.35$

**c.** $\alpha=0.1, \beta=0.0001, P_0=2, P_\infty=115.35$

**d.** $\alpha=0.01, \beta=0.001, P_0=2, P_\infty=155.346$

**e.** $\alpha=0.1, \beta=0.01, P_0=100, P_\infty=155.346$