
Python Tuples
Tuple Basics And Syntax



-->Tuples are identical to lists in all respects, except for the following properties:

-->Tuples are defined by enclosing the elements in parentheses (()).

-->Tuples are immutable.i.e It wont supports Item assignment after creation.

-->Tuple Indexing and Slicing is as same as List.

When To Use Tuples
-->Faster Execution when Compared to List.

-->When Data remain Constant


#Tuple Packing
Tuple_with_Data = ("First_Value","Second_Value","Third_Value","Fourth_value","Fifth_Value","Sixth_Value","Last_Value")

Tuple_with_Data[0]


#Tuple UnPacking
(t1,t2,t3,t4,t5,t6,t7) = Tuple_with_Data
t1
t2
t3

Tuple Built-in Fns


# count()   -->Returns No Occurrencess of a Value in Tuple
Tuple_Count_Test = (1,4,2,3,4,2,3,4,65,4,4,6)
Tuple_Count_Test.count(6)
Tuple_Count_Test.count(4)


# Index()   -->Returns Index of the First Occurrencess of a Value in Tuple
Tuple_Count_Test = (1,2,3,4,2,3,4,65,4,4,6)
Tuple_Count_Test.index(6)
Tuple_Count_Test.index(4)
Tuple_Count_Test.index(4)