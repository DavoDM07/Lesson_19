#Givenastring, create a dictionary where keys are characters, and values are
#their ASCII values.



word = "hello word"
dictionary = {k: ord(k) for k in word}
print(dictionary)