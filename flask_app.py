from flask import  request, jsonify, render_template
import flask
import json2table
import simplejson as json



app = flask.Flask(__name__)

@app.route('/')
def index():
        return flask.render_template('index1.html')
    
@app.route("/test" , methods=['GET', 'POST'])
def test():
        if flask.request.method == 'POST':
            select = flask.request.form.get('Company')
            if(select == 'OXY'):
                return OXY()
            if(select == 'EOG'):
                return EOG()
            if(select == 'APA'):
                return APA()
            if(select == 'APC'):
                return APC()
            if(select == 'COP'):
                return COP()

def OXY():
        json_data=open('OXY-summary.json').read()
        news = open('OXY_news.txt').read()
        data = json.loads(json_data)
        formatted_table = json2table.convert(data)
        return formatted_table+news

def EOG():   
        json_data=open('EOG-summary.json').read()
        news = open('EOG_news.txt').read()
        data = json.loads(json_data)
        formatted_table = json2table.convert(data)
        return formatted_table+news
    
def APA():
        json_data=open('APA-summary.json').read()
        news = open('APA_news.txt').read()
        data = json.loads(json_data)
        formatted_table = json2table.convert(data)
        return formatted_table+news
    
def APC():
        json_data=open('APC-summary.json').read()
        news = open('APA_news.txt').read()
        data = json.loads(json_data)
        formatted_table = json2table.convert(data)
        return formatted_table+news
    
def COP():
        json_data=open('COP-summary.json').read()
        news = open('COP_news.txt').read()
        data = json.loads(json_data)
        formatted_table = json2table.convert(data)
        return formatted_table+news

    
    
if __name__ == '__main__':
    app.run(debug=True)
