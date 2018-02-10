from flask import Flask, render_template

from data import Projects

app = Flask(__name__)

Projects = Projects()

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/showreel')
def showreel():
    return render_template('showreel.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects = Projects)

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/article')
def article():
    return render_template('article.html')




if __name__ == '__main__':
    app.run(debug=True)
    