"""
The program reads a string and makes each alternate
character into an upper case character and each other 
alternate character a lower case character.
Also make each alternative word lower and upper case.

have to output the following:
“Hello World” would become “HeLlO WoRlD”
“I am learning to code” would become “i AM learning
TO code”.

"""

#ask user to input a string and save on variable input_string 
input_string = input("please, write something: ")

#split the input string
split_string = input_string.split()

#variable initialization
new_string = ""
new_character = ""

i = 0

#for loop for each word of the string
for words in split_string:
    j = 0
    #get the word size
    word_size = len(words)
    #while loop as long j is smaller than the word size 
    while j < word_size:
      #upper case each character of the word
      if j % 2 == 0:  
        new_character += words[j].upper()
      else:
        #lower case each character of the word
        new_character += words[j].lower()
      j += 1
    new_character +=" "
print("".join(new_character))

#for loop for each word of the string
for words in split_string:
    #lower case each word of the string
    if i % 2 == 0:
        new_string += words.lower() + " "
    else:
        #uper case each word of the string
        new_string += words.upper() + " "
    i += 1

print("".join(new_string))
