import sys
import itertools

def main():
    isTriangle = False
    Case = 0
    list = [0,1,2,100,199,200,201], [0,1,2,100,199,200,201], [0,1,2,100,199,200,201]
    print("| Case | a    | b    | c    |  Expected Output |")
    for values in itertools.product(*list):
       if (values[0] + values[1] > values[2]) and (values[1] + values[2] > values[0]) and (values[0] + values[2] > values[1]):
           isTriangle = True
       else:
           isTriangle = False
       Case += 1
    
       if(isTriangle and Case % 27 == 0):
           if (values[0] == values [1]) and (values[1] == values[2]):
               print("| ",Case,"  | ",values[0],"  | ", values[1],"  | ",values[2],"   |  Equilateral |")
           elif (values[0] == values[1] and values[0] != values[2]) or (values[0] == values[2] and values[0] != values[1]) or (values[1] == values[2] and values[1] != values[0]):
               print("| ",Case,"  | ",values[0],"  | ", values[1],"  | ",values[2],"   |  Isosceles |")
           elif (values[0] != values[1] and values[0] != values[2] and values[1] != values[2]):
               print("| ",Case,"  | ",values[0],"  | ", values[1],"  | ",values[2],"   |  Scalene |")
       elif(Case % 27 == 0):
           print("| ",Case,"  | ",values[0],"  | ", values[1],"  | ",values[2],"   |  Not a Triangle |")




if __name__ == "__main__":
    main()