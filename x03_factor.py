#!python3

'''
**** The Discriminant
The square root part is called the "discriminant".  
1. Depending on the coefficients, it is possible for it to have a negative value. Since you can't square root a negative, when the discrminant is 0, there are no solutions to the equation.
2. If the discriminant is 0, there is only 1 solution, because the quadratic is a perfect square
3. If the discriminant is positive, there will be 2 solutions
4. If the discriminant is a perfect square, then the roots will be rational numbers (fractions) and it is possible to solve the quadratic by factoring rather than having to rely on the quadratic formula
5. If the discriminant is not a perfect square, then the roots will be irrational numbers (involving roots) and the quadratic can not be factored.

Assignments:
##### x03. Determine if the quadratic can be factored
'''
import x01_discriminant

def factorable(discriminant):
  if discriminant >= 0:
    D = discriminant**0.5
    DD = round(D)
  else:
    return False

  if D == DD:
    return True
  else:
    return False
  

def main():
  #uncomment the lines that match your assignment
  #assert factorable(1,4,4) == True
  assert factorable(0) == True
  
  #assert factorable(1,-1,-6) == True
  assert factorable(25) == True
  
  #assert factorable(2,3,8) == False
  assert factorable(-55) == False
  
  #assert factorable(1,3,7) == False
  assert factorable(5) == False
  
if __name__ == "__main__":
  main()
