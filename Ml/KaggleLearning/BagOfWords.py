#!/usr/bin/python
# -*- coding: UTF-8 -*-
import os
import pandas as pd
import numpy as np

path = "E:\\python\\Practice\\Ml\\KaggleLearning\\word2vec-nlp-tutorial"
unlabled_train_data_path = os.path.join(path, 'unlabeledTrainData.tsv')
labled_train_data_path = os.path.join(path, 'labeledTrainData.tsv')
test_data_path = os.path.join(path, 'testData.tsv')

labled_train_data = pd.read_csv(labled_train_data_path, header=0, quoting=3, delimiter='\t')

labled_train_data.describe()

# Data Cleaning and Text Preprocessing
from bs4 import BeautifulSoup

# Initialize the BeautifulSoup object on a single movie review
example1 = BeautifulSoup(labled_train_data["review"][0])

# Print the raw review and then the output of get_text(), for
# comparison
print(labled_train_data["review"][0])
print(example1.get_text())

import re

# Use regular expressions to do a find-and-replace
# [^a-zA-Z] 所有的不是字母
letters_only = re.sub("[^a-zA-Z]",  # The pattern to search for
                      " ",  # The pattern to replace it with
                      example1.get_text())  # The text to search
print(letters_only)

low_case = letters_only.lower()
# tokenization
words = low_case.split()

from nltk.corpus import stopwords

words = [word for word in words if word not in stopwords.words('english')]
print(words)


def review_to_words(raw_review):
    raw_text = BeautifulSoup(raw_review, "html5lib").get_text()

    letters_only_text = re.sub("[^a-zA-Z]", " ", raw_text)

    words = letters_only_text.lower().split()

    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))

    # remove stops
    meaningful_words = [word for word in words if word not in stops]

    return (" ".join(meaningful_words))


clean_train_reviews = []
for review in labled_train_data['review']:
    if ((review.index() + 1) % 1000 == 0):
        print("Review {} of {}\n".format(review.index() + 1, labled_train_data['review'].size))
    clean_train_reviews.append(review_to_words(review))

# creating bag of words
from sklearn.feature_extraction.text import CountVectorizer

vectorizer = CountVectorizer(analyzer="word",
                             tokenizer=None,
                             preprocessor=None,
                             stop_words=None,
                             max_features=5000)

# fit_transform() does two functions: First, it fits the model
# and learns the vocabulary; second, it transforms our training data
# into feature vectors. The input to fit_transform should be a list of
# strings.
train_data_features = vectorizer.fit_transform(clean_train_reviews)

# Numpy arrays are easy to work with, so convert the result to an
# array
train_data_features = train_data_features.toarray()

# Take a look at the words in the vocabulary
vocab = vectorizer.get_feature_names()

dist = np.sum(train_data_features, axis=0)

for tag, count in zip(vocab, dist):
    print(tag, count)

from sklearn.ensemble import RandomForestClassifier

# Initialize a Random Forest classifier with 100 trees
forest = RandomForestClassifier(n_estimators=100)

# Fit the forest to the training set, using the bag of words as
# features and the sentiment labels as the response variable
#
# This may take a few minutes to run
forest = forest.fit(train_data_features, labled_train_data["sentiment"])

# Read the test data
test = pd.read_csv(test_data_path, header=0, delimiter="\t", quoting=3)

# Verify that there are 25,000 rows and 2 columns
print(test.shape)

# Create an empty list and append the clean reviews one by one
num_reviews = len(test["review"])
clean_test_reviews = []

for i in range(0, num_reviews):
    if ((i + 1) % 1000 == 0):
        print("Review %d of %d\n" % (i + 1, num_reviews))

    clean_review = review_to_words(test["review"][i])
    clean_test_reviews.append(clean_review)

# Get a bag of words for the test set, and convert to a numpy array
test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()

# Use the random forest to make sentiment label predictions
result = forest.predict(test_data_features)

# Copy the results to a pandas dataframe with an "id" column and
# a "sentiment" column
output = pd.DataFrame(data={"id": test["id"], "sentiment": result})

# Use pandas to write the comma-separated output file
output.to_csv("Bag_of_Words_model.csv", index=False, quoting=3)
