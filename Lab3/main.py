#lab3
import random
import copy

class Clause: 
    def __init__(self, p, n):
        self.p = set(p)
        self.n = set(n) 

    def __str__(self):
        return "p: " + str(self.p) + ", n: " + str(self.n)
    
    def __hash__(self):
    #freezes a set so it doesnt change, 
    #remains the same, frozensets can be used as keys
        return hash((frozenset(self.p), frozenset(self.n)))
    
      # equal between two hash values
    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return NotImplemented
        return self.p == other.p and self.n == other.n

    def is_subset(self, other):
        return self.p.issubset(other.p) and self.n.issubset(other.n)

def resolution(A, B):
    A_copy = copy.deepcopy(A)
    B_copy = copy.deepcopy(B)
    if not (A_copy.p.intersection(B_copy.n)) and not (A_copy.n.intersection(B.p)):
        return False # There is no solution (no intersection)
    if (A_copy.p.intersection(B_copy.n)):
        a = random.choice(list(A_copy.p.intersection(B_copy.n)))
        A_copy.p.remove(a) # Removes element a from the set if its in the intersection
        B_copy.n.remove(a)
    else:
        a = random.choice(list(A.n.intersection(B.p)))
        A_copy.n.remove(a) 
        B_copy.p.remove(a)

    C = Clause(p = set(A_copy.p).union(B_copy.p), n = set(A_copy.n).union(B_copy.n))
    #C.p.add(A.p.union(B.p)) # Adds the union 
    #C.n.add(A.n.union(B.n))
    if C.p.intersection(C.n): # C is tautology (always true)
        return False
    # C is a set so it should not have any duplicates by default
    return C # Returns resolvent of A & B or false


def solver(KB):
    while True:
        S = set()
        #KB_copy = copy.deepcopy(KB)
        KB_prim = copy.deepcopy(KB) 
        #for A,B in enumerate(KB):
        my_list = list(KB)
        for i in range(len(KB)-1):
            for j in range(i+1, len(KB)):
                C = resolution(my_list[i], my_list[j])
                if C is not False:
                    S = S | set({C})
        if not S:
            return KB
        KB = incorporate(S, KB)
        if KB_prim == KB:
            break
    return KB

def incorporate(S, KB): # S: set of clauses, KB: set of clauses
    for A in copy.deepcopy(S):
        KB = incorporate_clause(A, KB)
    return KB

def incorporate_clause(A, KB): # A: clause, KB: Set of clauses
    for B in copy.deepcopy(KB):
        if B.is_subset(A):
            return KB
    for B in copy.deepcopy(KB): 
        if A.is_subset(B):
            KB.remove(B)
    KB = KB.union(set({A}))
    return KB

ice = 'a'
sun = 'b'
money = 'c'
movie = 'd'
cry = 'e'
A4 = Clause(p = {'ice'}, n = {'sun', 'money'})
B4 = Clause(p = {'ice', 'movie'}, n = {'money'})
C4 = Clause(p = {'money'}, n = {'movie'})
D4 = Clause(p = {}, n = {'movie', 'ice'})
E4 = Clause(p = {'sun', 'money', 'cry'}, n = {})
F4 = Clause(p = {'movie'}, n = {})

KB = set({A4, C4, D4, E4, F4})

KB1 = incorporate(S={}, KB=KB)
result4 = solver(KB1)

for C in result4: 
    print(C)
