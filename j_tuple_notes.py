
#* ----------------------- Tuples ------------------

#? Lists are collections which hold many pieces of data
#? Dictionaries hold many items as key : value pairs
#? Tuples are another collection data type. 

#? Take a look at this list: 

coffee_order = [
    "Alex - Cortado",
    "Ben - Latte",
    "Charlie - Mocha"
]

#? We know we can use many methods on this list to change the list, like .append()

coffee_order.append("Diana - Hot Chocolate")

#? Take a look at this syntax: 

coffee_order = (
    "Alex - Cortado",
    "Ben - Latte",
    "Charlie - Mocha"
)

#? This is a tuple. It is like a list in that in can hold a collection of data. But try to change it:
#! coffee_order.append("Diana - Hot Chocolate")

#? You will get an error!
#! AttributeError: 'tuple' object has no attribute 'append'

#? Tuples cannot be changed by methods once they've been made. They are a very safe collection type, because no one can accidently change them!

#? Tuples should be used when the order the pieces of data are in is important. For example if I gave you come co-ordinates:

#* (5, 19)

#? You know 5 is the x-axis, and 19 is the y-axis. This is because the order they are in provides structure. Tuples should be used for this - because their orders can't be changed!