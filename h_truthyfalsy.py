
#* ------------------ Truthy / Falsy ------------------------

#? We know that we can compare two values, and a boolean is made in the background to find out if this comparison is true or false

music = "classical"
print(music=="classical")
#* Result - True

#? We also know we can cast data, and turn it into a different data type
withdraw_amount = int(input("Please enter the amount you want to withdraw   > "))

#? We can force data to turn into a Boolean value, true or false. But what would be true, and what would be false?

music="classical"
my_favourite_songs = []
my_number = 0
my_name = ""
favourite_drink = "water"

#? See the results of forcing these to turn into values by using:
print(bool(music))

#? Some are True, and some are False!
#? Things which have a value are considered truthy values. They have properties. They're not the boolean True - but if we forced thatcasting, they would become True
#? Things with no value are falsy values. These are empty collections, numerical 0, None, and False. 

#? The truthy or falsy property of a value indicate one very important thing
#* Does some data exist?

#? Let's write some code to let a user sign in. 
#? We want to make sure that they 100% type something in. 

user_name = input("Please enter your chosen user name   > ")

#? We can't do exact comparisons like if name == "Abby" or if name == "Ben" or if name == "Cindy"....it would be impossible to know what the user will type. All we want to do is check they type something.

#? As long as the type something, it will be a truthy value. And truthy is True.
if user_name:
    print(f"Welcome to your new account, {user_name}")
else:
    print("You did not enter anything")
