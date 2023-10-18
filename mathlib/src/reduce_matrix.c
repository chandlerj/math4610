#include <stdio.h>
#include <stdlib.h>


void reduce_matrix(){
    int size;
    
    printf("\nEnter the size of matrix: ");
    scanf("%d",&size); //determine size of matrix
    double A[size + 2][size + 2],factor,x[size + 1];
    printf("\nEnter the elements of augmented matrix row-wise:\n");
    //get components of matrix
    for(int i=1; i<= size; i++){

        for(int j=1; j<=(size+1); j++){ //iterate to size + 1 to get matrix A and vector 
            printf(" A[%d][%d]:", i,j);
            scanf("%lf",&A[i][j]);
        }
    }

    //put matrix in upper triangular form
    for(int j = 1; j <= size; j++){

        for(int i = 1; i <= size; i++) {

        if(i!=j){
            factor=A[i][j]/A[j][j];
            for(int k = 1; k <= size + 1; k++){
                A[i][k] = A[i][k] - factor * A[j][k];
                // printf("A[%d][%d] = %d\n", i, k, A[i][k]);
                }
            }
        }   
    }

    //use back propogation to find the solutions to the system of equations
    for(int i = 1; i <= size; i++){
        x[i] = A[i][size + 1] / A[i][i];
        printf("\n x%d=%f\n",i,x[i]);
    }

}