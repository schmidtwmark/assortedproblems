
import sys
word = input("Enter a string\n")

def cost(h):
    if h >= 1:
        return 1
    else:
        return 0

def cost_alt(h):
    k = 3 #minimum length of palindromes
    if h < k:
        return 1
    else:
        return 0

def getPalindromes(string):
    ret = []
    for i in range(len(string) + 1):
        if i == 0:
            continue
        a = string[0:i]
        b = string[0:i][::-1]
        if a == b:
            ret.append(a)
    return ret

def decomp(string):
    n = len(string)
    if(n <= 1):
        return cost_alt(n)
    pals = getPalindromes(string)
    best = sys.maxsize
    for pal in pals:
        i = len(pal)
        other = decomp(string[i:])
        total = cost(i) + other
        if total < best:
            best = total
    return best

print(decomp(word))

