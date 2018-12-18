question_1.py: it observes that r1 and r2 should be additive inverse of each other in modn. then the program proceeds to find p by finding the gcd of n and |a-b| (r1 and r3).it finds the other prime by dividing n by p.

question_2.py: this program finds elements of Z*n and Q*n and their corresponding generators.findZElts() and findZGens() take a number and output the elements and generators of Z*n correspondingly. similarly findQElts() and findQGens() take a number and output the elements and generators of Q*n ,correspondingly.


question_3.py: this program finds m (c^d modn) firstly by finding the inverse of e.then it finds the result by CRT and outputs the average time taken by each method.

question_4.py: given an equation with constants a,b and n. findroots() function calculates the roots of the equation. if there is no solution, it outputs 'there is no solution'. for the purpose of solving question4, findroots() is called by the given inputs.

question_5.py: lfsr() function takes seed and taps. seed is the string version of the initial state. taps are the powers of x in the polynomial. lfsr() outputs the states and the xor bits, one by one.