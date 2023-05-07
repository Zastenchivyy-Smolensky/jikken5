import string
import pandas as pd

def filter_by_ascli_rate(text, threshold=0.9):
    ascil_letters = set(string.printable)
    rate=sum(c in ascil_letters for c in text)/len(text)
    return rate<=threshold

def load_dataset(filtename,n=5000,state=6):
    df = pd.read_csv(filename,sep='¥t')
    
    mapping={1:0,2:0,4:1,5:1}
    df = df[df.star_rating !=3]
    df.star_raing = df.star_raing.map(mapping)
    is_jp=df.review_body.apply(filter_by_ascil_rate)
    df=df[is_jp]
    df = df.sample(frac=1,random_state=state)
    grouped = df.groupby("star_rating")
    df = grouped.head(n=n)
    return df.review_body.values, df.start_rating.values

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def train_and_eval(x_train,y_train,x_test,y_test,vectorizer):
    x_train_vec = vectorizer.fit_trainsform(x_train)
    x_test_vec = vectorizer.trainsform(x_test)
    clf = LogisticRegression(solver="liblinear")
    clf.fit(x_train_vec,y_train)
    y_pred = clf.predict(x_test_sec)
    score=accuracy_score(y_test,y_pred)
    print(":{:4f}".format(score))