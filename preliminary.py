import nltk
import csv
import pickle

curses = ['fuck', 'fucking', 'fucked', 'fucks', 'shit', 'shits', 'damn', 'damned']

def count_screaming(words):
    score = 0
    for word in words:
        if word.isupper():
            score += 1
    return score

def count_cursing(words):
    score = 0
    for word in words:
        if word.lower() in curses:
            score += 1
    return score

def generate_array(path):
    results = []
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            tokenized = nltk.word_tokenize(row[3])
            results.append([count_screaming(tokenized), count_cursing(tokenized)])
    return results


###change these paths to be specific to your computer###
train_array = generate_array("C:/Users/Joe/Downloads/fake-news/train_clean.csv")
test_array = generate_array("C:/Users/Joe/Downloads/fake-news/test_clean.csv")

#This is done outside of generate_array because the test set does not have labels to check against
labels = []
with open("C:/Users/Joe/Downloads/fake-news/train_clean.csv", newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        labels.append(row[4])

pickle.dump(train_array, open("C:/Users/Joe/Downloads/fake-news/train_array.pkl", 'wb'))
pickle.dump(test_array, open("C:/Users/Joe/Downloads/fake-news/test_array.pkl", 'wb'))
pickle.dump(labels, open("C:/Users/Joe/Downloads/fake-news/train_labels.pkl", 'wb'))