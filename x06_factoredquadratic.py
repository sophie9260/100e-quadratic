#!python3
'''
This is a challenging problem!

x06. Determine the factored form
You may use the functions you created in previous assignments
'''
import x05_roots
import x01_discriminant

def Factored(a,b,c):
  answer = []
  discriminant = (b**2)-(4*a*c)

  if discriminant < 0:
    return None

  elif discriminant == 0:
    d = (discriminant**0.5)
    a1 = ((-b)+d)/2*a
    a1 = int(a1)
    if a1 > 0:
      answer.append(f"(x - {a1})")

    if a1 < 0:
      A = a1*(-1)
      answer.append(f"(x + {A})")


  elif discriminant > 0:
    d = (discriminant**0.5)
    a1 = ((-b)+d)/2*a
    a2 = ((-b)-d)/2*a
    print(a1, a2)
    a1 = int(a1)
    a2 = int(a2)
    if a1 > 0:
      answer.append(f"(x - {a1})")
    if a1 < 0:
      A = a1*(-1)
      answer.append(f"(x + {A})")
    if a2 > 0:
      answer.append(f"(x - {a2})")
    if a2 < 0:
      A2 = a2*(-1)
      answer.append(f"(x + {A2})")
    print(answer)
    return answer

def main():
  assert ("(x + 3)" in Factored(1,1,-6)) == True
  assert ("(x - 2)" in Factored(1,1,-6)) == True
  assert ("(x + 2)" in Factored(1,7,10)) == True
  assert ("(2x + 1)" in Factored(2,5,2)) == True
  assert ("(x + 2)" in Factored(2,5,2)) == True
  assert ("(3x + 1)" in Factored(6,-7,-3)) == True
  assert (Factored(1,4,7)) == None
  assert (Factored(2,4,4)) == None
  
if __name__ == "__main__":
  main()
  
