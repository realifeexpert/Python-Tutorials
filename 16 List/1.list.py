# Lists

#Lists are used to store multiple items in a single variable.
#Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.
#Lists are created using square brackets:

thislist = ["apple", "banana", "cherry"]
print(thislist)


# List Items

#List items are ordered, changeable, and allow duplicate values.
#List items are indexed, the first item has index [0], the second item has index [1] etc.


# Ordered

#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#If you add new items to a list, the new items will be placed at the end of the list.

# Note: There are some list methods that will change the order, but in general: the order of the items will not change.


# Changeable

#The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.


# Allow Duplicates

#Since lists are indexed, lists can have items with the same value:

thislist = ["apple", "banana", "cherry", "apple", "cherry"]

print(thislist)


# List Length

#To determine how many items a list has, use the len() function:

thislist = ["apple", "banana", "cherry"]
print(len(thislist))


# List Items - Data Types

#List items can be of any data type:
#String, int and boolean data types:

list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)


#A list can contain different data types:

list1 = ["abc", 34, True, 40, "male"]

print(list1)


# type()

#From Python's perspective, lists are defined as objects with the data type 'list':
#<class 'list'>

mylist = ["apple", "banana", "cherry"]

print(type(mylist))



# The list() Constructor

#It is also possible to use the list() constructor when creating a new list.

thislist = list(("apple", "banana", "cherry"))        # note the double round-brackets
print(thislist)


# Python Collections (Arrays)

#There are four collection data types in the Python programming language:

"""
1. List is a collection which is ordered and changeable. Allows duplicate members.
2. Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
3. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
4. Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""

#*Set items are unchangeable, but you can remove and/or add items whenever you like.
#**As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.   
#When choosing a collection type, it is useful to understand the properties of that type. Choosing the right type for a particular data set could mean retention of meaning, and, it could mean an increase in efficiency or security.


