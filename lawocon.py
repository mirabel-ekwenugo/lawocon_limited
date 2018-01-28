from flask import Flask, render_template, url_for, request, flash
from forms import ContactForm
from flask_mail import Mail, Message

mail = Mail()
app = Flask(__name__)
app.secret_key = 'lawocon'

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'mirabelkoso@gmail.com'
app.config['MAIL_PASSWORD'] = 'divinemimi'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True

mail.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template("index.html")


@app.route('/contact-us', methods=['GET', 'POST'])
def contact_us():
    form = ContactForm()
    if request.method == 'POST':
        if form.validate() is False:
            flash('All fields are required.')
            return render_template('contact.html', form=form)
        else:
            msg = Message(form.subject.data, sender=form.email.data, recipients=['mirabelkoso@gmail.com'])
            msg.body = """
            From: %s <%s>
            %s
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)
    elif request.method == 'GET':
        return render_template('contact.html', form=form)


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/projects')
def project():
    return render_template("project.html")


@app.route('/blog')
def blog():
    return render_template("blog-grid.html")


if __name__ == '__main__':
    app.run()

# Contact Details
# Tel: +234 803 412 2200
# Tel: +234 805 669 1962
# Tel: +234 706 225 7846
# Email: Lawoconprojects@gmail.com
# Our Location
# 2nd Floor WAEC Building,
# 10 Zambezi Crescent,
# Maitama. Abuja
