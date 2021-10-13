from market import app
from flask import render_template, redirect, url_for, flash, request
from market.models import Item, User
from market.forms import RegisterForm, LoginForm, PurchaseItemForm, SellItemForm

from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.exceptions import abort
from market import db
import sqlite3


#=================================================
try:
    connection = sqlite3.connect('database.db')
    cur = connection.cursor()

    cur.execute('''DROP TABLE IF EXISTS posts ''')

    cur.execute('''CREATE TABLE posts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
        title TEXT NOT NULL,
        content TEXT NOT NULL
    )''')



    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('First Post', 'Content for the first post')
                )

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('Second Post', 'Content for the second post')
                )
    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('third  Post', 'Content for the third  post')
                )

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('fourth  Post', 'Content for the fourth  post')
                )
    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('fifth  Post', 'Content for the fifth  post')
                )

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('sixth  Post', 'Content for the sixth  post')
                )
    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('seventh  Post', 'Content for the seventh post')
                )

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('eighth Post', 'Content for the eighth post')
                )
    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('ninth  Post', 'Content for the ninth post')
                )

    cur.execute("INSERT INTO posts (title, content) VALUES (?, ?)",
                ('tenth  Post', 'Content for the tenth  post')
                )
                

    connection.commit()
    connection.close()
except sqlite3.Error as error:
    print("Error while executing sqlite script", error)
#=================================================







def get_db_connection():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        print("Database created and Successfully Connected to SQLite")
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as error:
        print("Error while connecting to sqlite", error)


def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post




#@app.route('/')
#@app.route('/home')
#def home_page():
#    return render_template('home.html')


@app.route('/')
@app.route('/home')

def home_page():
    return render_template('home.html')

def hello():
    return 'Hello, World!'


@app.route('/index')
#@login_required
def index():

    conn = get_db_connection()
    posts_query = conn.execute("SELECT * FROM posts").fetchall()
    conn.close()
    return render_template('index.html', posts=posts_query)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)



#phan 1
@app.route('/create', methods=('GET', 'POST'))
@login_required
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO posts (title, content) VALUES (?, ?)',
                         (title, content))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
@login_required
def edit(id):
    post = get_post(id)

    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        if not title:
            flash('Title is required!')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE posts SET title = ?, content = ?'
                         ' WHERE id = ?',
                         (title, content, id))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))

    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    post = get_post(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM posts WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(post['title']))
    return redirect(url_for('index'))






 # phan 2   


@app.route('/register', methods=['GET', 'POST'])
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        user_to_create = User(username=form.username.data,
                              email_address=form.email_address.data,
                              password=form.password1.data)
        db.session.add(user_to_create)
        db.session.commit()
        login_user(user_to_create)
        flash(f"Account created successfully! You are now logged in as {user_to_create.username}", category='success')
        return redirect(url_for('index'))
    if form.errors != {}: #If there are not errors from the validations
        for err_msg in form.errors.values():
            flash(f'There was an error with creating a user: {err_msg}', category='danger')

    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        attempted_user = User.query.filter_by(username=form.username.data).first()
        if attempted_user and attempted_user.check_password_correction(
                attempted_password=form.password.data
        ):
            login_user(attempted_user)
            flash(f'Success! You are logged in as: {attempted_user.username}', category='success')
            return redirect(url_for('index'))
        else:
            flash('Username and password are not match! Please try again', category='danger')

    return render_template('login.html', form=form)

@app.route('/logout')
def logout_page():
    logout_user()
    flash("You have been logged out!", category='info')
    return redirect(url_for("home_page"))










