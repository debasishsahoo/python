## volume.py  volume calculations with torus
# Author:
# Date:
# There are libraries of common functions, for example a math library
# that has functions such as sine, cosine, logs, etc.
# There ARE syntax and semantic errors in this program as given!
from math import pi   # use the value of pi defined in the math library
def main():
      radius = eval(input("Enter the radius: "))
      height = eval(input("Enter the height: "))
      conevol = 1/3*pi*radius*2*height   # cone volume
      cylvol = pi*radius**2*height        # cylinder volume
      spherevol = 3/4*Pi*r**3        # sphere volume
      print ('The volume of a cone: ',conevol)
      print ("The volume of a cylinder: ",cylvol)
      print ("The volume of a sphere: ",spherevol)

main()
