#These are the possible lists of taste attributes we need to validate.
taste_list = ["sweet","tart","dry","juicy"]

#user_flavor will store the user's response.
user_flavor = input("Welcome to the Watermelon Patch. Is the watermelon sweet, tart, dry, or juicy? ")

#Task 1: Use .strip() and .lower() to clean the users response
user_flavor = user_flavor.strip().lower()
#---1

#Task 2: Test if the users response is valid, and let them know.
if user_flavor in taste_list:
    print(f"{user_flavor}")
else:
    print("not valid")
#---2

user_rating = input("Please rate the watermelon from 1-10: ")

#Task 3: Test if the user inputted an actual digit, then respond differently if it was bad, average, or good. 
if user_rating.isdigit():
    user_rating = int(user_rating)
    if 1 <= user_rating <= 3:
        print("bad")
    elif 4 <= user_rating <= 7:
        print("average")
    elif 8 <= user_rating <= 10:
        print("good")
    else:
        print("valid number")
else:
    print("not valid")
#---3