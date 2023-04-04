#code to print first letter of every word of a sentence
line= input("enter a sentence: ")
t = line.split()
for first in t:
    print(first[0])    
