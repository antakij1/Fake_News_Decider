import pickle
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

###change these paths to be specific to your computer###
train = pickle.load(open("C:/Users/Joe/PycharmProjects/fakenews/data/train_array.pkl", 'rb'))
labels = pickle.load(open("C:/Users/Joe/PycharmProjects/fakenews/data/train_labels.pkl", 'rb'))

data_train, data_test, labels_train, labels_test = train_test_split(train, labels, test_size = 0.33)

model = tree.DecisionTreeClassifier()
model.fit(data_train, labels_train) #training our decision tree on our labelled training data. It compares what it got (real or fake) to what the true answer is for each article, and adjusts itself accordingly
predicted_labels = model.predict(data_test) #using our trained decision tree to predict answers (real or fake) for our test data

print(accuracy_score(labels_test, predicted_labels))

#Though it's clunky right now, you can compare what the decision tree classified the articles as,
#based on amount of all-caps words and amount of curse words per article, to what you think each one
#should be. We should find either a better database(I couldn't) or split our train data into
#two halves, and use those as our testing/training. Sklearn has a function to do this, "train-test-split."

#For ease of viewing, the predicted labels can be viewed as a csv file. 1 is fake news, 0 is "true" news