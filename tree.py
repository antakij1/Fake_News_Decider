import pickle
import csv
from sklearn import tree

###change these paths to be specific to your computer###
train = pickle.load(open("C:/Users/Joe/Downloads/fake-news/train_array.pkl", 'rb'))
labels = pickle.load(open("C:/Users/Joe/Downloads/fake-news/train_labels.pkl", 'rb'))
test = pickle.load(open("C:/Users/Joe/Downloads/fake-news/test_array.pkl", 'rb'))

model = tree.DecisionTreeClassifier()
model.fit(train, labels) #training our decision tree on our labelled training data. It compares what it got (real or fake) to what the true answer is for each article, and adjusts itself accordingly
predicted_labels = model.predict(test) #using our trained decision tree to predict answers (real or fake) for our test data

with open("C:/Users/Joe/Downloads/fake-news/labels.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=',')
    writer.writerow(['Label'])
    for n in range(len(predicted_labels)):
        writer.writerow([predicted_labels[n]])


#Though it's clunky right now, you can compare what the decision tree classified the articles as,
#based on amount of all-caps words and amount of curse words per article, to what you think each one
#should be. We should find either a better database(I couldn't) or split our train data into
#two halves, and use those as our testing/training. Sklearn has a function to do this, "train-test-split."

#For ease of viewing, the predicted labels can be viewed as a csv file. 1 is fake news, 0 is "true" news