from flask import Flask, escape, request, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = '78dd78dad6a396a8175e8a508ec52100'

posts = [
    {
        'author': 'Will W',
        'title': 'blog post 1',
        'content': 'first post content',
        'date_posted': 'april 20, 2020'
    },

    {
        'author': 'Chris G',
        'title': 'blog post 12',
        'content': 'first post content',
        'date_posted': 'april 21, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():

    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('Login Successful', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful. Please check Username and Password', 'danger')

    return render_template('login.html', title='Login', form=form)



if __name__ == '__main__':
    app.run(debug=True)