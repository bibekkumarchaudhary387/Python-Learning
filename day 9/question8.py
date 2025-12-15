#Removing Stop Words
#Goal: Implement a basic stop word removal process, a common text preprocessing step in NLP.
#Task: Given a list of tokens, remove all stop words and return the resulting list.
#Python

tokens = ['the', 'model', 'is', 'training', 'quickly', 'and', 'the', 'data', 'is', 'clean']
stop_words = {'the', 'is', 'and'}

new_set = [
    token for token in tokens if token not in stop_words
]
print(new_set)