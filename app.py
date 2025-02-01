from  flask import Flask,render_template,redirect,flash,url_for
from forms import RegistrationForm ,LoginForm
app = Flask(__name__)
app.config['SECRET_KEY'] ='c065d0cda42a6b418420d984d14bda2f'

posts= [
    {
        "author": "Mithilesh",
        'title': "blog post 1",
        'content': "First Post content",
        'date_posted': "January 30,2025"
    },
    {
        "author": "Tejas",
        'title': "blog post 2",
        'content': "Second Post content",
        'date_posted': "January 31,2025"
    },
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('aboutus.html',title="About us")

@app.route("/contact")
def contact():
    return render_template('contactus.html',title="Contact us")

@app.route("/register",methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}','success')
        return redirect(url_for('home'))
    return render_template('register.html',title = "Registration",form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title="Login", form=form)

if __name__ =="__main__":
    app.run(debug=True)