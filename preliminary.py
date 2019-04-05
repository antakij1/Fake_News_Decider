import nltk
import csv
import pickle
curses = ['fuck', 'fucking', 'fucked', 'fucks', 'shit', 'shits', 'damn', 'damned', 'crap']

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

def avg_wordlength(words):
    numerator = 0.0
    denominator = len(words)
    for w in words:
        numerator = numerator + len(w)
    return numerator/denominator if denominator != 0 else 0

def generate_array(path):
    results = []
    with open(path, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=',')
        for row in reader:
            tokenized = nltk.word_tokenize(row[3])
            tokenized = [w for w in tokenized if not w in stop_words]
            results.append([count_screaming(tokenized), count_cursing(tokenized), avg_wordlength(tokenized)])
    return results

stop_words = set(nltk.corpus.stopwords.words('english'))
###change these paths to be specific to your computer###
train_array = generate_array("C:/Users/Joe/PycharmProjects/fakenews/data/train_clean.csv")

#This is done outside of generate_array because the test set does not have labels to check against
labels = []
with open("C:/Users/Joe/PycharmProjects/fakenews/data/train_clean.csv", newline='', encoding='utf-8') as file:
    reader = csv.reader(file, delimiter=',')
    for row in reader:
        labels.append(row[4])

pickle.dump(train_array, open("C:/Users/Joe/PycharmProjects/fakenews/data/train_array.pkl", 'wb'))
pickle.dump(labels, open("C:/Users/Joe/PycharmProjects/fakenews/data/train_labels.pkl", 'wb'))