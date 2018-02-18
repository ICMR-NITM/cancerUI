#! /usr/bin/env python2

import cgi
import cgitb
import time
import os
cgitb.enable()

train_path = os.path.join(os.path.dirname(__file__), "data.csv")
test_path = os.path.join(os.path.dirname(__file__), "test_data.csv")



# coding: utf-8

# In[111]:
import sys


from Tkinter import *
import numpy as np
import pandas as pd
from sklearn.svm import SVC
from sklearn.cross_validation import train_test_split




data1 = pd.read_csv(train_path)


data1 = data1.drop(['Unnamed: 32','id'], axis=1)
y1 = data1.diagnosis 
x1 = data1.drop(['diagnosis'], axis=1)
X_train1, X_test1, y_train1, y_test1 = train_test_split(x1, y1, test_size=0.0, random_state=42)

data = pd.read_csv(test_path)
y = ['M']
x = data
X_test, X_train, y_test, y_train = train_test_split(x, y, test_size=0.0, random_state=42)


svc = SVC(kernel = 'linear',C=.1, gamma=10, probability = True)
svc.fit(x1,y1)
y_pred = svc.fit(X_train1, y_train1).predict(X_test)
out = pd.DataFrame(svc.predict_proba(X_test))
out.head()


color = ""
p_benign = 0
p_malignant = 0

header = "Content-type: text/html\n\n"

def for_user():
    
    message = ""
    p_benign = 0
    p_malignant = 0

    is_safe = ""
    img = ""

    i=0
    count=0
    for index, row in out.iterrows():
        print row[0], row[1]
        sys.stderr.write(str(row[0]))

        if row[0]<row[1]:
            message = "The predicted tumour is cancerous !!"
            color = "red"
            p_benign = round(row[0]*100, 2)
            p_malignant = round(row[1]*100, 2)
            is_safe = "Patient is not safe."
            img = "images/sad.gif"
            sys.stderr.write("not safe.\n")


        elif row[0]>row[1]:
            message = "The predicted tumour is non-cancerous !!"
            color = "green"
            p_benign = round(row[0]*100, 2)
            p_malignant = round(row[1]*100, 2)
            is_safe = "Patient is safe."
            img = "images/smile.gif"
            sys.stderr.write("safe.\n")

        sys.stderr.write(color)

        if color=="green":

            html = """

            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <meta name="description" content="">
                <meta name="author" content="">
                <link rel="icon" href="../../../../favicon.ico">

                <title>Breast cancer prediction</title>

                <!-- Bootstrap core CSS -->
                <link href="https://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">

                <!-- Custom styles for this template -->
                <link href="https://getbootstrap.com/docs/4.0/examples/starter-template/starter-template.css" rel="stylesheet">
              </head>

              <body>

                <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
                  <a class="navbar-brand" href="/cgi-bin/home.py">Cancer prediction tool</a>
                  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>

                </nav>

                <main role="main" class="container">

                  <div class="starter-template">
                    <h1>Report and predictions</h1><hr>
                  </div>
                  <div class="alert alert-success" role="alert">
                  <h1 class="alert-heading">The predicted tumour is not cancerous.</h1>
                  <hr>

                  <p>The cancer has been not diagnosed in the tumour. The patient is safe. </p>
                </div>

                </main><!-- /.container -->

                <!-- Bootstrap core JavaScript
                ================================================== -->
                <!-- Placed at the end of the document so the pages load faster -->
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script>window.jQuery || document.write('<script src="../../../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
                <script src="https://getbootstrap.com/assets/js/vendor/popper.min.js"></script>
                <script src="https://getbootstrap.com/dist/js/bootstrap.min.js"></script>
              </body>
            </html>

            """

            print header + html
            print '<h1 class="container">Probablity of Benign (non-cancerous): <span class="badge badge-info">%s</span></h1>' % (str(p_benign)+"%")
            print '<h1 class="container">Probablity of Malignant (cancerous): &nbsp; &nbsp; &nbsp;<span class="badge badge-info">%s</span></h1>' % (str(p_malignant)+"%")
            print "<br>"
            print '<a type="button" class="container btn btn-success btn-lg btn-block" href="http://localhost:8000/cgi-bin/home.py">TRY AGAIN</a>'


        else:
            html = """

            <!doctype html>
            <html lang="en">
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                <meta name="description" content="">
                <meta name="author" content="">
                <link rel="icon" href="../../../../favicon.ico">

                <title>Breast cancer prediction</title>

                <!-- Bootstrap core CSS -->
                <link href="https://getbootstrap.com/dist/css/bootstrap.min.css" rel="stylesheet">

                <!-- Custom styles for this template -->
                <link href="https://getbootstrap.com/docs/4.0/examples/starter-template/starter-template.css" rel="stylesheet">
              </head>

              <body>

                <nav class="navbar navbar-expand-md navbar-dark bg-dark fixed-top">
                  <a class="navbar-brand" href="/cgi-bin/home.py">Cancer prediction tool</a>
                  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarsExampleDefault" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
                    <span class="navbar-toggler-icon"></span>
                  </button>

                </nav>

                <main role="main" class="container">

                  <div class="starter-template">
                    <h1>Report and predictions</h1><hr>
                  </div>
                  <div class="alert alert-danger" role="alert">
                  <h1 class="alert-heading">The predicted tumour is cancerous.</h1>
                  <hr>

                  <p>The cancer has been diagnosed in the tumour. The patient needs immediate treatment. </p>
                </div>

                </main><!-- /.container -->

                <!-- Bootstrap core JavaScript
                ================================================== -->
                <!-- Placed at the end of the document so the pages load faster -->
                <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
                <script>window.jQuery || document.write('<script src="../../../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
                <script src="https://getbootstrap.com/assets/js/vendor/popper.min.js"></script>
                <script src="https://getbootstrap.com/dist/js/bootstrap.min.js"></script>
              </body>
            </html>

            """




            print header + html
            print '<h1 class="container">Probablity of Benign (non-cancerous): <span class="badge badge-info">%s</span></h1>' % (str(p_benign)+"%")
            print '<h1 class="container">Probablity of Malignant (cancerous): &nbsp; &nbsp; &nbsp;<span class="badge badge-info">%s</span></h1>' % (str(p_malignant)+"%")
            print "<br>"
            print '<a type="button" class="container btn btn-success btn-lg btn-block" href="http://localhost:8000/cgi-bin/home.py">TRY AGAIN</a>'

math_flag ="10"

print p_benign

print "<h2 class='container'> Probablity of Benign (non-cancerous) : %s</h2>" % str(p_benign)
print "<h2 class='container'> Probablity of Malign (cancerous) : %s</h2>" % str(p_malignant)







    
for_user()
header = "Content-type: text/html\n\n"

sys.stderr.write(color)
sys.stderr.write("Cscs")
sys.stderr.write(color)





