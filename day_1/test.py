def countWords(text):
    counter = len(text.split(" "))
    return f"Text has {counter} words."


text = "My name is Vinicius Bortoletto"

print(countWords(text))
