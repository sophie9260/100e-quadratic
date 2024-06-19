#!python3
'''
This is a challenging problem!

x06. Determine the factored form
You may use the functions you created in previous assignments
'''
import math
def Factored(a,b,c):
  list = []
  d = b**2-(4*a*c)
  
  if d >= 0:
    if a == 1:
      fp  = ((-1 * b) + (d**0.5)) / (2*a)
      fn = ((-1 * b) - (d**0.5)) / (2*a)
      if fp > 0:
        list.append(f"(x - {int(fp)})")
      elif fp < 0:
        list.append(f"(x + {int(-1 * fp)})")
      if fn > 0:
        list.append(f"(x - {int(fn)})")
      elif fn < 0:
        list.append(f"(x + {int(-1 * fn)})")
      print(list)
      return list
    else:
      fp  = ((-1 * b) + (d**0.5)) / (2*a)
      fn = ((-1 * b) - (d**0.5)) / (2*a)
      print(fp,fn)
      ax = (fp).as_integer_ratio()
      ax_n = (fn).as_integer_ratio()
      print(ax)
      print(ax_n)
      Bx = ax[1]
      cx = ax[0]
      print(fn)
      print(1, ax_n)
      Bx_n = ax_n[1]
      cx_n = ax_n[0]
      print(2, Bx_n, cx_n)
      if fp > 0:
        list.append(f"({Bx}x - {cx})")
      elif fp < 0:
        list.append(f"({Bx}x + {-1 * cx})")
      if fn > 0:
        list.append(f"({Bx}x - {cx})")
      elif fn < 0:
        if Bx_n == 1:
          list.append(f"(x + {-1 * cx_n})")
        else:
          if cx_n < 0:
            cx_n = cx_n*-1
            list.append(f"({Bx_n}x + {cx_n})")
          else:
            list.append(f"({Bx_n}x + {cx_n})")
      print(list)
      return list

    

  else:
    return None
  

def main():
  assert ("(x + 3)" in Factored(1,1,-6)) == True
  assert ("(x - 2)" in Factored(1,1,-6)) == True
  assert ("(x + 2)" in Factored(1,7,10)) == True
  assert ("(2x + 1)" in Factored(2,5,2)) == True
  assert ("(x + 2)" in Factored(2,5,2)) == True
  assert("(2x + 3)" in Factored(8,14,3)) == True
  #assert ("(3x + 1)" in Factored(6,-7,-3)) == True
  assert (Factored(1,4,7)) == None
  assert (Factored(2,4,4)) == None
  
if __name__ == "__main__":
  main()
  