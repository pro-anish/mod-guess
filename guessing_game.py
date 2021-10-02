#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 00:17:55 2021

@author: anish
"""


from itertools import combinations
from tabulate import tabulate

print('YOU CAN MAKE YOUR OWN NUMBER GUESSING GAME!!')
print('YOU NEED TO ENTER THE NUMBER UPTO WHICH YOU WANT THE PROGRAM TO MAKE THE GAME FOR YOU')
q=int(input('ENTER YOUR NUMBER '))
input("PRESS ENTER TO START THE GAME!!\n")
print('---------------------------------------------------------')
print('GUESSING GAME--1 to ',q)
print('STEP1: THINK A NUMBER BETWEEN 1 AND',q)
input("Press Enter to continue...")
print('YOU WILL BE GETTING A NUMBER OF TABLES CONSISTING OF NUMBERS\n')
print('STEP 2: ENTER 1 FOR YES AND 0 FOR NO')


a=0
b=0
i=1
while True :   
  r=0
  for j in range(1,i+1):
    comb = list(combinations([2**j for j in range(0,i)], j))      #initialising the no. of tables required for the game
    #print(comb)
    r=r+len(comb)
    #print(len(comb))
    #print(r)
    no=j  
  if r>q:
    break
  i+=1
#print(r)         #max number possible according to the given number
#print(no)       #no of tables required
  
  
  
for i in range(1,no+1):
  globals()['b%s'%i]= [2**(i-1)]
  #print(globals()['b%s'%i])            #making new lists with 2**n as the first number i.e E11 element of the every table
  
  
print(b4) 
  
  


for i in range(1,no+1):
  comb = list(combinations([2**j for j in range(0,no)], i))
  for j in comb:
    #print (j,sum(j))           #will show the possible combinations and their sum(unique)
    h= list(j)
    #print(h,sum(h))
    for k in h:     #[1, 4, 8] 13
      for l in range(1,no+1):
        if k in globals()['b%s' % l]:
          globals()['b%s' % l].append(sum(h))       #appends the numbers to the desired lists


#print(list(b4))           #will show the list(b4) of first table





def newlist(x):
    while len(x)%float((len(x)**0.5))!=0:
        x.append('~')
    tablise(x)
    
    

def tablise(x):
  trial_tab_list=[]

  for i in range(0,len(x),int(len(x)**0.5)):
      trial_tab_list.append(x[i:i+int((len(x)**0.5))])
 
  print(tabulate(trial_tab_list,tablefmt="fancy_grid"))




for i in range(1,no+1):
  #print(globals()['b%s'%i])
  no_repeats_list= list(set(globals()['b%s'%i]))
  reduced_list=[]
  for j in no_repeats_list:         #adding numbers within the given input range
    if j<=q:
      reduced_list.append(j)        
  newlist(reduced_list)
  
  globals()['response%s' % i]= int(input('IS YOUR NUMBER HERE?'))
  

table_dictionary={}
for i in range(0,no+1):  
   table_dictionary["table%s" %(i+1)] = 2**(i)  
#print(table_dictionary)

ans=0

for j in range(1,no+1):
  if globals()['response%s'%j]==1:
    ans=ans+ table_dictionary['table%s'%j]
if ans>q:
  print('OOPS,IT SEEMS THAT YOU HAVE NOT RESPONDED CORRECTLY!')
else:
  print('\nYOUR NUMBER IS',ans)
print('---------------------------------------------------------') 

































