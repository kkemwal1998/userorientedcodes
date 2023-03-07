

# Python set


# PYthon final assignment :
# Thus in this, we will be constructing a unit test in order to test our probability distribution functions that we have implemented in project.py .
# This unit test function has been designed to mainly test the probability calculations of the functions.  
from project import Uniform_distribution
from project import Binomial_distribution
from project import Poisson_Distribution
from project import Geometric_Distribution
from project import Negative_Binomial_distribution



def main() :
    test_Uniform_Distribution()
    test_Binomial_distribution()
    test_Poisson_Distribution() 
    test_Geometric_Distribution()
    test_Negative_Binomial_distribution()




def test_Uniform_Distribution() :
    assert Uniform_distribution(12) == 0.08333333333333333
    assert Uniform_distribution(10) == 0.1

def test_Binomial_distribution() :

    assert Binomial_distribution(10,0.6,3) ==   0.042467328000000006
    assert Binomial_distribution(11,0.6,7) == 0.2364899328

def test_Poisson_Distribution() :

    assert Poisson_Distribution(5,8) == 0.06527803935524845
    assert Poisson_Distribution(50,10) ==  5.190544464968974e-12 


def test_Geometric_Distribution() :

    assert Geometric_Distribution(0.7,4) ==  0.018900000000000007

def test_Negative_Binomial_distribution() :

    assert Negative_Binomial_distribution(7,4,0.7) == 0.12965400000000002





if __name__ == "__main__" :
    main()
