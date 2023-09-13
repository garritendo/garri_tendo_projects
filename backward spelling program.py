#backward spelling program
#this program takes a word or phrase entered by a user and prints it backwards.
#input fuction to get word from user
wordinput = input("please type in any word or phrase:\n")
print("")
print()
#word from user considered as sequence
wordlenth = len(wordinput)
#use indexation. word lenth less by one to get index of last element in the sequence
endindex = wordlenth-1
#a new variable called backword will be used to receive each elements from the sequence called wordinput
backword = wordinput[endindex]
#the above will be done thru a while loop that picks elements from right to left thru augm assign operator
while endindex > 0:
    endindex -= 1
    backword += wordinput[endindex]
    #when that is done, exit loop, print sequence in new variable and print sequence from user side by side
print("the word/phrase you entered is:", wordinput,
      "\nand what you typed has been spelt backwords as:", backword)
input("\n\npress enter to exit program")