import os
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split

def load_datasets_unlabeled_test():
    dataset = load_files('review_polarity_competition/reviews_sentoken', shuffle=False)
    docs_train, docs_dev, y_train, y_dev = train_test_split(
        dataset.data, dataset.target, test_size=0.10, random_state=42)
    dirname = "review_polarity_competition/test_reviews_sentoken"
    test = []
    # I do this to keep the files in numeric order
    for fname in range(len(os.listdir(dirname))):
        fname = str(fname) + ".txt"
        with open(os.path.join(dirname, fname)) as fd:
            test.append(fd.read())
    train = docs_train, y_train
    dev = docs_dev, y_dev
    return train, dev, test

def save_results(fname, labels):
    with open(fname, 'w') as f:
        f.write("Id,Category\n")
        for i,l in enumerate(labels):
            f.write(str(i) + ".txt," + str(l) + "\n")

from sklearn import metrics

    
def print_eval(model, X, y_true):
    y_pred = model.predict(X)
    acc = metrics.accuracy_score(y_true, y_pred)
    print('accuracy\t{:2.2f}\n'.format(acc))
    print(metrics.classification_report(y_true, y_pred, target_names=['neg', 'pos']))
    cm = metrics.confusion_matrix(y_true, y_pred)
    print(cm)


def eval(model, X, y_true):
    y_pred = model.predict(X)
    acc = metrics.accuracy_score(y_true, y_pred)
    f1 = metrics.f1_score(y_true, y_pred, average='macro')
    return {'acc': acc, 'f1': f1}


def print_short_eval(model, X, y_true):
    res = eval(model, X, y_true)
    print('accuracy\t{acc:2.2f}\tmacro f1\t{f1:2.2f}'.format(**res))

    
import pickle


def save_model(model, filename):
    with open(filename, 'wb') as f:
        pickle.dump(model, f)

def load_model(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)
