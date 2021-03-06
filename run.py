from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField
# from stki_scripts.main import findSim
from stki_scripts.w11 import final_terakhir
import os
# 
app = Flask(__name__)
app.config.update(dict(SECRET_KEY='12345'))

class SearchTask(FlaskForm):
    keyword = TextField('Keyword')
    search = SubmitField('Search')

def searchTask(form):
    keyword = form.keyword.data
    path_corpus = "./text files"
    # keyword = keyword.split()
    # keyword normalize
    res = final_terakhir(keyword, path_corpus)
    return res

@app.route('/', methods=['GET','POST'])
def main():
    # create form
    sform = SearchTask(prefix='sform')

    # get response
    data = {}
    if sform.validate_on_submit() and sform.search.data:
        data = searchTask(sform)
    
    # render HTML
    return render_template('home.html', sform = sform, data = data)

@app.route('/text/<path:path>')
def opentext(path):
    textcontent = {}
    location = os.path.dirname(__file__)
    fullpath = os.path.join(location, "static/text/", path)
    resp = open(fullpath).read()
    textcontent[0] = resp.split(',',1)

    return render_template('text.html', data= textcontent)

if __name__=='__main__':
    app.run(debug=True)