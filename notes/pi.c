#include <stdio.h>
#include <stdlib.h>

#ifdef _OPENMP
#include <omp.h>
#endif

/*global variables*/
static long NUM_STEPS = 10000;
double step;

int main(int argc, char* argv[]){
  int thread_count = atoi(argv[1]); 
  double pi, sum = 0.0;
  step = 1.0 / (double) NUM_STEPS;
  double my_sum = 0.0;
  /*
   * This statement intializes openMP
   * pragma - preprocessor directive
   * omp - call related to the omp library
   * parallel - begin a parallel region and itialize threads
   * num_threads - number of threads to allocate to parallel region
   * private - gives each thread its own copy of the variables in the argument
   */
  # pragma omp parallel num_threads(thread_count) \
       private(my_sum)
  {
    double x;
    
    #ifdef _OPENMP
    int my_rank = omp_get_thread_num();
    printf("hello from rank %d\n", my_rank);
    #endif
    
    /*
     * another preprocessor directive to instruct openMP that it needs
     * to parallelize the for loop below. This will distribute the iterations
     * of the for loop to each thread.
     */
    # pragma omp for 
    for(int i = 0; i < NUM_STEPS; i++){
      x = (i + 0.5) * step;
      my_sum += 4.0 / (1.0 + (x * x));

    }
    /* 
     * This preprocessor directive tells openMP to utilize atomic variables
     * in order to sum all the work of the individual ranks into one variable. 
     * In this case, each thread computed a local sum and these sums are all reduced
     * to one global sum.
     */
    # pragma omp reduction (+: sum)
    sum += my_sum;
  }
  pi = step * sum;

  printf("the approximation of pi obtained is %f\n", pi);
  return 0;
}
