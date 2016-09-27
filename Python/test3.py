import sys
import itertools

def main():
    #           Month       Day             Year
    date = [1,2,6,11,12], [1,2,15,30,31], [1812,1813,1912,2011,2012]
    Case = 0
    print("| Case | a    | b    | c    |  Expected Output |")
    for values in itertools.product(*date):
        Case += 1
        if (Case % 12 == 0) and (values[0] == 1 or values[0] == 3 or values[0] == 5 or values[0] == 7 or values[0] == 8 or values[0] == 10):
            if values[1] < 31:  #increase day by one
                print("| ", Case, "  | ", values[0], "  | ", values[1], "  | ", values[2], "   | ", values[0], ", ", values[1]+1, ",",values[2], " |")
            else:
                print("| ", Case, "  | ", values[0], "  | ", values[1], "  | ", values[2], "   | ", values[0]+1, ", 1", ",",values[2], " |")
        if (Case % 12 == 0) and (values[0] == 4 or values[0] == 6 or values[0] == 9 or values[0] == 11):
            if values[1] < 30:
                print("| ", Case, "  | ", values[0], "  | ", values[1], "  | ", values[2], "   | ", values[0], ", ", values[1]+1, ",", values[2], " |")
            else:
                print("| ", Case, "  | ", values[0], "  | ", values[1], "  | ", values[2], "   | ", values[0] + 1,", 1", ",", values[2], " |")
        if (Case % 12 == 0) and (values[0] == 2):
            if (values[2]%400 == 0 or values[2]%100 != 0) and (values[2]%4 == 0) and (values[1] == 28):
                print("| ", Case, "  | ", values[0], "  | ", values[1], "  | ", values[2], "   | 2, 29,",values[2], "|")
            elif (values[2]%400 != 0) and (values[2]%4 != 0) and (values[1] == 28):
                print("| ", Case, "  | ", values[0], "  | ", values[1], "  | ", values[2],"   | 3, 1,",values[2], "|")
            elif (values[1] > 29):
                print("| ", Case, "  | ", values[0], "  | ", values[1], "  | ", values[2], "   | Invalid Input Date |")
            elif (values[1] < 28):
                print("| ", Case, "  | ", values[0], "  | ", values[1], "  | ", values[2], "   | ", values[0], ", ",values[1] + 1, ",", values[2], " |")
        if (Case % 12 == 0) and (values[0] == 12):
            if (values[1] < 31):
                print("| ", Case, "  | ", values[0], "  | ", values[1], "  | ", values[2], "   | ", values[0], ", ",values[1] + 1, ",", values[2], " |")
            elif (values[2] != 2012):
                print("| ", Case, "  | ", values[0], "  | ", values[1], "  | ", values[2], "   |  1", ", 1, " , values[2]+1, " |")
            elif (values[2] == 2012):
                print("| ", Case, "  | ", values[0], "  | ", values[1], "  | ", values[2], "   | Invalid Input Date |")




if __name__ == "__main__":
    main()

'''
C:\Users\mahyar\AppData\Local\Programs\Python\Python35-32\python.exe "C:/Users/mahyar/Desktop/software test2/test3.py"
| Case | a    | b    | c    |  Expected Output |
|  12   |  1   |  15   |  1813    |  1 ,  16 , 1813  |
|  24   |  1   |  31   |  2011    |  2 , 1 , 2011  |
|  36   |  2   |  15   |  1812    |  2 ,  16 , 1812  |
|  48   |  2   |  31   |  1912    | Invalid Input Date |
|  60   |  6   |  2   |  2012    |  6 ,  3 , 2012  |
|  72   |  6   |  31   |  1813    |  7 , 1 , 1813  |
|  84   |  11   |  2   |  2011    |  11 ,  3 , 2011  |
|  96   |  11   |  31   |  1812    |  12 , 1 , 1812  |
|  108   |  12   |  2   |  1912    |  12 ,  3 , 1912  |
|  120   |  12   |  30   |  2012    |  12 ,  31 , 2012  |

Process finished with exit code 0
'''