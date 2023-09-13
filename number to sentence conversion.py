#program to write a given number into letters.
#for example, 125000 will be written as one hundred twenty five thousand.
number =input("enter a collection of numbers\n")
strinumb = str(number)
lizt = []
for i in strinumb:
    lizt+=i
numword = {"0":"","1":"one","2":"two","3":"three","4":"four","5":"five","6":"six",
           "7":"seven","8":"eight","9":"nine "}
copylizt = lizt
liztlen = len(copylizt)
inverslength = -len(copylizt)
inverslizt = []
while len(copylizt)>0:
    inverslizt +=copylizt[-1] 
    del copylizt[-1]

a = 1
b = 10
c = 100
d = 1000
e = 100000
d = 1000000

print(inverslizt)


