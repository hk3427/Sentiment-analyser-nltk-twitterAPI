from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("coming"))
print(lemmatizer.lemmatize("worst",pos = "a"))
print(lemmatizer.lemmatize("Robotics"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("run",'v'))