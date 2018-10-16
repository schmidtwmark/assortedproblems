
import sys
word = input("Enter a string\n")

def cost1(h):
    if h >= 1:
        return 1
    else:
        return 0

def cost2(h):
    k = 3 #minimum length of palindromes
    if h < k:
        return 1
    else:
        return 0

cost_function = cost1

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
        return cost_function(n), []
    pals = getPalindromes(string)
    best = sys.maxsize
    best_set = []
    for pal in pals:
        i = len(pal)
        other, other_set = decomp(string[i:])
        total = cost_function(i) + other
        if total < best:
            best = total
            best_set = [pal] + other_set
    return best, best_set

print(decomp(word))

