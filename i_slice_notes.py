
#*  ------------------- Slice Notation -----------------------

my_string = "helLo everyone!"
#? We know we can access a specific location in a string using index position. 
#? This allows us to isolate a specific element in a collection. 

print(my_string[3])
#* Result - L 

#? Slice notation allows us to reference multiple values to take a chunk of a string. 
#? Is follows the pattern start : stop : step

#? This is like how range works! We give a start value, a stopping value, and how to move through that sequence!

print(my_string[3:9:1])
#* Result - Lo eve
#? Start at index 3, stop at 9, step by 1
#? Like range, this stops 1 step short, so we actually only see index positions 3,4,5,6,7, and 8
