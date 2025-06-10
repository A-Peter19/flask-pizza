from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    # Looks for template
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/user/<name>')
def user(name):
    # passes the name variable into the user.html template.
    return render_template('user.html', name=name)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/posts')
def posts():
    sample_posts = [
        {'title': 'Day 1!', 'body': 'This is my first post.'},
        {'title': 'Another update', 'body': 'More content coming.'}
    ]
    # This renders a template that shows your posts.
    return render_template('posts.html', posts=sample_posts)

@app.route('/submit', methods=['POST'])
def submit():
    # this grabs the data from the form : the username inputted.
    username = request.form.get('username')
    if not username:
        # If no name is provided, redirect the user back to the form.
        return redirect(url_for('form'))
    # otherwise show thank you page.
    return render_template('thankyou.html', name=username)

@app.context_processor
def inject_current_year():
    return {'current_year': datetime.gmtnow().year}

if __name__ == '__main__':
    app.run(debug=True)


