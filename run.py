from flask import Flask, render_template, redirect
from flask_wtf import FlaskForm
from wtforms import TextField, IntegerField, SubmitField
# from stki_scripts.main import findSim
from stki_scripts.w11 import findSim

app = Flask(__name__)
app.config.update(dict(SECRET_KEY='12345'))

class SearchTask(FlaskForm):
    keyword = TextField('Keyword')
    search = SubmitField('Search')

def searchTask(form):
    keyword = form.keyword.data
    path_corpus = "./text files"
    keyword = keyword.split()
    # keyword normalize
    res = findSim(keyword, path_corpus)
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

if __name__=='__main__':
    app.run(debug=True)