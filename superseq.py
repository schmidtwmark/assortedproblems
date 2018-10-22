A = list("abc")
B = list("qcd")
C = list("aaqd")
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

def countsuperseq(A, B, count):
    if len(A) == 0 or len(B) == 0:
        return len(A) + len(B) + count
    if(A[-1] == B[-1]):
        return countsuperseq(A[:-1], B[:-1], 1 + count)
    first = countsuperseq(A[:-1], B, 1 + count)
    second = countsuperseq(A, B[:-1], 1 + count)
    return min(first, second)


s =superseq(A, B, seq)

print(superseq(superseq(A,B,[]), C, []))

print(countsuperseq(superseq(A,B,[]), C, 0))
    
