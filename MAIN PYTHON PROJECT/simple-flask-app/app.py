from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'secret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:akul@localhost/malavika'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username_or_email = request.form['username_or_email']
        password = request.form['password']
        user = User.query.filter((User.username == username_or_email) | (User.email == username_or_email)).first()
        if user and user.check_password(password):
            flash('Login successful!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Invalid username/email or password', 'danger')
    else:
        get_flashed_messages()
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))

        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            flash('Username or Email already exists.', 'danger')
            return redirect(url_for('register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()
        flash('Account created successfully! Please log in.', 'success')
        return redirect(url_for('login'))
    return render_template('Register.html')

@app.route('/notebook.html')
def notebook():
    return render_template('Notebook.html')

@app.route('/journals.html')
def journals():
    return render_template('journals.html')

@app.route('/colour_pencils.html')
def colour_pencils():
    return render_template('colour_pencils.html')

@app.route('/sticky notes.html')
def sticky_notes():
    return render_template('Sticky notes.html')

@app.route('/notepads.html')
def notepads():
    return render_template('Notepads.html')

@app.route('/highlighters.html')
def highlighters():
    return render_template('Highlighters.html')

@app.route('/pencils.html')
def pencils():
    return render_template('Pencils.html')

@app.route('/pens.html')
def pens():
    return render_template('Pens.html')

@app.route('/erasers_and_correctors.html')
def erasers_and_correctors():
    return render_template('erasers_and_correctors.html')

@app.route('/paperclips.html')
def paperclips():
    return render_template('Paperclips.html')

@app.route('/WEBSITE.html')
def website():
    return render_template('WEBSITE.html')

searchable_items = [
    {"name": "Notebook", "url": "notebook"},
    {"name": "Journals", "url": "journals"},
    {"name": "Colour Pencils", "url": "colour_pencils"},
    {"name": "Sticky Notes", "url": "sticky_notes"},
    {"name": "Notepads", "url": "notepads"},
    {"name": "Highlighters", "url": "highlighters"},
    {"name": "Pencils", "url": "pencils"},
    {"name": "Pens", "url": "pens"},
    {"name": "Erasers and Correctors", "url": "erasers_and_correctors"},
    {"name": "Paperclips", "url": "paperclips"},
]

@app.route('/search')
def search():
    query = request.args.get('search')
    results = []
    if query:
        for item in searchable_items:
            if query.lower() in item['name'].lower():
                results.append(item)
    return render_template('search_results.html', query=query, results=results)


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)