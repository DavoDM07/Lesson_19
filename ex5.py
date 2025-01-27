#Given a list of words, create a dictionary where keys are words, and values are
#their lengths, but only for words with lengths greater than 3.


words = ["davit","aren","karen","arevshat","joe"]
length_list = [len(i) for i in words if len(i) > 3]
print(length_list)
