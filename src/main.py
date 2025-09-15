import numpy as np
import pandas as pd
import sklearn as sk
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, f1_score, recall_score
import tkinter as tk
from tkinter import filedialog
from data import DataLoader


def load_email():
    tk.Tk().withdraw()
    file_path = filedialog.askopenfilename(title="Select an email", 
                                           filetypes=[("Text files", "*.txt"), ("Email files", "*.eml") , ("All files", "*.")])
    if file_path:
        with open(file_path,"r",encoding="utf-8") as f:
            return f.read()
    else:
        return None



loader = DataLoader()
easy_ham, hard_ham, spam = loader.load_emails("data/archive.zip")

all_emails = easy_ham + hard_ham + spam
labels = ['easy_ham'] * len(easy_ham) + ['hard_ham'] * len(hard_ham) + ['spam'] * len(spam)

vectorizer = CountVectorizer(lowercase = True, stop_words="english")
X = vectorizer.fit_transform(all_emails)

X_train, X_test, y_train, y_test = train_test_split(X,labels,test_size=0.2,random_state=42, stratify=labels)

nb = MultinomialNB()
nb.fit(X_train,y_train)

y_pred = nb.predict(X_test)

print("Accuracy :", accuracy_score(y_test, y_pred))

print("Precision :", precision_score(y_test, y_pred, average="macro"))

print("Recall :", recall_score(y_test, y_pred, average="macro"))

print("f1_score :", f1_score(y_test, y_pred, average="macro"))

# print("Vocabulary:", vectorizer.vocabulary_)

email_text = load_email()
if email_text:
    X_new = vectorizer.transform([email_text])
    prediction = nb.predict(X_new)
    print("Prediction for new email :", prediction)
else:
    print("No Email selected!")



        

