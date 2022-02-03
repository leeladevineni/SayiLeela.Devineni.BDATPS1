#!/usr/bin/env python
# coding: utf-8

# # Question 6:
# You can turn a word into pig-Latin using the following two rules (simplified):
# • If the word starts with a consonant, move that letter to the end and append
# 'ay'. For example, 'happy' becomes 'appyhay' and 'pencil' becomes 'encilpay'.
# • If the word starts with a vowel, simply append 'way' to the end of the word.
# For example, 'enter' becomes 'enterway' and 'other' becomes 'otherway' . For
# our purposes, there are 5 vowels: a, e, i, o, u (so we count y as a consonant). Write a function pig() that takes a word (i.e., a string) as input and returns its pig- Latin form. Your function should still work if the input word contains upper case characters. Your output should always be lower case however.

# In[177]:


def pig(x): 
    if x[0] not in ['a','e','i','o','u','A','E','I','0','U']:
        y =x[1:]+x[0]+ "ay"
        print(y)
    else:
        print(x+"way")
pig("happy")
pig("Enter")


# # Question 7:
# File bloodtype1.txt records blood-types of patients (A, B, AB, O or OO) at a clinic. Write a function bldcount() that reads the file with name name and reports (i.e., prints) how many patients there are in each bloodtype.
# 
# 

# In[173]:


from collections import Counter
def bldcount(file_name): 
    with open('/Users/Leela/Downloads/' + str(file_name)  ,'r') as f:
        for row in f:
            bt_list = row.split()
    a = Counter(bt_list)
    for el in a:
        if a[el] == 1:
            print("There is 1 Patient of Blood Type " + str(el))
        else:
            print("There are " +  str(a[el]) +" Patients of Blood Type " + str(el))
bldcount("bloodtype1.txt")


# # Question 8:
# Write a function curconv() that takes as input:
# 1. a currency represented using a string (e.g., 'JPY' for the Japanese Yen or 'EUR' for the Euro)
# 2. an amount
# and then converts and returns the amount in US dollars.
# 

# In[174]:


def curconv(cur,val):
    dict1 = {}
    with open('/Users/Leela/Downloads/currencies.txt','r') as f:
        for row in f:
            dict1[row.split()[0]] = row.split()[1] 
    return float(dict1[cur]) * val
curconv('AUD',100)


# # Question 9:
# Each of the following will cause an exception (an error). Identify what type of exception each will cause.
# Trying to add incompatible variables, as in adding 6 + ‘a’
# Referring to the 12th item of a list that has only 10 items
# Using a value that is out of range for a function’s input, such as calling math.sqrt(-1.0)
# Using an undeclared variable, such as print(x) when x has not been defined
# Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory.

# In[160]:


try: 
    x = 6
    y = 'a'
    print (x+y) 
except TypeError: 
    print ("Trying to add incompatible variable.")
else: 
    print ("Success")
    
try:
    x =[1,2,3,4,5,6,7,8,9,10]
    print (x[11])
except IndexError:
    print ("Referring to the 12th item of a list that has only 10 items")
else:
    print ("Success")
try:
    x = math.sqrt(-1.0)
    print(x)
except ValueError: 
    print ("Using a value that is out of range for a function’s input.")
else: 
    print ("Success")
try:
    y = a
    print(x)
except NameError: 
    print ("Using an undeclared variable.")
else: 
    print ("Success")
    
try:
     open('/Users/Leela/Downloads/currencis.txt')
except FileNotFoundError: 
    print ("Trying to open a file that does not exist, such as mistyping the file name or looking in the wrong directory.")
else: 
    print ("Success")
    


# # Question 10:
# Assume that the string letters is already defined as 'abcdefghijklmnopqrstuvwxyz'. Write a function called frequencies() that takes a string as its only parameter, and returns a list of integers, showing the number of times each character appears in the text. Your function may ignore any characters that are not in letters.

# In[178]:


def frequencies(str1):
    dict = {}
    str2= str1.lower()
    for n in str2:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    array1 =['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    output_array =[]
    for z in array1:
        keys = dict.keys()
        if z in keys:
            output_array.append(dict[z])
        else:
            output_array.append(0)
    print(output_array)           
            
frequencies('apple.')
frequencies('The quick red fox got bored and went home.')


# In[ ]:




