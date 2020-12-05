# SER531
Template-based Question Answering analysis on the LCQuAD2.0 Dataset

## Team 17

Akshay Kumar Dileep

Anurag Mishra

Ria Mehta

Siddharth Uppal

## Prerequisites for Setup

Python3

Nodejs

Npm

Python3 Packages - 
```
flask
flask_cors
flask_restful
pandas
ast
pandas
numpy
collections
itertools
sister
sklearn.preprocessing
pickle
xgboost
nltk
```

## Installation

Clone the applicaiton. 

```
git clone https://github.com/MasterAkay/SER531.git
```

Installing And Setting Up the Web App -

Browse to the "Webapp Demonstration" folder in terminal

```
npm install
npm start
```
The above commands will start the Angular application on http://localhost:4200/

Installing And Setting Up the Web API.


Browse to the "WebAPI" folder in a seperate terminal instance
```
python3 API.py
```

Now that we have both the API and Web App running in seperate instances of the terminal enter the query in the webapp to get the result.


## Database Required 

The first time you request the api it will search if the database is already present in the local machine if not it will download it which can take NOTE: Upto 15 min to download. Do not end the request or close the browser when it downloads.





