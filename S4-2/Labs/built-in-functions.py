import random 

# Creates a random list of integers between 200000 and 500000
video_views = random.sample(range(200000, 500000), 15)

# Creates a random list of integers between 50000 and 200000
video_likes = random.sample(range(50000, 200000), 15)

# the first task only checks for zip, not list
list(zip(video_likes, video_views))


# did not work (should?)
def divide_likes_views(pairs):
    likes = pairs[0]
    views = pairs[1]
    likes_div_views = round((likes/views) * 100, 2)
    return likes_div_views

# did work (shouldnt?)

def divide_likes_views(pairs):
    likes = pairs[0]
    views = pairs[1]
    likes_div_views = round((likes/views), 2)
    return likes_div_views

# doesnt, should! 
def divide_likes_views(pairs):
    percentage_likes = pairs[0]/pairs[1] * 100
    return round(percentage_likes, 2)

# works
def remove_lower(percent):
    if percent > .5:
        return True
    else:
        return False

# didnt
def remove_lower(percent):
    if percent < .5:
        return False
    else:
        return True