
import re
import csv
import json
import random
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

class BotNB:
    def __init__(self):
        self.data = None
        self.patterns = []
        self.tags = []
        self.responses = []
        self.index = None

    def train(self, json_file, test_data=None):
        with open(json_file) as file:
            self.data = dict(json.load(file))

        for dictionary in self.data["intents"]:
            patterns = dictionary.get("patterns")
            tag = dictionary.get("tag")
            responses = dictionary.get("responses")

            for pattern in patterns:
                self.patterns.append(pattern.lower())
                self.tags.append(tag.lower())

            for response in responses:
                self.responses.append(response.lower())

        self.X_train = self.patterns
        self.Y_train = self.tags
        self.X_test = self.patterns
        self.Y_test = self.tags

        self.vectorizer = CountVectorizer()
        self.X_train = self.vectorizer.fit_transform(self.X_train)
        self.X_test = self.vectorizer.transform(self.X_test)

        # initialize a model
        self.model = MultinomialNB()
        self.model.fit(self.X_train, self.Y_train)

        # make a predictions with testing set
        predictions = self.model.predict(self.X_test)

        # get the prediction info
        self.accuracy = accuracy_score(self.Y_test, predictions)
        self.confusion_mat = confusion_matrix(self.Y_test, predictions)
        self.report = classification_report(self.Y_test, predictions, zero_division=0)

    def respond(self, text):
        vector = self.vectorizer.transform([text.lower()])
        predicted_class = self.model.predict(vector)[0]
        pred_prob = self.model.predict_proba(vector)[0][0]

        class_response_pool = [d["responses"] for d in self.data["intents"] if d["tag"] == predicted_class][0]
        response = random.choice(class_response_pool)

        return (predicted_class, response, pred_prob)

if __name__ == "__main__":
    mybot = BotNB()
    mybot.train("data/intents.json")
    report = mybot.report
    print(report)

    while True:
        text = input(">> ")
        response = mybot.respond(text)
        print(response)
