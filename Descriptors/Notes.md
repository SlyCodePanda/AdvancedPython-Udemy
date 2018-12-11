# Descriptors

## Introduction
<u>What is a descriptor?</u><br>
A class that gives us control over an attribute of another object.<br>
In general, a descriptor is an object attribute with “binding behavior”, one whose attribute access has been overridden by methods in the descriptor protocol.<br>
Those methods are ```__get__(), __set__(), and __delete__()```. If any of those methods are defined for an object, it is said to be a descriptor.<br>
<b>Get</b>, <b>Set</b>, and <b>Delete</b> are built in functions in Python.<br>
Define any of these methods and an object is considered a descriptor and can override default behavior upon being looked up as an attribute.<p>

<u>Advantages</u><br>
* They are used to avoid repeatable code.<br>
* They help us handle input in an ordered way.<br>
* They allow only particular types of data as requested, as they provide the user with a powerful validation tool.<br>
* The programmer can have multiple instances of each descriptor class to manage attributes with similar behaviour. In which each descriptor object<br>
is a unique instance of a descriptor class bound to a distinct attribute name when the owner class is defined.<br>

## Get, Set, and Delete Descriptors
<b>Get</b> : get(self, instance, owner)<br>
<b>Set</b> :set(self, instance, value)<br>
Must return the attribute's value.<br>

<b>Delete</b> :delete(self, instance)<br>
Must delete the value of the entire attribute.


#### Refs
https://docs.python.org/2/howto/descriptor.html
