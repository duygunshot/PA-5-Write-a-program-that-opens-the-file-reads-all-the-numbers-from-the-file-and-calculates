#Group7
#Dean Tran, Edwin Rodriguez, Elisa Shukuru
#04/03/2023
"""The purpose of the programming assignment is to write a program that opens the file, reads all the numbers from the file, and calculates"""

def numCount(lis):#Function to count the numbers
    count = 0
    for i in range(len(lis)):#Count the numbers loop
        count += 1

    return count

def minMax(lis):#Function to find the largest and smallest number
    min = lis[0]
    max = lis[0]
    for i in range(len(lis)):#Find the smallest number loop
        if lis[i] < min:
            min = lis[i]
    
    for i in range(len(lis)):#Find the largest number loop
        if lis[i] > max:
            max = lis[i]
    
    return max, min
    
def sum(lis):#Function to calculate the sum of all the numbers
    sum = 0
    
    for i in range(len(lis)):#Find the sum of numbers loop
        sum += lis[i]

    return sum

def avg(lis):#Function to calculate the average of all the numbers
    sum = 0
    count = 0

    for i in range(len(lis)):#Find the sum of numbers loop
        sum += lis[i]

    for i in range(len(lis)):#Count the numbers loop
        count += 1
    
    avg = sum / count#Calulate the average

    return avg

f = open("Random.txt", "rt")#Open the Random.txt file
num = 0
myList = []
for i in f:#Add all the numbers from the file to the list
    num = int(i)
    myList.append(num)
f.close()#Close the Random.txt file

f = open("PA5_Group7.txt", "at")#Create the output file
f.write(f"The number of numbers in the file: {numCount(myList)}\n")#Write the number of numbers to the output file
f.write(f"The largest and smallest number in the file: {minMax(myList)}\n")#Write the largest and smallest numbers to the output file
f.write(f"The sum of all numbers in the file: {sum(myList)}\n")#Write the sum of all the numbers to the output file
f.write(f"the average of all the numbers in the file: {avg(myList)}\n")#Write the average of all the numbers to the output file
f.close()#Close the output file

