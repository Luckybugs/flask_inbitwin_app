from flask import Flask, render_template, request
from flask_mail import Mail, Message

from data import Projects

app = Flask(__name__)


# app.config.update(dict(
#     MAIL_SERVER = 'smtp.googlemail.com',
#     MAIL_PORT = 465,
#     MAIL_USE_TLS = False,
#     MAIL_USE_SSL = True,
#     MAIL_USERNAME = 'djurovic.jelena@gmail.com',
#     MAIL_PASSWORD = 'DjoleDontPanic'
# ))

mail = Mail(app)


Projects = Projects()



@app.route('/')
def index():
    return render_template('home.html')

@app.route('/showreel')
def showreel():
    return render_template('showreel.html')

@app.route('/ebemti')
def projects():
    return render_template('projects.html', projects = Projects)

@app.route('/projects/<string:title>/')
def project(title):
    for p in Projects:
        if title in p.values():
            current = p
    return render_template('project.html', title = title, current = current)

@app.route('/about' )
def about():

    # msg = Message('Test', sender='djurovic.jelena@gmail.com', recipients=['djurovic.jelena@gmail.com'])
    # msg.body = 'This is a test email' #Customize based on user input
    # mail.send(msg)
    return render_template('about.html')


@app.route('/article')
def article():
    return render_template('article.html')




if __name__ == '__main__':
    app.run(debug=True)
    