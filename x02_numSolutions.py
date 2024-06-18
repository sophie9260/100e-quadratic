#!python3
"""
**** The Discriminant
The square root part is called the "discriminant".  
1. Depending on the coefficients, it is possible for it to have a negative value. Since you can't square root a negative, when the discrminant is less than 0, there are no solutions to the equation.
2. If the discriminant is 0, there is only 1 solution, because the quadratic is a perfect square
3. If the discriminant is positive, there will be 2 solutions
4. If the discriminant is a perfect square, then the roots will be rational numbers (fractions) and it is possible to solve the quadratic by factoring rather than having to rely on the quadratic formula
5. If the discriminant is not a perfect square, then the roots will be irrational numbers (involving roots) and the quadratic can not be factored.

Assignments:
##### x02. Determine the number of solutions
Determine the number of solutions. You will need to make use of the discriminant.  If you have already completed x01, you can import that function and make use of it in this assignment
"""
import x01_discriminant

def numSolutions(discriminant):
  if discriminant == 0:
    print("There will be one solution")
    return 1
  elif discriminant > 0:
    print("There will be two solutions")
    return 2
  elif discriminant < 0:
    print("There will be no solutions")
    return 0


def main():
  #Uncomment the lines that make use of your function definition
  #assert numSolutions(2,3,8) == 0
  assert numSolutions(-55) == 0
  
  #assert numSolutions(1,4,4) == 1
  assert numSolutions(0) == 1
  
  #assert numSolutions(1,-1,-6) == 2
  assert numSolutions(25) == 2

if __name__ == "__main__":
  main()
  
