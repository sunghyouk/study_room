import os
import pickle
import sqlite3
import time
# for backup (+ timestamp)
from shutil import copyfile

import numpy as np

# 로컬 디렉토리에서 HashingVectorizer를 임포트
from vectorizer import vect


def update_model(db_path, model, batch_size=10000):

    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT * from review_db')

    results = c.fetchmany(batch_size)
    while results:
        data = np.array(results)
        X = data[:, 0]
        y = data[:, 1].astype(int)

        classes = np.array([0, 1])
        X_train = vect.transform(X)
        model.partial_fit(X_train, y, classes=classes)
        results = c.fetchmany(batch_size)

    conn.close()
    return model


cur_dir = os.path.dirname(__file__)

clf = pickle.load(open(os.path.join(cur_dir,
                                    'pkl_objects',
                                    'classifier.pkl'), 'rb'))
db = os.path.join(cur_dir, 'reviews.sqlite')

# app.py에서 불러들임
# clf = update_model(db_path=db, model=clf, batch_size=10000)

# classifier.pkl 영구적 업데이트
# pickle.dump(clf, open(os.path.join(cur_dir,
#                                    'pkl_objects', 'classifier.pkl'), 'wb'),
#             protocol=4)

# Backup file + timestamp
timestr = time.strftime("%Y%m%d-%H%M%S")
orig_path = os.path.join(
    cur_dir, 'pkl_objects', 'classifier.pkl')
backup_path = os.path.join(
    cur_dir, 'pkl_objects',
    'classifier_%s.pkl' % timestr)
copyfile(orig_path, backup_path)
