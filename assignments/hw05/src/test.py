import gausElim, backsub, matrixVector,LUDefactor, forwardElim, diagMatrix
import numpy as np
def main():
    #Testing Gaus elim
    [A, y0, b] = diagMatrix.createDiagDominantMatrix(10)

    [guas_elim , y1] = gausElim.Gaus_elim(A, b)
    final_result = backsub.backSub(guas_elim, y1)

    error = np.zeros(10)
    for i in range(10):
        error[i] = abs(final_result[i] - y0[i])
    
    print(f'the error of the GE function is represented by this vector:\n{error}')

    # testing LU Defactorization
    [A_lu, y0_lu, b_lu] = diagMatrix.createDiagDominantMatrix(10)

    [lower_m , upper_m] = LUDefactor.LU_Defactor(A_lu)

    z_lu = matrixVector.multiplyMatrixByVector(lower_m, b_lu)
    
    z1_lu = forwardElim.forward_elim(lower_m, z_lu)

    x_lu = backsub.backSub(upper_m, z1_lu)

    error_lu = np.zeros(10)
    for i in range(10):
        error_lu[i] = abs(x_lu[i] - y0_lu[i]) 
    print(f'the error of the LU-factorization function is represented by this vector:\n {error_lu}')






main()
