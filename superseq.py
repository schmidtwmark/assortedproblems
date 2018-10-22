A = list("abc")
B = list("qcd")
C = list("aaq")
seq = []
import time
def superseq(A, B, seq):
    if(len(A) == 0):
        return B + seq
    if(len(B) == 0):
        return A + seq
    if (A[-1] == B[-1]): 
        return superseq(A[:-1], B[:-1], [A[-1]] + seq)
    else:
        first = superseq(A[:-1], B, [A[-1]] + seq)
        second = superseq(A, B[:-1], [B[-1]] + seq)
        return first if len(first) < len(second) else second

print(superseq(A, B, seq))

    
