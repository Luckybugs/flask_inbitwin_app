from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mail import Mail, Message
from wtforms import Form, StringField, TextAreaField, validators
from urllib import quote
from wtforms.csrf.session import SessionCSRF
from config import ADMINS


from data import Projects

app = Flask(__name__)

app.config.from_object('config')




mail = Mail(app)

Projects = Projects()

def no_spaces(string):
    return quote(string)



@app.route('/')
def index():
    return render_template('home.html', projects = Projects)

@app.route('/showreel')
def showreel():
    return render_template('showreel.html')

@app.route('/projects')
def projects():
    return render_template('projects.html', projects = Projects)

@app.route('/projects/<page>/')
def project(page):
    for p in Projects:
        if page in p.values():
            current = p
    return render_template('project.html', page=page, current=current)




@app.route('/article')
def article():
    return render_template('article.html')



# FORM CLASS

class MyBaseForm(Form):
    class Meta:
        csrf = True
        csrf_class = SessionCSRF
        csrf_secret = 'CSRF_SECRET_KEY'

        @property
        def csrf_context(self):
            return session

class EmailForm(MyBaseForm):
    name = StringField('Name', [validators.Length(min=2, max=50, message='That\'s not a valid name.')])
    email = StringField('Email', [
        validators.Length(min=6, max=120, message='Little short for an email address?'),
        validators.Email(message='That\'s not a valid email address.')
    ])
    message = TextAreaField('Message', [validators.Length(min=20, message='Not much to say?')])



@app.route('/about', methods=["GET", "POST"])
def about():

    form = EmailForm(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        message = form.message.data
  
        
        msg = Message('inbitwin.com message from ' + name, sender=ADMINS[0], recipients=ADMINS)
        msg.body = message + '\n from: \n' + name + '\n' + email
        mail.send(msg)

        success = 'Your message has been sent'
        return render_template('about.html', form=form, success=success)

    elif request.method == 'POST' and not form.validate():

        print form.name.data, form.email.data, form.message.data, form.validate(), form.errors
        error = 'Youre message has not been sent!'
        return render_template('about.html', form=form, error=error)


    return render_template('about.html', form=form)



if __name__ == '__main__':
   
    app.run(debug=True)
    