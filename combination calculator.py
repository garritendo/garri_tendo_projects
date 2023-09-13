# a program to calculate the combinations
#   n COMBINATION r or better put:  nCr. 10C3 will mean 10!/(3!(10-3)!)
#we shall need three factorial calculations as per the formular above
print("to calculate say n combination r, u shall enter the n number and r numbers.")
number1 = int(input("type the n number:\n"))
copynum1 = str(number1)
print('''      COMBINATION''')
number2 = int(input("type the r number:      "))
copynum2 = str(number2)
number3 = number1 - number2
#we shall calculate factorials for number1 number2 and number 3
#below is code to calculate just number1. we shall then replicate process to calculate number3 and number2
#the above number1 shall be appended as the first element of a list sequence called series
series = []
series.append(number1)
#the following uses the input to calculate its factorial
while number1 > 1:
    number1 = number1-1
    series.append(number1)
#at this point, the loop stops, after generating a list sequence of all numbers to be multiplied in the factorial
# we shall use the lenth of the list sequence in reverse and with a while loop, shall do the factorial.
#we shall use indexation to map out each element in the list sequence, while using the length of the sequence as a guide
serieslength = len(series)
indexx = -(serieslength-1)
factorial = 1
while indexx <= 0:
    factorial *= series[indexx]
    indexx += 1
#after we exit the loop
#below is code to calculate factorial for number3
series3 = []
series3.append(number3)
#the following uses the input to calculate its factorial
while number3 > 1:
    number3 = number3-1
    series3.append(number3)
#at this point, the loop stops, after generating a list sequence of all numbers to be multiplied in the factorial
# we shall use the lenth of the list sequence in reverse and with a while loop, shall do the factorial.
#we shall use indexation to map out each element in the list sequence, while using the length of the sequence as a guide
serie3length = len(series3)
indexx3 = -(serie3length-1)
factorial3 = 1
while indexx3 <= 0:
    factorial3 *= series3[indexx3]
    indexx3 += 1
#after we exit the loop, 
#below is code to calculate factorial for number2
series2 = []
series2.append(number2)
#the following uses the input to calculate its factorial
while number2 > 1:
    number2 = number2-1
    series2.append(number2)
#at this point, the loop stops, after generating a list sequence of all numbers to be multiplied in the factorial
# we shall use the lenth of the list sequence in reverse and with a while loop, shall do the factorial.
#we shall use indexation to map out each element in the list sequence, while using the length of the sequence as a guide
serie2length = len(series2)
indexx2 = -(serie2length-1)
factorial2 = 1
while indexx2 <= 0:
    factorial2 *= series2[indexx2]
    indexx2 += 1
#after we exit the loop,
#below is code to calculate the n combination of m, the two numbers entered above
calccombination = factorial/(factorial2*factorial3)
print(copynum1,"  COMBINATION  ",copynum2,"  is:   ",calccombination)  