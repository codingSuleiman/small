from flask import Flask
from flask import render_template, url_for, flash, redirect, session, request, abort
from form import PostForm, TotalPost

app = Flask(__name__)
app.config['SECRET_KEY'] = '5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8'


@app.route('/', methods=['POST', 'GET'])
def home():
    form = PostForm()
    posts = TotalPost()
    if form.validate_on_submit():
        posts.total_posts.append(form.content.data)
        return redirect(url_for('home'))
    return render_template('index.html', form=form, posts=posts.total_posts[::-1])