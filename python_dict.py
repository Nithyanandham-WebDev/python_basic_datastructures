
Python Dictionaries:

-->Unlike sequences, which are indexed by a range of numbers, dictionaries are indexed by keys,
 which can be any immutable type; strings and numbers can always be keys. -->You can’t use lists as keys
 --> Key Values duplication is not allowed. --> If New Entry Is placed Using Existing Key It Overrides the Existing Vlaues.

Dictionary Creation:

You can define a dictionary by enclosing a comma-separated list of key-value pairs in curly braces ({}). A colon (:) separates each key.

Dictionary = {

          <key_2>: <value>,

          .
          .
          .
          <key_n>: <value>
          }


# Creating_Dictionary Method#1
Dict_Creation = {
                 "Book_ISBN":"978-93-5110-201-4",
                 "Book_Name" : "Learning_Python",
                 "Book_Author" : "Mark Lutz",
                 "Book_Publisher" : "O'Reilly",
                 "Book_Edition" : "5th Edition"
                }



# Creating_Dictionary Method#2
# Using Dict() Method

Dict_Creation_Dict_Method = dict([
                 ("Book_ISBN","978-93-5110-201-4"),
                 ("Book_Name" , "Learning_Python"),
                 ("Book_Author" , "Mark Lutz"),
                 ("Book_Publisher" , "O'Reilly"),
                 ("Book_Edition" , "5th Edition")
                 				])

Dict_Creation


Dict_Creation_Dict_Method


# Creating_Dictionary Method#3
# Using for Loop
Dict_Creation_Dict_Using_For_Loop = {x:x**3 for x in range(1,7)}


Dict_Creation_Dict_Using_For_Loop


Dict_Practice_List = ["Schmitt","King","Ferguson","Labrune","bergulfsen","Nelson","Piestrzeniewicz",
"Keitel","Murphy","Lee","Freyre","Berglund","Petersen","Saveley","Natividad","Young","Leong","Hashimoto","Victorino","Oeztan",
"Franco","de Castro","Rancé","Bertrand","Tseng","King","Kentary","Frick","Karttunen","Ashworth","Cassidy","Taylor","Devon","Tamuri",
"Barajas","Young","Walker","Citeaux","Gao","Saavedra","Young","Kloss","Ibsen","Fresnière","Camino","Thompson","Bennett","Roulet","Messner"
"Accorti","Da Silv","Tonini","Pfalzheim","Lincoln","Franken","OHara","Rovelli","Huxley","Hernandez","Harrison","Holz","Klaeboe","Schuyler","Anderse","Koskitalo","Dewey"
"Frick","Huang","Brown","Graham","Brown","Brown","Calaghan","Suominen","Cramer","Cervantes","Fernandez","Chandler","McKenna",
"Lebihan","Henriot","Kuger","MacKinlay","Josephs","Yoshido","Young","Rodriguez","Urs","Nelson","Cartrain","Pipps","Cruz","Moroni"



Dict_Practice_List_1 = []
for x in Dict_Practice_List:
    Dict_Practice_List_1.append('Length of {} is {}'.format(x,len(x)))



# Creating_Dictionary Method#4
# Using Two list and Zip Method
Dict_Creation_Dict_Using_Two_Lists = dict(zip(Dict_Practice_List,Dict_Practice_List_1))


Operators And Functions
Operators



# in Operator

"King" in Dict_Creation_Dict_Using_Two_Lists     #True

"Operators" in Dict_Creation_Dict_Using_Two_Lists     #False



# not in Operator

"King" not in Dict_Creation_Dict_Using_Two_Lists     #False

"Operators" not in Dict_Creation_Dict_Using_Two_Lists     #True



# len() function returns the number of key-value pairs in a dictionary:

len(Dict_Creation_Dict_Using_Two_Lists)


Functions


# clear() Empties Dictionary
Dict_Creation_Dict_Using_Two_Lists


Dict_Creation_Dict_Using_Two_Lists.clear()


Dict_Creation_Dict_Using_Two_Lists



# get(Key, <default>) The Python dictionary .get() method provides a convenient way of getting the value of a key from a dictionary without checking ahead of time whether the key exists, and without raising an error.
#default Parameter Default value is -1
#default Parameter is optional If Specified as "1" returns 1 if Searched Key is not found.

Dict_Creation_Dict_Using_Two_Lists.get("Cruz")

Dict_Creation_Dict_Using_Two_Lists.get("Python",1)   #Returns 1 If Key Not Found



# items()     -->Returns a list of key-value pairs in a dictionary.
# returns a list of tuples containing the key-value pairs in d. The first item in each tuple is the key, and the second item is the key’s value.

Dict_Creation.items()


# keys()     -->Returns a list of keys in a dictionary.
# returns a list containing the key in dictionary.

Dict_Creation.keys()


# values()     -->Returns a list of values in a dictionary.
# returns a list containing the Values in dictionary.

Dict_Creation.values()



# del     -->Used to Delete Entry in dictionary.

del Dict_Creation['Book_Author']



Dict_Creation


# pop(Key, <default>)     -->Removes a key from a dictionary, if it is present, and returns its value.

#default Parameter Default value is -1
#default Parameter is optional If Specified as "1" returns 1 if Searched Key is not found.

Dict_Creation_Dict_Using_Two_Lists.pop("Cruz","3")

Dict_Creation_Dict_Using_Two_Lists.get("Vignesh",1)   #Returns 1 If Vignesh Not Found


# popitem()     -->Removes a key-value pair from a dictionary.

Dict_Creation

Dict_Creation.popitem()

Dict_Creation


# update(<obj>)     -->Merges a dictionary with another dictionary or with an iterable of key-value pairs.

Dict_Creation.update(Dict_Creation_Dict_Using_For_Loop)


"Shimamura","Perrier","Müller","McRoy","Donnermeyer","Hernandez","Feuer","Lewis","Larsson","Frick","Mendel","Murphy""Choi"]

