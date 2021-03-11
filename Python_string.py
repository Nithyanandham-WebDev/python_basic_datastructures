#!/usr/bin/env python
# coding: utf-8

# # Python Strings
# 
# Python has a built-in string class named "str" with many handy features.
# 
# String literals can be enclosed by either double or single quotes, although single quotes are more commonly used.
# 
# Python strings are "immutable" which means they cannot be changed after they are created.
# 
# Characters in a string can be accessed using the standard [] syntax.
# 
# Python uses zero-based indexing, so if s is 'hello' s[1] is 'e'. 
# 
# If the index is out of bounds for the string, Python raises an error. 
# 
# The len(string) function returns the length of a string.

# In[64]:


# String Declaration

String_1 = "Python Strings"
String_2 = "Understanding and Implementation"
string_list3 = ["Schmitt","King","Ferguson","Labrune","bergulfsen","Nelson","Piestrzeniewicz",
"Keitel","Murphy","Lee","Freyre","Berglund","Petersen","Saveley","Natividad","Young","Leong","Hashimoto","Victorino","Oeztan",
"Franco","de Castro","Rancé","Bertrand","Tseng","King","Kentary","Frick","Karttunen","Ashworth","Cassidy","Taylor","Devon","Tamuri",
"Barajas","Young","Walker","Citeaux","Gao","Saavedra","Young","Kloss","Ibsen","Fresnière","Camino","Thompson","Bennett","Roulet","Messner"
"Accorti","Da Silv","Tonini","Pfalzheim","Lincoln","Franken","OHara","Rovelli","Huxley","Hernandez","Harrison","Holz","Klaeboe","Schuyler","Anderse","Koskitalo","Dewey"
"Frick","Huang","Brown","Graham","Brown","Brown","Calaghan","Suominen","Cramer","Cervantes","Fernandez","Chandler","McKenna",
"Lebihan","Henriot","Kuger","MacKinlay","Josephs","Yoshido","Young","Rodriguez","Urs","Nelson","Cartrain","Pipps","Cruz","Moroni"
"Shimamura","Perrier","Müller","McRoy","Donnermeyer","Hernandez","Feuer","Lewis","Larsson","Frick","Mendel","Murphy""Choi"]

# In[65]:


String_1
String_2

# "Understanding and Implementation"

# # String Operators

# In[66]:


# The + Operator
#The + operator concatenates strings. It returns a string consisting of the operands joined together:
String_Concat_Operator = String_1 +' '+ String_2


# In[67]:


String_Operator_Concat

# 'Python Strings Understanding and Implementation'

# In[68]:


#The * Operator
#The * operator creates multiple copies of a string.
String_Multi_Operator = (String_1+' ') *3


# In[69]:


String_Multi_Operator


# # The in Operator and not in Operator
#     Python also provides a membership operator that can be used with strings. The in operator returns True if the first operand is contained within the second, and False otherwise:

# In[70]:


# Using in Operator
String_1 in (String_1 + String_2)
"r" in 'operator'


# In[71]:


# Using not in Operator
String_1 not in (String_1 + String_2)
"r"  not in 'operator'


# # String Indexing
# Often in programming languages, individual items in an ordered set of data can be accessed directly using a numeric index or key value. This process is referred to as indexing.
# 
# In Python, strings are ordered sequences of character data, and thus can be indexed in this way. Individual characters in a string can be accessed by specifying the string name followed by a number in square brackets ([]).
# 
# String indexing in Python is zero-based: the first character in the string has index 0, the next has index 1, and so on. The index of the last character will be the length of the string minus one.
# 
# String indices can also be specified with negative numbers, in which case indexing occurs from the end of the string backward: -1 refers to the last character, -2 the second-to-last character

# ![google_str.png](attachment:google_str.png)

# In[72]:


String_Indexing_Ex_1 = "Python Strings Basic Understanding and Implementation"


# In[73]:


String_Indexing_Ex_1[0]     #Prints First Character i.e Index 0
String_Indexing_Ex_1[-1]     #Prints Last Character i.e Index -1


# # String Slicing
# 
# ## Syntax:
# 
#    ## String[start:Stop:Step]
# 
# 
# 

# In[74]:


String_Indexing_Ex_1[0:]     #Prints all Character Starts From Index 0


# In[75]:


String_Indexing_Ex_1[5:9]     #Prints Characters Between Index 5 to 8


# In[76]:


String_Indexing_Ex_1[0:9:3]     #Prints Characters Between Index 0 to 8 with Step 3


# In[77]:


String_Indexing_Ex_1[-3:]     #Prints Last 3 Characters.


# In[78]:


String_Indexing_Ex_1[-9:-3]     #Prints Character i.e Index -9 to -3


# In[79]:


String_Indexing_Ex_1[::-1]     #Prints String in Reverse Order


# In[80]:


String_Indexing_Ex_1[-12:-2:2]     #Prints Last Character i.e Index -12 to -2 with Step 2


# In[82]:


String_Indexing_Ex_1[:]    #Gives us a copy of the whole String


# # String Functions

# In[85]:


# chr()  #-->Converts an integer(i.e ASCII Value) to a character

chr(97)


# In[87]:


# ord()  #-->Converts Given Character to an Integer(i.e ASCII Value).

ord("9")


# In[92]:


# len()  #-->Converts Given Character to an Integer(i.e ASCII Value).

len("9597218896")


# In[95]:


# str()  #-->Returns a string representation of an object(i.e Converts Given Value to String)


str(1345)


# # Case Conversion Functions

# In[98]:


# capitalize()     -->Capitalizes the target string.

String_Test_Capitalize = "Test String to Test Capitalize Function"

String_Test_Capitalize.capitalize()



# In[102]:


# lower()     -->Converts alphabetic characters to lowercase.

String_Test_Lower = "Test String to Test LowerCase Function"

String_Test_Lower.lower()

"python_67".lower()   #false

"python_pydev34".lower()  #false

"python".lower()          #true        

# In[104]:


# upper()     -->Converts alphabetic characters to uppercase.

String_Test_Upper = "Test String to Test UpperCase Function"

String_Test_Upper.upper()


"python_67".upper()   #false

"python_pydev34".upper()  #false

"PYTHON".upper()          #true

# In[105]:


# swapcase()     -->Swaps case of alphabetic characters.

String_Test_SwapCase = "Test String to Test SwapCase Function"

String_Test_SwapCase.swapcase()


# In[110]:


# title()     -->Converts the target string to “title case.”

String_Test_Title = "test string to test title function"

String_Test_Title.title()


# In[118]:


# CaseFold()     -->Return a version of the string suitable for caseless comparisons.

String_Test_CaseFold = "Test String to Test CaseFold Function"

String_Test_CaseFold.casefold()


# # String Find and Replace Functions.

# In[127]:


# count()     -->Return a version of the string suitable for caseless comparisons.

#S.count(sub[, start[, end]]) -> int   S-->String

String_Test_Count = "Test String to Test Count Function"

String_Test_Count.count('T')

String_Test_Count.count('e',2,19)    #With Start,Stop Index


# In[135]:


import re
String_Find_Replace_Fn_Test  = []
for x in dir(str):
    if(re.search(r'^[a-z]',x)):
        String_Find_Replace_Fn_Test.append(x)
['capitalize',
'casefold',
'center',
'count',
'encode',
'endswith',
'expandtabs', 
'find',
'format',
'format_map',
'index',
'isalnum',
'isalpha',
'isascii',
'isdecimal',
'isdigit',
'isidentifier',
'islower',
'isnumeric',
'isprintable',
'isspace',
'istitle',
'isupper',
'join',
'ljust',
'lower',
'lstrip',
'maketrans',
'partition',
'removeprefix',
'removesuffix',
'replace',
'rfind',
'rindex',
'rjust',
'rpartition',
'rsplit',
'rstrip',
'split',
'splitlines',
'startswith',
'strip',
'swapcase',
'title',
'translate',
'upper',
'zfill']


# startswith(Sub_String, Start_Index, Stop_Index)     -->Determines whether the target string ends with a given substring.
# Emits/Returns True or False.
# Here Start and Stop is Optional
# str.startswith("Some_String",4) refers Consider String From Position 4

String_Find_Replace_Fn_StartsWith = []
for x in String_List_3:
    if x.startswith("S"):
        String_Find_Replace_Fn_StartsWith.append(x)

String_Find_Replace_Fn_StartsWith

['Schmitt', 'Saveley', 'Saavedra', 'Schuyler', 'Suominen']


String_Find_Replace_Fn_StartsWith_Index = []
for x in String_List_3:
        if x.startswith("t",3,5):
            String_Find_Replace_Fn_StartsWith_Index.append(x)
String_Find_Replace_Fn_StartsWith_Index


['Keitel',
 'Victorino',
 'Oeztan',
 'Bertrand',
 'Kentary',
 'Karttunen',
 'Cartrain']

# In[158]:


# endswith(<suffix>[, <start>[, <end>]])     -->Determines whether the target string ends with a given substring.
# Emits/Returns True or False. 

String_Find_Replace_Fn_EndsWith = []
for x in String_Find_Replace_Fn_Test:
    if x.endswith("t"):
        String_Find_Replace_Fn_EndsWith.append(x)

String_Find_Replace_Fn_EndsWith       

['count', 'format', 'isdigit', 'ljust', 'rjust', 'rsplit', 'split']


String_Find_Replace_Fn_EndsWith_Index = []
for x in String_List_3:
        if x.endswith("t",0,5):
            String_Find_Replace_Fn_EndsWith_Index.append(x)
String_Find_Replace_Fn_EndsWith_Index

['Piestrzeniewicz', 'Karttunen']


# find(Sub_String, Start_Index, Stop_Index)     -->Searches the target string for a given substring.
# returns the lowest index where substring is found
#returns -1 if substring is not found

String_Find_Replace_Fn_Find = "Here are some of the most common string methods. A method is like a function, but it runs \"on\" an object If the variable s is a string, then the code s.lower() runs the lower() method on that string object and returns the result (this idea of a method running on an object is one of the basic ideas that make up Object Oriented Programming, OOP). Here are some of the most common string methods"

String_Find_Replace_Fn_Find.find('that',189) # Finds that after 188th index



# index(Sub_String, Start_Index, Stop_Index)     -->Searches the target string for a given substring.
# returns the lowest index where substring is found
#raises error if substring is not found

String_Find_Replace_Fn_Index = "Here are some of the most common string methods. A method is like a function, but it runs \"on\" an object. If the variable s is a string, then the code s.lower() runs the lower() method on that string object and returns the result (this idea of a method running on an object is one of the basic ideas that make up Object Oriented Programming, OOP). Here are some of the most common string methods"

String_Find_Replace_Fn_Index.index('string') # Finds that after 188th index


# rfind(Sub_String, Start_Index, Stop_Index))     -->Searches the target string for a given substring starting at the end.
# returns the Highest index where substring is found
#returns -1 if substring is not found

String_Find_Replace_Fn_Rfind = "Here are some of the most common string methods. A method is like a function, but it runs \"on\" an object. If the variable s is a string, then the code s.lower() runs the lower() method on that string object and returns the result (this idea of a method running on an object is one of the basic ideas that make up Object Oriented Programming, OOP). Here are some of the most common string methods"

String_Find_Replace_Fn_Find.rfind('method') # Finds that after 188th index


# rindex(Sub_String, Start_Index, Stop_Index))     -->Searches the target string for a given substring starting at the end.
# returns the lowest index where substring is found
#raises error if substring is not found

String_Find_Replace_Fn_Rindex = "Here are some of the most common string methods. A method is like a function, but it runs \"on\" an object. If the variable s is a string, then the code s.lower() runs the lower() method on that string object and returns the result (this idea of a method running on an object is one of the basic ideas that make up Object Oriented Programming, OOP). Here are some of the most common string methods"

String_Find_Replace_Fn_Index.rindex('object') # Finds that after 188th index

# In[153]:


# center      -->center align the string using a specified character (space is default) as the fill character


# center(Width,Fill)     -->Centers a string in a field.
# Width Argument is mandatory
#Fill optional(Default WhiteSpace)

"Python".center(10)     #Means Total 10 Characaters and Place Python in Middle

"Python".center(10,"~")  #Fill White Spaces With ~.


# In[ ]:


# expandtabs    -->methods sets the tab size to the specified number of whitespaces.


# expandtabs(TabSize = <AnyValue(int)>)     -->Expands tabs in a string.
#replaces each tab character ('\t') with spaces.

"Python\tLanguage\t".expandtabs(tabsize = 20)

"Python\tLanguage\t".expandtabs(tabsize = 15)

'Python         Language'

# In[ ]:


# find          -->first occurrence of the specified value


String_Test_find = "Test String to Test find Function"

String_Test_find.find()


# In[ ]:


# format   -->returns the formatted  string


String_Test_format = "Test String to Test format Function"

String_Test_format.format()



# In[ ]:



# isalnum -->returns true if all the character are alphanumeric,meaning alphabet letter (a-z) and numbers(0-9)


String_Test_isalnum = "Test String to Test isalnum Function"

String_Test_isalnum.isalnum() 

"python_67".isalnum()    #false because "_" 

"python23".isalnum()     #true


# In[ ]:


# 'isalpha',   --> does not take any parameters.

# "true" if all character in the string are alphabet,otherwise,its return "false"

returns:

# true - if  all character in the string  are alphabets.

# false - if the string contain 1 or more non - alphabets


String_Test_isalpha = "Test String to Test isalpha Function"

String_Test_isalpha.isalpha()

"python_78".isalpha()   #false because "_" and 78 

"python".isalpha()      #true
 
# In[ ]:


# isascii  -->function returns a readable version of any object (string,tuples,list,etc)


String_Test_isascii = "Test String to Test isascii Function"

String_Test_isascii.isascii()


# In[ ]:


# isdecimal -->methods returns true if all the charcters are decimal (0-9).



String_Test_isdecimal = "Test String to Test isdecimal Function"

String_Test_isdecimal.isdecimal()


# In[ ]:


# isdigit --> does not take any parameters


# "true" if all character in the string are digit,otherwise,its return "false"

returns:

# true - if  all character in the string  are digit.

# false - if the string contain 1 or more non - digit


String_Test_isdigit = "Test String to Test isdigit Function"

String_Test_isdigit.isdigit()


"Python_Version_38".isdigit()     #False

"PythonVersion38".isdigit()     #False    

"PythonVersion".isdigit()     #False

"262593".isdigit()     #True

# In[ ]:


# isidentifier --> methods returns true if the string is a valid identifer,otherwise false.


String_Test_isidentifier = "Test String to Test isidentifier Function"

String_Test_isidentifier.isidentifier()


"Python_Version_38".isidentifier()     #False

"PythonVersion38".isidentifier()     #False    

"for".isidentifier()     #True

"True".isidentifier()     #True


# In[ ]:


# islower    -->returns true if all the charcters are in lower case,otherwise  false.


String_Test_islower = "Test String to Test islower Function"

String_Test_islower.islower()


"Python_Version_38".islower()     #False

"Python_Version_38".islower()     #False

"pythonversion".islower()     #True


# In[ ]:


# isnumeric  -->returns true if all charcters in the string are numeric 


String_Test_isnumeric = "Test String to Test isnumeric Function"

String_Test_isnumeric.isnumeric()

"python_45".isnumeric()   #false

"pythondevpy45".isnumeric()   #false

"pythondevpy".isnumeric()     #false

"122324".isnumeric()          #true          

# In[ ]:


# isprintable  -->returns true if all charcters in the string are printable


String_Test_isprintable = "Test String to Test isprintable Function"

String_Test_isprintable.isprintable()


"nithyanandham".isprintable()     #True

"nithyanandham123".isprintable()     #True

"nithyanandham\n".isprintable()     #False '\n' Character


# In[ ]:


# isspace   -->returns true if all charcters in the string are whitespaces

String_Test_isspace = "Test String to Test isspace Function"

String_Test_isspace.isspace()


"".isspace()     #False

" ".isspace()     #True

"Python ".isspace()     #False

"\t\t".isspace()     #True

"Python\t".isspace()     #False

# In[ ]:

# istitle  -->returns true if the string follows the rule of a title

String_Test_istitle = "Test String to Test istitle Function"

String_Test_istitle.istitle()


"Python Is Scripting Language".istitle()     #True

"Python Is scripting language".istitle()     #False

# In[ ]:


# isupper  -->returns true if all charcters in the string are upper case.

String_Test_isupper = "Test String to Test isupper Function"

String_Test_isupper.isupper()


"Python_Version_38".isupper()     #False

"Python_Version_38".isupper()     #False

"pythonversion".isupper()     #False

"PYTHON".isupper()     #True

# In[ ]:


# join   -->Concatenates strings from an iterable(List/Tuple/String).

# Needs a Separator String

# '<Sep>'.join(<Iteratable>)

' :: '.join(String_Find_Replace_Fn_Test)

capitalize::casefold::center::count::encode::endswith::expandtabs::find::format::format_map::index::isalnum::isalpha::isascii::isdecimal::
isdigit::isidentifier::islower::isnumeric::isprintable::isspace::istitle::isupper::join::ljust::lower::lstrip::maketrans::partition::
removeprefix::removesuffix::replace::rfind::rindex::rjust::rpartition::rsplit::rstrip::split::splitlines::startswith::strip::swapcase::
title::translate::upper::zfill

# In[ ]:


# ljust  -->Left-justifies a string in field.
# Width Argument is mandatory
#Fill optional(Default WhiteSpace)

"Python".ljust(10)     #Means Total 10 Characaters and Place WhiteSpace after String.

"Python".ljust(10,"~")  #Fill White Spaces With ~.st()


# In[ ]:


# lstrip --> Trims leading characters from a string.
#<chars>Optional. A set of characters to remove as leading characters
"     Python".lstrip()     #Prints "Python" Removes White Spaces From Starting.

"Vignesh:Python".lstrip('Vi')  #Strips Characters From Left

"++++x...y!!z* nithyanandhampython".lstrip("+.!xyz*")   #' nithyanandhampython'

# In[ ]:


# partition  --> method searches for a specified string, and splits the string into a tuple containing three elements.


# The first element contains the part before the specified string.

# The second element contains the specified string.

# The third element contains the part after the string


String_Test_parition = "Test String to Test partition Function"

String_Test_parition.partition()

"nithyanandham.thiru@gmail.com".partition(".")

"nithyanandham.thiru@gmail.com".partition("@")

('nithyanandham.thiru', '@', 'gmail.com')
# In[ ]:


# replace  --> method replaces a specified phrase with another specified phrase

String_Test_replace = "Test String to Test replace Function"

String_Test_replace.replace()



# In[ ]:


# rjust  -->method will right align the string, using a specified character (space is default) as the fill character



String_Test_rjust= "Test String to Test rjust Function"

String_Test_rjust.rjust()

# In[ ]:


# rpartition  --> method searches for the last occurrence of a specified string, and splits the string into a tuple containing three elements.


The first element contains the part before the specified string.

The second element contains the specified string.

The third element contains the part after the string.



String_Test_rpartition= "Test String to Test partition Function"

String_Test_rjust.rpartition()


# rpartition(<Sep>)     -->Divides a string based on a separator.
# rpartition(<sep>) splits String at the Last occurrence of string <sep>. 

# The return value is a three-part tuple consisting of:

# -->1-# The portion of s preceding <sep>
# ->2# <sep> itself
# ->3# The portion of s following <sep>


"nithyanandham.thiru@gmail.com".partition(".")

"nithyanandham.thiru@gmail.com".partition("@")

('nithyanandham.thiru', '@', 'gmail.com')

# In[ ]:


# rsplit   -->method splits a string into a list, starting from the right


# rsplit(sep=None, maxsplit=-1)     -->Splits a string into a list of substrings.
# Without arguments, rsplit() splits s into substrings delimited by any sequence of whitespace
# If the optional keyword parameter <maxsplit> is specified, a maximum of that many splits are performed, starting from the right end of s

String_Conversion_Fn_Rsplit = "Here are some of the most common string methods. A method is like a function, but it runs \"on\" an object. If the variable s is a string, then the code s.lower() runs the lower() method on that string object and returns the result (this idea of a method running on an object is one of the basic ideas that make up Object Oriented Programming, OOP). Here are some of the most common string methods"


String_Conversion_Fn_Rsplit.rsplit()   #Split Done on Every Whitespace

String_Conversion_Fn_Rsplit.rsplit(maxsplit = 3)

"nithyanandham,Python,Learning".rsplit(',')

['nithyanandham', 'Python', 'Learning']

# In[ ]:


# rstrip   -->Trims trailing characters from a string.
#<chars>Optional. A set of characters to remove as leading characters
"Python     ".rstrip()     #Prints "Python" Removes White Spaces From Ending.

"nithyanandhamPython++++x...y!!z*".rstrip("*zyx!.+")   #' nithyanandhampython'

# In[ ]:

# split(sep=None, maxsplit=-1)     -->Splits a string into a list of substrings.
# Without arguments, split() splits s into substrings delimited by any sequence of whitespace
# If the optional keyword parameter <maxsplit> is specified, a maximum of that many splits are performed, starting from the Lest end of String

String_Conversion_Fn_split = "Here are some of the most common string methods. A method is like a function, but it runs \"on\" an object. If the variable s is a string, then the code s.lower() runs the lower() method on that string object and returns the result (this idea of a method running on an object is one of the basic ideas that make up Object Oriented Programming, OOP). Here are some of the most common string methods"

String_Conversion_Fn_Rsplit.rsplit()   #Split Done on Every Whitespace

String_Conversion_Fn_Rsplit.rsplit(maxsplit = 3)

"nithyanandham,Python,Learning".rsplit(',')

['nithyanandham', 'Python', 'Learning']

# In[ ]:


# splitlines   --> method splits a string into a list.

# splitlines(<KeepEnds>)    ->Breaks a string at line boundaries.
# splits String up into lines and returns them in a list.
# If the optional <keepends> argument is specified and is True|1, then the lines boundaries are retained in the result strings:

String_Conversion_Fn_SplitLines = "Here are some of the most common string methods\n. A method is like a function, but it runs \"on\" an object\n. If the variable s is a string, then the code s.lower() runs the lower() method on that string object and returns the result (this idea of a method running on an object is one of the basic ideas that make up Object Oriented Programming, OOP).\n Here are some of the most common string methods"

String_Conversion_Fn_SplitLines.splitlines(1)

String_Conversion_Fn_SplitLines.splitlines()


# In[ ]:


# strip       --> Trims leading characters from a string.
#<chars>Optional. A set of characters to remove as leading characters
"     Python     ".strip()     #Prints "Python" Removes White Spaces From Start and End.


"nithyanandhamPython++++x...y!!z*".rstrip("*zyx!.+")   #' nithyanandhampython'

# In[ ]:


# zfill      --> method adds zeros (0) at the beginning of the string, until it reaches the specified length.

# If the value of the len parameter is less than the length of the string, no filling is done.


String_Test_zfill= "Test String to Test zfill Function"

String_Test_zfill.zfill()

"python".zfill(9)

"pythonlong".zfill(12)

"00pythonlong"







