from flask import Flask,render_template,request
import requests

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/home')
def index():
    response=requests.get('http://127.0.0.1:5000/api/teams')
    teams=response.json()['teams']

    return render_template('index.html',teams=sorted(teams))

@app.route('/teamvteam')
def teamvteam():
    team1=request.args.get('team1')
    team2=request.args.get('team2')

    response=requests.get('http://127.0.0.1:5000/api/teamvteam?team1={}&team2={}'.format(team1,team2))
    response=response.json()

    response1=requests.get('http://127.0.0.1:5000/api/teams')
    teams=response1.json()['teams']

    return render_template('index.html',result=response,teams=sorted(teams))

@app.route('/batsman_records')
def batsman_records():

    batsman=request.args.get('batsman')

    response=requests.get('http://127.0.0.1:5000/api/batsman-record?batsman={}'.format(batsman))
    response=response.json()
    return render_template('batsman.html',result=response)

@app.route('/bowler_records')
def bowler_records():

    bowler=request.args.get('bowler')

    response=requests.get('http://127.0.0.1:5000/api/bowler-record?bowler={}'.format(bowler))
    response=response.json()
    return render_template('bowler.html',result=response)

app.run(debug=True,port=8000)