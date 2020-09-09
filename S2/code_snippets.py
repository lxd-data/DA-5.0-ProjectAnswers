"""
File for testing code snippets to make sure their
expected behavior matches their actual behavior.
"""

# 2.1.2

def remove_duplicates(lista):
    listb=[]
    if lista:
        for item in lista:
            if item not in listb:
                listb.append(item)
    else:
        return lista
    return listb

print(remove_duplicates([1, 2, 3, 3, 3, 3, 2, 2, 1]))

print("This is Python")

print("Hello, I am", 29 + 1, " years old")

print("Hello, world!")

print("Hello, World!")

# Define the general structure of the song with default values
song = {
    "song_id":0,    # song reference id, default : 0
    "name": "",     # song name, default: empty string
    "length_seconds": 0     # song length in seconds, default: 0
}

# Here is an example of how you can
# create comments across multiple lines
# in Python.

print('doesn\'t') # use '\' to escape the single quote