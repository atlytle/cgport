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
    
class Pattern:
    def __init__():
        pass
    # We want to generate all GT patterns (|M>) corresponding to a given
    # irrep/iweight. See equation C9 of reference.

if __name__ == "__main__":
    print(comb(4,2))
    #irrep = Irrep([3, 2, 3])
    irrep = Irrep([2, 3, 0])
