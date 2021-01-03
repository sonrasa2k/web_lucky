from flask import Flask
import numpy as np
from flask import Flask, flash, request, redirect, url_for, render_template
import pandas as pd
day_in_data = []
moth_in_data = []
rank_in_data = []
app = Flask(__name__,template_folder='templates')
def get_data(path_csv):
    global day_in_data
    global moth_in_data
    global rank_in_data
    data = pd.read_csv(path_csv)
    day_in_data = data[['day']].values
    moth_in_data = data[['month']].values
    rank_in_data = data[['rank']].values
    print(rank_in_data[0])

@app.route('/')
def upload_form():
    return render_template('index.html')
@app.route('/lucky',methods=['POST'])
def get_date():
    day = request.form.get('date')
    month = request.form.get('month')
    get_data("lucky.csv")
    rank_final = ""
    for i in range(len(day_in_data)):
        if int(day) == int(day_in_data[i]) and int(month) == int(moth_in_data[i]):
            rank_final = int(rank_in_data[i])
    rank_final = "Bạn xếp thứ : "+ str(rank_final)+"/366"
    return render_template('index.html',rank = rank_final)


if __name__ == "__main__":
    app.run(debug=True)