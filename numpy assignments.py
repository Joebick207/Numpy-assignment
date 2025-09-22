import numpy as np
import sys
A=np.array([[1,2],
           [3,4]])
B=np.array([[5,6],
           [7,8]])
C_add=A+B
print("Element_wise addition: \n",C_add)
C_mul=A*B
print("Element_wise multiplication: \n",C_mul)
C_dot=A@B
print("Matrix product)(A@B: \n",C_dot)
def main():

    return 0
if __name__=="__main__":
    sys.exit(main())