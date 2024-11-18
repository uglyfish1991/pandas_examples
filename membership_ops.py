
#* ----------------------- Riddles! ------------------
#? There are times, when working with huan inputs and normal flows of language, that if statements with exact comparisons might not work as well as we'd like. 

#? Take a look at the riddle below:
#! What coat is always wet when you put it on? 

#? The answer is paint, but the answer could also be: 
#? A coat of paint
#? coat of paint
#? paint coat
#? or any other way a person might want to say paint. 

#? In previous sessions, we would have used the "or" logical operator to have many situations trigger the same response

user_answer = input("What coat is always wet when you put it on?")

if user_answer == "paint" or user_answer =="coat of paint" or user_answer =="paint coat" or user_answer =="a coat of paint":
    print("Correct")
else:
    print("Incorrect =[ ")

#? The above code isn't wrong, but it still doesn't cover every situation. Users could make slight typos like "acoat of paint" that doesn't make their answer incorrect, but hasn't been included in our if statement!

#? Instead, we can rely on
#* in
#? A membership operator. 
#? In works very much like it would in English. "If there's yoghurt in the fridge.....", "if there's a red pair in stock......" - it helps see if a something belongs to a whole

#? in this instance, is the substring "paint" belongs anywhere in the full string user_answer

if "paint" in user_answer:
    print("Well done")
else:
    print("incorrect")

#? it is a more flexible way for us to work with data! 
