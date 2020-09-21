#These are the possible taste attributes you need to validate.
taste_list = ["sweet","tart","dry","juicy"]


#This is a list of user's responses to the taste of the watermelon.
user_tastes = ["tart","dry","juicy","tart","dry","sweet","sweet","dry","juicy","dry"]
#This is a list of user ratings.
user_ratings = [3,6,8,2,7,6,5,1,4,10]
#This is a list of quality. Each user rating needs to be qualified as "bad", "average", or "good"
quality_list = []

#Task 1: Fill quality_list with the quality of each watermelon rated in user_ratings.
for rating in user_ratings:
    if rating > 0 and rating < 4:
        quality_list.append("bad")
    elif rating > 3 and rating < 8:
        quality_list.append("average")
    elif rating > 7 and rating <= 10:
        quality_list.append("good")
print(quality_list)
#---1


#Task 2: Count how many of each flavor there is
for taste in taste_list:
    print(f"There are {user_tastes.count(taste)} watermelons that are {taste}")
#---2

#Task 3: Print the ratings of watermelons that are Juicy
print("Ratings of watermelons that are juicy:")
for i in range(len(user_tastes)):
    if user_tastes[i] == "juicy":
        print(user_ratings[i])
#---3