"""
homework9
andrewID: siyuchen



Starting from the Polynomial class in the class notes, edit that class and
also implement the Quadratic class so that all the tests below succeed.

Be sure not to hardcode against these tests, as the autograder will use
similar tests, but with different constants.  You may need to study some
of the tests to understand what is going on, and you may well need to
do some of the required reading, and perhaps also some googling, to figure
out how to solve some of these.

You are also responsible for understanding how the tests themselves work.
For example, understand how the list of first-class functions is being used
in testPolynomialAndQuadraticClasses, and also understand why the try/except
calls are used in testQuadraticClass.

Good luck!
"""
import copy
import math
# The start of a very basic Polynomial class...
class Polynomial(object):
    def __init__(self, *coeffs):
        # if coeffs == [2,-3,5]:  2x**2-3*x+5
        # @TODO: eliminate leading zero's
        if len(coeffs)==0 :# thet input is empty Polynomial()
            coeffs= [0]
        elif type(coeffs[0])!=int:# the first is a list or a tuple
            coeffs=coeffs[0]
            if len(coeffs)==0:
                coeffs=[0]
        # each element is int
        # move the leading zeros
        coeffsCopy=list(copy.copy(coeffs))
        if(len(coeffsCopy)>1):
            start=0
            while (coeffsCopy[start]==0):
                coeffsCopy.pop(0)
        self.coeffs = coeffsCopy
    
    def degree(self):
        # The degree is power of the largest exponent, and since
        # we start at x**0, this is one less than the number of coefficients.
        return len(self.coeffs)-1
    
    def coeff(self, power):
        # This returns the coefficient corresponding to the given power.
        # Note that these are stored in reverse, in that the coefficient
        # for x**0 is not stored in coeffs[0] but rather coeffs[-1].
        return self.coeffs[self.degree()-power]
    
    def evalAt(self, x):
        # Evaluate this polynomial at the given value of x.
        return sum([self.coeff(power)*x**power
                    for power in xrange(self.degree()+1)])

    def __add__(self, other):
        # Add this polynomial to another polynomial, producing a third
        # polyonial as the result.  This makes the + operator work right.
        # First, make both coefficent lists the same length by nondestructively
        # adding 0's to the front of the shorter one
        (coeffs1, coeffs2) = (self.coeffs, other.coeffs)
        if (len(coeffs1) > len(coeffs2)):
            (coeffs1, coeffs2) = (coeffs2, coeffs1)
        # Now, coeffs1 is shorter, so add 0's to its front
        coeffs1 = [0]*(len(coeffs2)-len(coeffs1)) + coeffs1
        # Now they are the same length, so add them to get the new coefficients
        coeffs = [coeffs1[i] + coeffs2[i] for i in xrange(len(coeffs1))]
        # And create the new Polynomial instance with these new coefficients
        return Polynomial(coeffs)

    def __eq__(self,other):
        # for condition where the degree should be zero
        if self.degree()==0:
            return self.coeffs[0]==other
        if(type(self)==type(other)):
            return (self.coeffs==other.coeffs)
        else:
            return False

    def __hash__(self):
        # everytyhing in the hashbale things should be immutable
        thingstoHash = (tuple(self.coeffs))
        return hash(thingstoHash)

    def derivative(self):
        # Take the first derivative of this polynomial, returning the result
        # as a new polynomial.  For example:
        # f(x)  = A*x**3 + B*x**2 + C*x**1 + D
        # f'(x) = 3*A*x**2 + 2*B*x**1 + 1*C   [ 3*A, 2*B, 1*C ]
        coeffs = [ power*self.coeff(power)
                   for power in xrange(self.degree(), 0, -1)]
        return Polynomial(coeffs)

    def __repr__(self):
        # using what he machine learnt and then output it as eval will give 
        # the real value of it
        return "Polynomial("+repr(self.coeffs)+")"

    def __str__(self):
        # Convert this polynomial into a human-readable string.
        # This is not a very good string implementation. Ugly, but functional.
        result = ""
        # if the degree == 0 we will only return the coeff
        if self.degree()==0:
            result += str(self.coeff(0))
            return result 
        for power in xrange(self.degree(), -1, -1):
            coeff = self.coeff(power)
            if(coeff !=0):
                if (result != "" ): result += " + " if coeff >=0 else " - "
                if power==0:
                    result += str(abs(coeff))
                elif power==1 :
                    result += "%dx" % abs(coeff)
                elif coeff==1 :
                    result +="x^%d" % power
                elif coeff==-1:
                    result +="-x^%d" % power
                else:
                    result += "%dx^%d" % (abs(coeff), power)
        return result

    # read the hint part 
    # if the left side is an integer the right side is an instance of object
    def __rmul__(self,other):
        if type(other)==int:
            totalCoeffs=[e*other for e in self.coeffs]
        else:
            totalDegree = self.degree()+other.degree()
            totalCoeffs = [0]*(totalDegree+1)
            for i in xrange(self.degree()+1):
                for j in xrange(other.degree()+1):
                    totalCoeffs[i+j] += self.coeffs[i]*other.coeffs[j]
        return Polynomial(totalCoeffs)

    # redefine the multiple function
    def __mul__(self,other):
        if type(other)==int:
            totalCoeffs=[e*other for e in self.coeffs]
        else:
            totalDegree = self.degree()+other.degree()
            totalCoeffs = [0]*(totalDegree+1)
            for i in xrange(self.degree()+1):
                for j in xrange(other.degree()+1):
                    totalCoeffs[i+j] += self.coeffs[i]*other.coeffs[j]
        return Polynomial(totalCoeffs)

    def __pow__(self,number):
        # check different conditions
        if number==0:
            return 1
        # when the number ==1 just record the coeffs
        elif number==1:
            return Polynomial(self.coeffs)
        else:
            result = Polynomial(self.coeffs)
            for i in xrange(number-1):
                result = result * Polynomial(self.coeffs)
            return result



class Quadratic(Polynomial):
    # make the input argument a list
    
    def __init__(self,*coeffs):
        limitLength =3
        if (len(coeffs)>limitLength or len(coeffs)<limitLength):
            raise Exception()
        elif(len(coeffs)<limitLength):
            raise Exception()
        else:
            super(Quadratic,self).__init__(coeffs)
    # function determinant where I need to set the coeffs
    def determinant(self):
        coeffs = self.coeffs
        determinantCoeffs=4
        determinant = coeffs[1]**2-determinantCoeffs*coeffs[0]*coeffs[2]
        return determinant
    # get the number of real Roots
    def numberOfRealRoots(self):
        determinant = self.determinant()
        if determinant<0:
            return 0
        elif determinant==0:
            return 1
        else:
            return 2
    # method to compute the real roots
    def getRealRoots(self):
        coeffs = self.coeffs
        if self.numberOfRealRoots()==0:
            return [ ]
        elif self.numberOfRealRoots()==1:
            root = [-float(coeffs[1])/2/float(coeffs[0])]
        else:
            root=[]
            delta = math.sqrt(self.determinant())
            root.append((-float(coeffs[1])- delta)/2/float(coeffs[0]))
            root.append((-float(coeffs[1])+ delta)/2/float(coeffs[0]))
        return root

######################################################################
##### ignore_rest: The autograder will ignore all code below here ####
######################################################################

def testPolynomialAndQuadraticClasses():
    print "Testing Polynomial and Quadratic classes..."
    for testFn in [testPolynomialBasicsFromClassNotes,
                   testPolynomialEq,
                   testPolynomialStr,
                   testPolynomialRepr,
                   testPolynomialConstructor,
                   testPolynomialInSets,
                   testPolynomialTimesOperator,
                   testPolynomialExponentiationOperator,
                   testQuadraticClass
                  ]:
        print "  Running %s..." % testFn.__name__,
        testFn()
        print "Passed!"
    print "Passed all Polynomial and Quadratic Class tests!"

def almostEqual(d1, d2):
    epsilon = 0.000001
    return abs(d1 - d2) < epsilon

def testPolynomialBasicsFromClassNotes():
    # Commented out the string assertions since we actually
    # changed/improved those as part of this hw
    p1 = Polynomial([2, -3, 5])  # 2x**2 -3x + 5
    #assert(str(p1) == "2*x**2+-3*x**1+5*x**0") # ugly, but functional
    assert(type(p1) == Polynomial)
    print p1.degree()
    assert(p1.degree() == 2)
    assert(p1.coeff(0) == 5)
    assert(p1.coeff(1) == -3)
    assert(p1.coeff(2) == 2)
    assert(p1.evalAt(0) == 5)
    assert(p1.evalAt(2) == 7)
    # Now test the derivative method
    p2 = p1.derivative() # 4x - 3
    #assert(str(p2) == "4*x**1+-3*x**0")
    assert(type(p2) == Polynomial)
    assert(p2.evalAt(2) == 5)
    assert(p2.evalAt(5) == 17)
    # Now test the + operator
    p3 = p1 + p2 # (2x**2 -3x + 5) + (4x - 3) == (2x**2 + x + 2)
    #assert(str(p3) == "2*x**2+1*x**1+2*x**0")
    assert(type(p3) == Polynomial)
    assert(p3.evalAt(2) == 12)
    assert(p3.evalAt(5) == 57)

def testPolynomialEq():
    assert(Polynomial([1,2,3]) == Polynomial([1,2,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,3,0]))
    assert(Polynomial([1,2,3]) != Polynomial([1,2,0,3]))
    assert(Polynomial([1,2,3]) != Polynomial([1,-2,3]))
    assert(Polynomial([1,2,3]) != 42)
    assert(Polynomial([1,2,3]) != "Wahoo!")
    # A polynomial of degree 0 has to equal the same non-Polynomial numeric!
    assert(Polynomial([42]) == 42)

def testPolynomialStr():
    assert(str(Polynomial([1,2,3])) == "x^2 + 2x + 3")
    assert(str(Polynomial([-1,-2,-3])) == "-x^2 - 2x - 3")
    assert(str(Polynomial([42])) == "42")
    assert(str(Polynomial([-42])) == "-42")
    assert(str(Polynomial([0])) == "0")
    assert(str(Polynomial([1,0,-3, 0, 1])) == "x^4 - 3x^2 + 1")
    assert(str(Polynomial([1,0,-3, 0, 1])) == "x^4 - 3x^2 + 1")
    assert(str(Polynomial([-1,0,3, 0, -1])) == "-x^4 + 3x^2 - 1")

def testPolynomialRepr():
    for coeffs in [ [1,2,3], [0], [-1,0,2,0,-3] ]:
        assert(eval(repr(Polynomial(coeffs))) == Polynomial(coeffs))

def testPolynomialConstructor():
    # If the list is empty, treat it the same as [0]
    assert(Polynomial([]) == Polynomial([0]))
    assert(Polynomial([]) != Polynomial([1]))
    # Remove leading 0's
    assert(Polynomial([0,0,0,1,2]) == Polynomial([1,2]))
    assert(Polynomial([0,0,0,1,2]).degree() == 1)
    # Require that the constructor be non-destructive
    coeffs = [0,0,0,1,2]
    assert(Polynomial(coeffs) == Polynomial([1,2]))
    assert(coeffs == [0,0,0,1,2])
    # Require that the constructor also accept tuples of coefficients
    coeffs = (0, 0, 0, 1, 2)
    assert(Polynomial(coeffs) == Polynomial([1,2]))
    # Allow for variable-length arguments.  That is, if the arguments
    # are not a list, then put them in a list
    assert(Polynomial(1,2,3) == Polynomial([1,2,3]))
    # And thus if no values are supplied, this is also the same as [0]:
    assert(Polynomial() == Polynomial([0]))

def testPolynomialInSets():
    s = set()
    #assert(Polynomial(1,2,3) not in s)
    s.add(Polynomial(1,2,3))
    #assert(Polynomial(1,2,3) in s)
    assert(Polynomial([1,2,3]) in s)
    assert(Polynomial(1,2) not in s)

def testPolynomialTimesOperator():
    # (x**2 + 2)(x**4 + 3x**2) == (x**6 + 5x**4 + 6x**2)
    assert(Polynomial([1,0,2]) * Polynomial([1,0,3,0,0]) ==
           Polynomial([1,0,5,0,6,0,0]))
    # (x**3 - 3x + 5) * 10 == (10x**3 - 30x + 50)
    assert(Polynomial(1,0,-3,5) * 10 == Polynomial(10,0,-30,50))
    # Hint: to do multiplication this way, you have to use __rmul__,
    # which should just call __mul__ (yes, really)
    print "time"
    assert(10 * Polynomial(1,0,-3,5) == Polynomial(10,0,-30,50))

def testPolynomialExponentiationOperator():
    assert(Polynomial(1,2,3)**0 == 1)
    assert(Polynomial(1,2,3)**1 == Polynomial(1,2,3))
    assert(Polynomial(1,2,3)**2 == Polynomial(1,2,3) * Polynomial(1,2,3))
    assert(Polynomial(1,2,3)**3 == Polynomial(1,2,3) * Polynomial(1,2,3) * Polynomial(1,2,3))

def testQuadraticClass():
    q1 = Quadratic(3,2,1)  # 3x^2 + 2x + 1
    assert(type(q1) == Quadratic)
    assert(q1.evalAt(10) == 321)
    assert(isinstance(q1, Quadratic) == isinstance(q1, Polynomial) == True)
    # the determinant is b**2 - 4ac
    assert(q1.determinant() == -8)
    # use the determinant to determine how many real roots (zeroes) exist
    assert(q1.numberOfRealRoots() == 0)
    print q1.getRealRoots()
    assert(q1.getRealRoots() == [ ])
    # Once again, with a double root
    q2 = Quadratic(1,-6,9)
    assert(q2.determinant() == 0)
    assert(q2.numberOfRealRoots() == 1)
    [root] = q2.getRealRoots()
    assert(almostEqual(root, 3))
    # And again with two roots
    q3 = Quadratic(1,1,-6)
    assert(q3.determinant() == 25)
    assert(q3.numberOfRealRoots() == 2)
    [root1, root2] = q3.getRealRoots() # smaller one first
    assert(almostEqual(root1, -3) and almostEqual(root2, 2))
    # Now, creating a non-quadratic "Quadratic" is an error
    ok = False # the exception turns this to True!
    try: q = Quadratic(1,2,3,4) # this is cubic, should fail!
    except: ok = True
    assert(ok)
    # one more time, with a line, which is sub-quadratic, so also fails
    ok = False
    try: q = Quadratic([2,3])
    except: ok = True
    assert(ok)
    # And make sure that these methods were defined in the Quadratic class
    # and not in the Polynomial class (we'll just check a couple of them...)
    assert('evalAt' in Polynomial.__dict__)
    assert('evalAt' not in Quadratic.__dict__)
    assert('determinant' in Quadratic.__dict__)
    assert('determinant' not in Polynomial.__dict__)
    
testPolynomialAndQuadraticClasses()

