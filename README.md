# Spam-Detector-for-youtube-comments

## Install Flask
Within the activated environment, use the following command to install Flask:

<p><code> pip install Flask </code></p>
Flask is now installed. Check out the Quickstart or go to the Documentation Overview.

#### Living on the edge
If you want to work with the latest Flask code before it’s released, install or update the code from the master branch:

pip install -U https://github.com/pallets/flask/archive/master.tar.gz

## Folders
MainFolder/static 
MainFolder/templates 
MainFolder/app.py 
MainFolder/YoutubeSpamMergedData.csv

#### static
It contains all the .css,.js files and images that are to be used in the project.

#### templates 
Flask finds the HTML files in the templates folder, in the same folder in which this script is present.
In our project we are making home.html and result.html files inside the template folder.

#### app.py 
1. First we imported the Flask class. An instance of this class will be our WSGI application.
2. Next we create an instance of this class. The first argument is the name of the application’s module or package. If you are using a single module (as in this example), you should use __name__ because depending on if it’s started as application or imported as module the name will be different ('__main__' versus the actual import name). This is needed so that Flask knows where to look for templates, static files, and so on. For more information have a look at the Flask documentation.
3. We then use the route() decorator to tell Flask what URL should trigger our function.
4. The function is given a name which is also used to generate URLs for that particular function, and returns the message we    want to display in the user’s browser.
for more refer http://flask.pocoo.org/docs/1.0/quickstart

## Machine-Learning model
For text classification we are using Naive-Bayes Classifier's Multinomial model.

### Naive-Bayes-Classifier 
The multinomial Naive Bayes classifier is suitable for classification with discrete features (e.g., word counts for text classification). The multinomial distribution normally requires integer feature counts.
<p><code> class sklearn.naive_bayes.MultinomialNB(alpha=1.0, fit_prior=True, class_prior=None)[source] </code></p>
See documentation https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html

## Run project on localhost:5000
Execute the below command in the terminal 
<p><code> pyhton app.py </code></p>
