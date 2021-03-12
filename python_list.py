List_Comprehension
List Creating Methods

import itertools

# 1.0 creating  a empty list 

list = []

# 1.1 creating two  or  more empty list in single line 

list_1,list_2,list_3 = [],[],[]

# 1.2 creating list in with data 

list_with_data_1 = ["first_value","second_value","third_value","fourth_value","fifth_value","six_value","last_value"]

list_with_data_2 = ["python","fileio","db","monogodb","5"]

list_with_data3  = [1,2,3,4,5,6,7,8]

# 1.3 using range

# syntax --> range(strat_value,end_value,step_value)

list_using_range1,list_using_range2 = range(0,22,1),range(0,12,3)


# 1.4 Using For to Create List
List_Created_Using_Loops = [Iter_Var**3 for Iter_Var in range(10)] # Creates A List Multiples Of 3



# 1.5 Creating a List By Adding Old List 
List_Created_From_Adding = List_with_Data_2 + List_with_Data_1 # Simply Appends With the First List



# 1.6 Creating a Nested List Using Existing/New List 

# This Can Be Done Using Two Methods
# zip() --> In Python 3, zip returns an iterator. 
# zip() function stops when anyone of the list of all the lists gets exhausted. 
# In simple words, it runs till the smallest of all the lists


# zip_longest() : zip_longest stops when all lists are exhausted. 
# When the shorter iterator(s) are exhausted, 
# zip_longest yields a tuple with None value by default 
# You can Specify what to fill using  fillvalue=<any_value>
# Basic Explanation of itertools.zip_longest Using 3 lists.

#Both zip() and zip_longest() takes Minimum one Iterable as argument,


Nested_List = list(itertools.zip_longest(List_with_Data_1,List_with_Data_2,List_with_Data_3,fillvalue = "NA"))

In [ ]:  List

In [ ]:  List_1,List_2,List_3

In [ ]:  List_2

In [ ]:  List_with_Data_1

In [ ]:  List_Created_Using_Loops

In [ ]:  List_Created_From_Adding

In [ ]:  Nested_List



Indexing And Slicing


# Python List Positive Index Starts with 0 and Negative Index Starts with -1.
# Basic Syntax

# List|Sting|Tuple[start_Index:Last_Index,Step]

List_with_Data_1[0]  #Prints First Value in a List


List_with_Data_1[-1] #Prints Last Value  in a List


List_with_Data_1[::] #Prints all Contents in a List Starts from Index 0


List_with_Data_1[::-1] #Prints all Contents in a List in Reverse Order Starts from Index -1


List_with_Data_1[:3:]  #Prints First 3 Elements in a List in Starts from Index 3


List_with_Data_1[-2-1::]  #Prints Last 3 Elements in a List


List_with_Data_1[::2] #Prints all Contents in a List in With Step 2 (i.e Every Even Index) Starts from Index 0


List_with_Data_1[::-2]  #Prints all Contents in a List in With Step 2 (i.e Every Odd Index) Starts from Index -1


#Prints Elements in a List from 2nd Index to 8th in With Step 2 (i.e Every Odd Index) Starts from Index 2
List_with_Data_1[2:8:2]


List_with_Data_1[-1:-6:-2]  #Prints all Contents in a List in With Step 2 (i.e Every Odd Index) Starts from Index -1


List Built-in Functions


# append("Value")   -->Appends an Value to a list.
List_with_Data_1

List_with_Data_1.append("Data_Appended")

List_with_Data_1


# clear   -->Truncates Entire List.
List_with_Data_1

List_with_Data_1.clear()

List_with_Data_1


# Copy   -->Copies Entire List to a New list.

List_with_Data_1_Copy = List_with_Data_1.copy()

List_with_Data_1_Copy

# Or

List_with_Data_1_Copy = List_with_Data_1[::]

List_with_Data_1_Copy


# extend(<Iter>)  --->Extends a list with the objects from an iterable.

List_with_Data_Extend = [x for x in range(1,3)]

List_with_Data_Extend.extend(List_with_Data_1)

List_with_Data_Extend

# Or

List_with_Data_Extend += List_with_Data_1

List_with_Data_Extend


# index  --> Return first index of value.

List_with_Data_Extend.index("Last_Value")


# insert(Index, Value)   -->Insert object before index

List_with_Data_Insert = [0,1,2,3,4,5,6,7,8]


List_with_Data_Insert.insert(4,"Inserted Before 4th Index")

List_with_Data_Insert

# Or

List_with_Data_Insert[3] = "Inserted at 3rd Index"

List_with_Data_Insert


# pop(index)   -->Removes an element from a list.
# defalut Value is -1 i.e last Index
# Should Specify Index
# returns removed value

List_with_Data_Pop = [x for x in range(21,28)]


List_with_Data_Pop.pop()


List_with_Data_Pop.pop(3)


# remove(Value)   -->Removes an object from a list.

List_with_Data_Remove = [x for x in range(10,18)]


List_with_Data_Remove

List_with_Data_Remove.remove(14)

List_with_Data_Remove


# reverse   -->Reverse tht List

List_with_Data_Reverse = [x for x in range(10,18)]


List_with_Data_Reverse.reverse()

List_with_Data_Reverse


# sort(reverse = True/False) -->Sort the list
# default Ascending Order i.e reverse = False
# default Decending Order

import random

# List_with_Data_Sort = [random.randrange(1,49) for x in range(10)]

List_with_Data_Sort = [15, 45, 25, 38, 43, 38, 38, 7, 21, 45]


List_with_Data_Sort.sort()

List_with_Data_Sort




































