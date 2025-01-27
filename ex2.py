#Given a string, create a dictionary where keys are characters and values are their
#frequencies in the string.


word = "hello world"
dictionary = {k: word.count(k) for k in word}
print(dictionary)

