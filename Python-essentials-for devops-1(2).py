#######################################################################Chapter 01######################################################################


####Nested loop 

car = "cadillac"

if "m" in car:
    print("I found an m in your car name")
    if car == "mercedes":
         print("Oh nice it's a mercedes")
    elif car == "mazda":
             print("Mazda really?")
    elif car == "maybach":
             print("fancy maybach")
elif "c" in car:
        print("I found a c in your car")
        if car == "citeron":
             print("a french citeron")
else:
        print("No car like that exists here")
     
#Continue statement skips a step in the loop

for i in range(10):
    if i == 5: 
        continue #THis step has been skipped
    print(i)


###While loops

count = 2 #2 is where it starts
while count < 6:
    print(f"The count is {count}")
    count += 1 # now 2+1=3 will be fed back into the statement until count =5 
    #because that's less than 6


#example 1

i = 2
while i < 10:
 print(i)
 i += 2


#example 2
i = 1
while i < 6:
 print(i)
 i += 1
else:
 print("i is no longer less than 6")





## How to make a while loop end

count = 100
while True:
    print(f"count is less than 200, it's actually {count}")
    if count > 150: #As soon as count is 6 it'll break and still output the greater number
        break
    count += 10 


### Handling exceptions

cars_finished = ["mercedes", "bmw", "ferrari"]

while True:
     try:
        car = cars_finished.pop()
        print(car)
     except IndexError as b:
        print("we tried to pop too many cars")
        print(b)
        break



#Object methods and attributes - Define a fancy motorbike - Example1


class fancy_motorbike():
     #Variable for class
    wheels = 4
    def motorbike_1(self):
       print("You have called motorbike1")

motorbike = fancy_motorbike()

how_many_wheels = motorbike.wheels

print(how_many_wheels)

which_motorbike = motorbike.motorbike_1() #No need to print as it gets called 


#Object methods and attributes - Football team - Example2
#Our football team defined a method called wingers_in_team. 
#When you instantiate an instance of football team called man_utd
#..you can access the attribute and invoke the method using the dot syntax

class football_team():
     #variable for class
    players = 11
    def wingers_in_team(self):
       print("you've tried to return the number of wingers in the team")

man_utd = football_team()
man_utd_wingers = man_utd.players   #Don't use brackets when trying to call a variable  

man_utd.positiontype = man_utd.wingers_in_team()
                        #As we have self here. the print gets executed.


#Sequence

5 in [1,2,4,5]

whats_my_name = "snoopdoog"

whats_my_name[0] # This will print the first letter in whats_my_name
whats_my_name[-1] # This prints the last letter in whats_my_name
whats_my_name.index("o") #This will tell you the position of o
whats_my_name.index("g",4,10)  #Finds g between position 4 and 10


#Slicing

my_sequence = ["a","b","c","d","a"]
my_sequence[2:3]
len(my_sequence) # 4 values in the list :D
min(my_sequence) # smallest member
my_sequence.count("a") # how many a's are there

#List()
list()

list(range(10)) #0-9
list("Sohail Khan")

nine = [0,1,2,3,4,5,6,7]
empty = []
mixed = [0,"a",empty]












###Append list

cars = ["mercedes","vw","ferrari","lamborghini"]
cars.append("citeron")
cars
#Insert
cars = ["mercedes","vw","ferrari","lamborghini"]
cars.insert(1,"audi") #replace vw with audi
cars

#Extend
more_cars = ["jeep","mini","toyota","suzuki"]
cars.extend(more_cars) #let's add the new list to the current list
cars

#pop- remove last item from a list and return it
cars = ["mercedes","vw","ferrari","lamborghini"]
cars.pop() #returns suzuki because we've extended the list
cars.pop(0) #removes first item from the list and returns its value

#remove

cars.remove("vw") #removes vw from the list
cars

# for loop with append
cube = [] # now we need to fill this 
for i in range(3,18,3):
    icubed = i*i*i
    cube.append(icubed)
    if i%3==0:
        print("I is divisible by 3")
        if i != 3: # first condition has to be satisfied for this to work.
          print("I is not 3")
        if i ==3 :
          print("I is 3")
cube

# we can also replace this with a list comprehension.
cube = [i*i*i for i in range(3,18,3) if i%2==0] #return i if it's divisible by two
cube


#For loop with if statements (break and continue)

people = ["Joseph","Alma","Siamak"]
for x in people:
 if x == "Siamak":
  break
 print(x)

people = ["Joseph","Alma","Siamak"]
for x in people:
 if x == " Siamak":
  continue
 print(x)


people = ["Joseph","Alma","Siamak"]
for x in people:
 if x == " Siamak":
  break
 print(x)


#For loop to print some numbers and text
for x in range(10):
    print("the current value in the range is", x)



for x in range(10):
    print(x,end = ",") 



for x in range(4,100,2):
    print(x)


for x in range(4,100,2):
    if x >= 40 and x <=50:
        continue
    print(x,end = ",")


for x in range(4,100,2):
    if x >= 40 and x <=50:
        break
    print(x) 



for x in range(4,100,2):
    if x >= 40 and x <=50:
        if x == 45:
            print("we have found",x)
        continue
    elif x >=80:
       break
    else:
     print(x)


for x in range(10):
 if x == 3:
     break
 print(x)
 else:
  print("Finished counting!")





###########Strings################

str()
"hello my name is sohail"




my_list = list() #this returns brackets
str(my_list) # let's turn the bracks into a string


car_info = """
Hi mannnnnnnnn

"""




print(car_info)


car_info.lstrip()


"Ferrari".startswith("F") 



"%s + %s = %s" % (5,3,"Eight")



"{} was 2 seconds faster than the {}".format("ferrari","mercedes")

"{4} was 2 seconds faster than the {3} but obviously {2} came first".format("ferrari","mercedes","lamborghini","vw","Nissan")

"""{japan_car} was 2 seconds 
faster than the {german_car}""".format(japan_car="Nissan", german_car="vw")


##dict in strings##

values = {'footballer':'cr7','team': 'al Nassr'}
"the top goal scorer in the saudi league is {footballer}".format(**values)

##format string. here we don't need the .format part :) ##########

a = 50
b = 40
f" so let's add {a} and {b} together. {a+b}"




padding=10
count = 50
f"0{count:20d}"

from string import Template
hello = Template("$name how are you")
hello.substitute(name = "sohail")



############Dicts###########################

shake=dict()
type(shake)



protein_shake_list = [["shake1","Grenade"],["shake2","Huel"]]
dict(protein_shake_list)
type(protein_shake_list)


protein_shake_dict = {'shake1': 'Grenade', 'shake2': 'Huel'}
print(protein_shake_dict)

protein_shake_dict['shake2'] #Hmm let's find out what shake2 is 

protein_shake_dict["shake3"] = "my Protein" #Let's add another shake to the list

protein_shake_dict["shake1"] = "Fuel 20k" #Let's replace Grenade with Fuel 20k



if "shake5" in protein_shake_dict :
     print (protein_shake_dict["shake5"])
else:
     print("not found")    



del(protein_shake_dict["shake1"])
print(protein_shake_dict)


protein_shake_dict.keys()
protein_shake_dict.values()

for key,value in protein_shake_dict.items():
     print(f"{key}:Tasty and nutritious {value}") #F-strings joined the party in Python 3.6 with PEP 498. Also called formatted string literals, f-strings are string literals that have an f before the opening quotation mark. They can include Python expressions enclosed in curly braces. Python will replace those expressions with their resulting values. So, this behavior turns f-strings into a string interpolation tool.

#dict comprehensions

word = "coffee"

cap_each_word = {x: x.upper() for x in word}
cap_each_word


################Functions in python###################################



#Let's see your weekly takeways
def weekly_takeaway(first_meal,second_meal):
    """This is what you're  eating."""
    print(f"You had {first_meal} on a monday")
    print(f"you had {second_meal} on a saturday")

weekly_takeaway("subway","pizza")


def types_of_protein_shakes(huel=3, grenade=1):
     """default values assigned"""
     print(f"huelllsss:{huel}")
     print(f"grenadessss:{grenade}")

types_of_protein_shakes(0)



#Functions are objects and can be passed around:

def triple(input):
     """let's triped your input"""
     return input*3

def quadruple(input):
     """Let's quadruple your input"""
     return input*4

calculations = [triple,quadruple] #This is a list of functions so we use square brackets
for calculation in calculations:
     print(calculation(3))       


#Anonymous functions

item = [[6,"a",5],["f",5,"t"]]
sorted(item)

##lambda function

def my_map(my_func,my_iter):
     result = [] #this needs to get populated so we'll call it at the end
     for item in my_iter:
          new_item = my_func(item)
          result.append(new_item)
     return(result)

items = [4,3,2,4,5,2]
cubed = my_map(lambda x:x**2, items)
print(cubed)     

##using regular expressions

cc_list = '''sk9212k@gmail.com linkedin,
sk9212k@gmail.com kodekloud.'''

'kode' in cc_list #is code in cc_list?

import re
re.search(r'kode',cc_list)


##Character classes

cc_list = '''sk9212k@gmail.com linkedin,
sk9212k@gmail.com kodekloud.'''

re.search(r'\w+\@\.\w+',cc_list)    #w+ same as [a-zA-Z0-9_] \d


##Groups page 79

cc_list = '''sk9212k@gmail.com linkedin,
sk9212k@gmail.com kodekloud.'''

re.search(r'(\w+)\@\.(\w+)',cc_list) #brackets are needed here
matched = re.search(r'(\w+)\@\.(\w+)',cc_list)
matched.group(0) #full match so sk9212k@gmail.com because in re.search we're looking for the email address. 
matched.group(1) #gets the match before the @ sign. so sk9212k


#Named groups

cc_list = '''sk9212k@gmail.com linkedin,
sk9212k@gmail.com kodekloud.'''

matched = re.search(r'(?P<name-before-at>\w+)\@\.(\w+)',cc_list) #brackets are needed here and ?P<name-before-at>
matched.group('name-before-at')  
matched.group(1) #gets the match before the @ sign. so sk9212k

print(f'''name:{matched.group("name-before-at")}''')

##find all page 81 - dot_com_or_dot_uk is not defined?

import re
cc_list = '''sk9212k@gmail.co.uk linkedin,
sk9212k@gmail.com kodekloud.'''

matched = re.findall(r'(\w+)\@(\w+)\.(\w+)', cc_list)

dot_com_or_dot_uk = [x[2] for x in matched] #Let's see if the email address if .com or .co.uk
dot_com_or_dot_uk 


#Find Iterator. Let's deal with each match individually.

import re
cc_list = '''sk9212k@gmail.com linkedin,
sk9212k@gmail.com kodekloud.'''

matched = re.finditer(r'\w+\@\w+\.\w+',cc_list)
matched #this will find the first match as opposed to printing them all out



#We can use the iterator object, matched, can be used in for loop:
import re
cc_list = '''sk9212k@gmail.com linkedin,
solutions@gmail.com kodekloud.'''


matched = re.finditer("(?P<hello>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)",cc_list)

for m in matched:
     print(m.groupdict())


#Substitution. We can use regexes to substitute part or all of a string.

import re

re.sub(r("\d," ,"#", "The passcode you entered was 0003456")) #\d means 0-9, so let's replace that with #


###Lazy evaluation - Generators - in chunkz

def counting():
     n = 2
     while True:
          n += 2 #provides a convenient way to add a value to an existing variable and assign the new value back to the same variable.
          yield n

lets_count = counting()
lets_count
next(lets_count) #yield n will now store 4
next(lets_count) #yield n will now store 6
next(lets_count) #yield n will now store 8


#Tracking state in Fibonacci generator

def fib():
     first = 10
     Last = 2
     while True:
       first, Last = Last, + first + Last
       yield first_#Hmm not working

hello_fib = fib()

next(hello_fib)


f = fib()
for x in f:
     print(x) #This will print the "yield first"
     if x > 15:
          break


#Generator comprehensions to create one line generators

list_o_nums = [x for x in range(100)]
gen_o_nums = (x for x in range(100))    

list_o_nums
gen_o_nums

import sys
sys.getsizeof(list_o_nums)
sys.getsizeof(gen_o_nums) # This uses less memory

##### Using IPython to run Unish Shell commands  87- 90



#####################################################Chapter 2 - Automating Files and the file system################################################

#Reading and Writing files - Read length of text and find the nth character

file_path = 'bookofdreams.txt' #Make sure you create this file in the same folder
open_file= open(file_path,'r')

text= open_file.read()
len(text)
text[11] #This reads the 11th character


open_file.close() #Once your done. You can close file so it doesn't consume resources


#Reading and writing files - Readlines, I've also 

open_file = open(file_path,'r')
text = open_file.readlines()
len(text)

text[100] # Lets see what the 100th line says

open_file.close()




if open_file.closed is True:
     print("yupppp its closedd")
elif open_file.closed == False:    #Notice how I can use "is" and ==
      print("hey wait the file is stil open")
else:
     print("I'm not sure what's going on here. You can close the file using open_file.close()")


#You can read binary files by appending a b to mode







#Writing to a file using the write. You can define environment variables and application runtimes in a file names .envrc.  Direnv uses it to set these things up when you enter the directory with the file

text = """ export STAGE=DEVVVV..: export TABLE_ID=token-storage-1234"""

with open('.envrc','w') as opened_file: #Open file creates a file if it doesn't exist. Overwrties it if it does
     opened_file.write(text)

!cat .envrc #Perhaps these needs iPython.




#Pathlib for reading and writing files.

import pathlib

path = pathlib.Path('bookofdreams.txt')

path.read_text()


#Pathlib to read binary data. Let's use path.read_bytes method

#Overwrtie or write a new file. There are methods for writing text and for writing binary data
path = pathlib.Path('bookofdreams.txt')
path.write_text("d:p")










