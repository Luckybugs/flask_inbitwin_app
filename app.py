from flask import Flask, render_template, request, flash, redirect, url_for, session
from flask_mail import Mail, Message
from wtforms import Form, StringField, TextAreaField, validators
from urllib import quote

from data import Projects

app = Flask(__name__)


app.config.update(dict(
    MAIL_SERVER = 'smtp.googlemail.com',
    MAIL_PORT = 465,
    MAIL_USE_TLS = False,
    MAIL_USE_SSL = True,
    MAIL_USERNAME = 'djurovic.jelena@gmail.com',
    MAIL_PASSWORD = 'DjoleDontPanic'
))

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

@app.route('/projects/<title>/')
def project(title):
    for p in Projects:
        if title in p.values():
            current = p
            
            app.logger.info(no_spaces(title))
    return render_template('project.html', title = title, current = current)




@app.route('/article')
def article():
    return render_template('article.html')

# FORM CLASS
class EmailForm(Form):
    name = StringField('Name', [validators.Length(min=2, max=50, message='not a valid name')])
    email = StringField('Email', [
        validators.Length(min=6, max=120, message='Little short for an email address?'),
        validators.Email(message='That\'s not a valid email address.')
    ])
    message = TextAreaField('Message', [validators.Length(min=20, message='Not much to say?')])



@app.route('/about', methods=["GET", "POST"] )
def about():
    form = EmailForm(request.form)

    if request.method == 'POST' and form.validate():
        name = form.name.data
        email = form.email.data
        message = form.message.data



        flash('jebote', 'success')
        msg = 'jej!!!!!!!'

        print form.name.data, form.email.data, form.message.data, form.validate(), form.errors
        
        # msg = Message('Test', sender=email, recipients=['djurovic.jelena@gmail.com'])
        # msg.body = message #Customize based on user input
        # mail.send(msg)

        return render_template('about.html', form=form, msg=msg)
    else:

        print form.name.data, form.email.data, form.message.data, form.validate(), form.errors
        msg = 'Youre message has not been sent'
        return render_template('about.html', form=form, msg=msg)


    return render_template('about.html', form=form)



if __name__ == '__main__':
    app.secret_key='secret123'
    app.run(debug=True)
    