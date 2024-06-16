#!/usr/bin/env python3
# Andrew Lytle
# June 2024

import sys
from math import comb

# Following XII (p.13) of 1009.0437, the first step is to
# 1) Find irreps of S'' appearing in SxS'
# This is done using "patterns". Patterns represent the
# the states of an irrep. An irrep of SU(N) is specified by
# N decreasing integers (in canonical form we can always take
# the last element to be 0).

class Irrep:
    def __init__(self, iweight):
        self.N = len(iweight)  # Specifies SU(N) irrep.
        #self.validate_iweight(iweight)
        self.iweight = self.validate(iweight)

    def validate(self, iweight):
        "Check values are in descending order."
        _m = None
        for i, m in enumerate(iweight):
            if _m is not None:
                try:
                    assert(m < _m)
                except AssertionError:
                    print("iweight is not valid:")
                    print(f"iweight[{i}]={m} >= iweight[{i-1}]={_m}.")
                    print(f"{iweight = }")
                    sys.exit(1)
            _m = m
        return iweight
    
    def dim(self):
        # Closed form expression Eq 22 of reference.
        "Dimension of irrep."
        pass
    
class Pattern:
    def __init__(self, _Irrep):
        "By default returns the highest weight state in Irrep"
        self.Irrep = _Irrep
        N = self.Irrep.N
        #print(f"{N=}")
        self.L = int(N*(N+1)/2)  # Number of entries in a pattern.
        #print(f"{self.L=}")
        self.m = [0]*self.L  # Initialize pattern data.
        # Top row is the iweight.
        for k in range(N):
            self.m[k] = self.Irrep.iweight[k]
        for l in reversed(range(1, N)):
            for k in range(1, l+1):
                #print(f"{k = } {l = }")
                _id = self.id(k,l)
                #print(f"{_id = }")
                self.m[_id] = self.get(k, l+1)
    
    # We want to generate all GT patterns (|M>) corresponding to a given
    # irrep/iweight. See equation C9 of reference.

    def id(self, k, l):
        N = self.Irrep.N
        _index = (N*(N+1)-l*(l+1))/2 + (k-1)
        return int(_index)
    
    def get(self, k, l):
        "m_{k,l}"
        N = self.Irrep.N
        _index = (N*(N+1)-l*(l+1))/2 + (k-1)
        _index = int(_index)
        #print(f"{_index=}")
        return self.m[_index]
    
    def __str__(self):
        "String representation of GT pattern."
        res = ""
        pad = ""
        N = self.Irrep.N
        for l in reversed(range(1, N+1)):
            for k in range(1, l+1):
                res += str(self.get(k,l)) + " "
            pad += " "
            res += "\n" + pad
        return res

if __name__ == "__main__":
    #irrep = Irrep([3, 2, 3])
    irrep = Irrep([2, 1, 0])
    pattern = Pattern(irrep)
    #print(pattern.get(1, 1))
    print(pattern.m)
    print(pattern)
