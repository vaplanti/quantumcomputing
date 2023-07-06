import numpy as np

# Ignore errors importing matplotlib.pyplot (may not be available in
# testing framework)
try:
    import matplotlib.pyplot as plt
except ImportError:
    pass

import dimod
from dwave.system import LeapHybridSampler
from dimod import ConstrainedQuadraticModel, Integer
from dwave.system import LeapHybridCQMSampler

def create_model(coeffs):
    x = Integer('x', upper_bound=4)

    y = Integer('y', upper_bound=4)

    a1=int(coeffs[0])
    b1=int(coeffs[1])
    c1=int(coeffs[2])
    a2=int(coeffs[3])
    b2=int(coeffs[4])
    c2=int(coeffs[5])
    cqm = ConstrainedQuadraticModel()
    cqm.set_objective((a1*x+b1*y+c1)**2 + (a2*x+b2*y+c2)**2)
    cqm.add_constraint((a1*x+b1*y+c1)**2 + (a2*x+b2*y+c2)**2==0)
    sampler = LeapHybridCQMSampler()                

    sampleset = sampler.sample_cqm(cqm)                  

    print(sampleset.first)      



def input_coeffs():
    list= [int(i) for i in input("Enter six values: ").split()]

    if (len(list)!=6):
        print ("please input 6 numbers.")

    print("Solving the equations:", list[0], "* x1 + ",list[1], "* x2 + ", list[2], "= 0 and ", list[3], "* x1 +", list[4], "* x2 +", list[5], "= 0")
    return list

def main():
    coeffs=input_coeffs()
    print(coeffs)
    create_model(coeffs)


if __name__ == "__main__":
    main()