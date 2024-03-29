from flask import Flask, request                    # request takes input from user in json.
import pickle

app = Flask(__name__)                               # Flask(__name__) is the name of the application's module or package

print(__name__)

with open("classifier.pkl", "rb") as f:
    clf = pickle.load(f)

@app.route("/welcome", methods = ["GET"])           #decorator to define additional part of the URL.
def welcome():                                      #function of additional part.
    return {'message': "Welcome to the page"}

# required info - gender, married, credit_history, applicant_income, loan_amount.

@app.route("/predict", methods = ["POST"])
def predict():
    """predcits wheather loan is approved or not"""

    loan_req = request.get_json()

    if loan_req['gender'] =='Male':
        gender = 0
    else:
        gender = 1
    
    if loan_req['married'] =='Unmarried':
        marital_status = 0
    else:
        marital_status = 1

    if loan_req['credit_history'] =='Unclear Debts':
        credit_history = 0
    else:
        credit_history = 1

    applicant_income = loan_req['applicant_income']
    loan_amount = loan_req['loan_amount']

    result = clf.predict([[gender, marital_status, credit_history, applicant_income, loan_amount]])

    if result == 0:
        pred = 'Rejected'
    else:
        pred = 'Approved'

    return {"loan_approval_status": pred}

@app.route("/template", methods = ["GET"])
def template():
    return {
	"gender": "Male/Female",
	"married": "Married/Unmarriefd",
	"applicant_income": "<Numeric Salary>",
	"loan_amount": "Numeric loan amount",
	"credit_history": "Cleared Debts / Uncleared Debts"}


def sum_something(a,b):
    return a+b

def sub_something(a,b):
    return a-b