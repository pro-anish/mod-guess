from itertools import combinations
import sys
import math

#print('YOU CAN MAKE YOUR OWN NUMBER GUESSING GAME!!')

#
# - - - - - INITIAL INFORMATIONS - - - - - 
#

print('YOU NEED TO ENTER THE NUMBER UPTO WHICH YOU WANT THE PROGRAM TO MAKE THE GAME FOR YOU')

for i in range(3):
    # CHECKING IF THE INPUT IS CORRECT
    try:
        q = int(input('ENTER YOUR NUMBER : '))
        break
    except:
        print('OOPS,IT SEEMS THAT YOU HAVE NOT RESPONDED CORRECTLY!')
        if i == 2:
            print("RETRY!!!")
            sys.exit()

input("PRESS ENTER TO START THE GAME!!")
print('---------------------------------------------------------')
print('GUESSING GAME')
print('STEP 1: THINK A NUMBER BETWEEN 1 AND',q)
input("Press Enter to continue...")
print('YOU WILL BE GETTING A NUMBER OF TABLES CONSISTING OF NUMBERS')
print('STEP 2: ENTER 1 FOR YES AND 0 FOR NO')
#
# - - - - - END OF INITIAL INFORMATIONS - - - - -
#

# DECLARING VARIABLES
dict_of_numbers = {}
no_of_tables = 0
comb = []

# GENERATING REQUIRED 1ST ELEMENT NUMBER FOR THE TABLES
for i in range(1,q):
    comb = list(combinations([2**_ for _ in range(i)], i))
    no_of_tables = i 
    dict_of_numbers["B{0}".format(i-1)] = [2**(i-1)]
    if 2**(i) > q:
        break

for _ in range(1, no_of_tables+1):
    comb1 = list(combinations(comb[0], _))
    for j in comb1:
        for k in j:
            for l in range(no_of_tables):
                if k in dict_of_numbers["B{0}".format(l)]:
                    if not (sum(list(j))>q):
                        dict_of_numbers["B{0}".format(l)].append(sum(list(j)))
                dict_of_numbers["B{0}".format(l)] = list(set(dict_of_numbers["B{0}".format(l)]))

#
# - - - - Printing the Tables - - - -
#

def nearest_square(no):
    return (math.ceil(no**0.5))**2

def fillup(the_list, upto):
    temp = ['~']*(upto - len(the_list))
    the_list += temp
    return the_list

def make_table(_list):
    n = nearest_square(len(_list))
    l = int(n**0.5)
    max_wd = len(str(max(_list)))
    
    if len(_list)<n:
        _list = fillup(_list, n)
   
    i = 0
    out_string = ""
    while i<len(_list):
        if i%l == 0:
            # print()
            # print("+"+"="*(max_wd+3)*l+"+")
            # print("|", end = "")
            out_string += "\n+" + "="*(max_wd+3)*l+"+" + "\n|"
        
        out_string += " {0:^{1}} |".format(_list[i], max_wd)       
        i+=1
    else:
        # print()
        # print("+"+"="*(max_wd+3)*l+"+")
        out_string += "\n" + "+"+"="*(max_wd+3)*l+"+"
    
    return out_string

#
# - - - - - End of Printing Tables - - - - -
#

# make_table([100,2,3,10,2,2000,1,2,1])
# make_table(dict_of_numbers['B0'])
# fillup([1,2,3], 3)

#
# - - - - - MAIN BODY OF PROGRAM - - - -
#

ans = 0
choice = 0
flag = 0

for k in range(no_of_tables):
    print(make_table(dict_of_numbers["B{0}".format(k)]) + "\nIS YOUR NUMBER HERE ?")
     
    for _ in range(3):
        choice = input("(1 for YES, 0 for NO) : ")
        
        # CHECKING IF THE INPUT IS CORRECT
        if choice == "1":
            ans += 2**k
            flag = 0
            break
        elif choice == "0":
            flag = 0
            break
        else:
            flag = 1
            print("PLEASE ENTER 1 FOR YES AND 0 FOR NO")
    
    if flag == 1: # FOR WRONG INPUT
        print('OOPS,IT SEEMS THAT YOU HAVE NOT RESPONDED CORRECTLY!')
        print("RETRY!!!")
        sys.exit()

# PRINTING RESULTS
if ans > q or  (q == 0 and ans == 0):
    print('\nOOPS,IT SEEMS THAT YOU HAVE NOT RESPONDED CORRECTLY!')
else:
    print('\nYOUR NUMBER IS',ans)
print('---------------------------------------------------------') 
