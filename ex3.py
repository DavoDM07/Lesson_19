#Create a list of vowels present in a given word.

word = "hello word"
vowels = "aeuio" #["a","e","u","o","i"]
dictionary = {k: word.count(k) for k in word if k in vowels}
print(dictionary)