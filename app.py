from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)


app.config['SECRET_KEY'] = '9418723401723742a2fe7af9ef6a66d7'


posts = [
    {
        'author': 'Basia Kowalska',
        'title': 'Serwus',
        'content': 'First post content',
        'date_posted': 'August 5, 2021'
    },
    {
        'author': 'Kasia Czarnecka',
        'title': 'Serwus 2',
        'content': 'Second post content',
        'date_posted': 'August 5, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title = 'About')

@app.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account createted for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title = 'Register', form=form)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@admin.com' and form.password.data == 'adminadmin':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unseccessful. Please check username and password', 'danger')
    return render_template('login.html', title = 'Sign In', form=form)

if __name__ == '__main__':
    app.run(debug=True)
