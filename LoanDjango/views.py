from django.shortcuts import render
from django.http import HttpResponse
import pickle
import pandas as pd
import numpy as np


def index(request):
    return render(request, "home.html")


def result(request):
    features = ["CreditScore", "FirstTimeHomebuyer", "MSA",
                "MIP", "Units", "Occupancy", "OCLTV", "DTI", "OrigUPB", "OrigInterestRate",
                "Channel", "PPM", "PropertyState", "PropertyType", "LoanPurpose",
                "OrigLoanTerm", "NumBorrowers", "SellerName", "ServicerName", "MonthsDelinquent",
                "MonthsInRepayment"]
    with open('pipe_rf.pkl', 'rb') as f:
        model = pickle.load(f)

    features_values = np.array([request.GET[feature] for feature in features])

    data = pd.DataFrame([features_values], columns=features)
    prediction = model.predict(data)
    
    return render(request, "result.html", {'prediction': prediction[0]})
