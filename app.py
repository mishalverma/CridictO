from flask import Flask, render_template,request
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler


ui = Flask(__name__)
model_odi = pickle.load(open('model_odi.pkl', 'rb'))
model_t20 = pickle.load(open('model_t20.pkl', 'rb'))


@ui.route('/')
def Cridicto():

    return render_template('Cridicto.html')


@ui.route('/end_inning',methods =["GET", "POST"])
def end_inning():
    
    Format = int(request.form.get('inning-type'))
    Runs = int(request.form.get('score'))
    Wickets = int(request.form.get('wickets'))
    overs = str(request.form.get('overs'))
    balls = str(request.form.get('balls'))
    Striker = int(request.form.get('struns'))
    NStriker = int(request.form.get('nstruns'))

    Overs = float(overs+'.'+balls)
    
    
    if(Format==50):
        prediction = model_odi.predict(np.array([[Runs,Wickets,Overs,Striker,NStriker]]))
    elif(Format==20):
        prediction = model_t20.predict(np.array([[Runs,Wickets,Overs,Striker,NStriker]]))
    else:
        prediction = [0]
    
    output=round(prediction[0])

    return render_template('Cridicto.html',prediction_text="Predicted Score is {}".format(output))

@ui.route('/WorldCup/')
def WorldCup():

    return render_template('WorldCup.html')

@ui.route('/WorldCup/GroupStage',methods =["GET", "POST"])
def GroupStage():
    return render_template('GroupStage.html')

@ui.route('/WorldCup/GroupStage/Super12',methods =["GET", "POST"])
def Super12():
    return render_template('Super12.html')

@ui.route('/WorldCup/GroupStage/Super12/SemiFinals',methods =["GET", "POST"])
def SemiFinals():
    return render_template('SemiFinals.html')

@ui.route('/WorldCup/GroupStage/Super12/SemiFinals/Finals',methods =["GET", "POST"])
def Finals():
    return render_template('Finals.html')

@ui.route('/Winner',methods =["GET", "POST"])
def Winner():
    return render_template('Result.html',result='Winner of T20 World Cup 2021 will be England')

if __name__ == "__main__":

    ui.run(debug=True)

