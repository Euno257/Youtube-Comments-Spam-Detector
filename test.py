import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

df= pd.read_csv("YoutubeSpamMergedData.csv")
df_data = df[["CONTENT","CLASS"]]
# Features and Labels
df_x = df_data['CONTENT']
df_y = df_data.CLASS
# Extract Feature With CountVectorizer
corpus = df_x
cv = CountVectorizer()
X = cv.fit_transform(corpus) # Fit the Data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, df_y, test_size=0.33, random_state=42)
#Naive Bayes Classifier
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB()
clf.fit(X_train,y_train)
score = clf.score(X_test,y_test)
print(score)
