#These are the possible lists of taste attributes we need to validate.
taste_list = ["sweet","tart","dry","juicy"]
user_tastes = []

#user_flavor will store the user's response.
user_flavor = ""

print("Welcome to the Watermelon Patch.")

while True:
    user_flavor = input("Is the watermelon sweet, tart, dry, or juicy? Enter as many flavors as you like. Enter \"done\" when you are done: ")
    user_flavor = user_flavor.strip().lower()
    if user_flavor[-1] == '!':
        print("I'm glad you're excited, but enter a correct value")
        continue
    if user_flavor == "done":
        break
    if user_flavor in taste_list:
        print(f"Response recorded, it was {user_flavor}")
        user_tastes.append(user_flavor)
    else:
        print("That is not a valid response!")
    print("Collection more tastes...")
#---1
print(f"Entries recorded. You listed: {user_tastes}")


user_val = 0
while user_val < 1 or user_val > 10:
    user_rating = input("Please rate the watermelon from 1-10: ")
    if user_rating[-1] == '!':
        print("We can't take factorials!")
        continue
    if user_rating.isdigit() == True:
        user_val = int(user_rating)
        if user_val > 0 and user_val < 4:
            print("That bad? I'm sorry you didn't like it!")
        elif user_val > 3 and user_val < 8:
            print("So just average, huh?")
        elif user_val > 7 and user_val <= 10:
            print("Pretty good, I'm glad you liked it")
        else:
            print("That is not a valid number. Please enter a valid number from 1 to 10.")
    else:
        print("That is not a number. Please try again.")
#---2