#this program is developed to calculate the factorial of any given number
# for instance, 4! means four factorial, which is calculated thus: 4*3*2*1 which results in 24
#
number = int(input("type a whole number:\n"))
#the above number shall be appended as the first element of a list sequence called series
series = []
series.append(number)
#the following uses the input to calculate its factorial
while number > 1:
    number = number-1
    series.append(number)
#at this point, the loop stops, after generating a list sequence of all numbers to be multiplied in the factorial
print(series)
#the above print command is only included here for us to see what our list sequence looks like after the loop stops iterating 
# we shall use the lenth of the list sequence in reverse and with a while loop, shall do the factorial.
#we shall use indexation to map out each element in the list sequence, while using the length of the sequence as a guide
serieslength = len(series)
indexx = -(serieslength-1)
factorial = 1
while indexx <= 0:
    factorial *= series[indexx]
    indexx += 1
#after we exit the loop, we print the final number calculated as factorial of the input number
print("the factorial of the number you typed is: ",factorial)
        












