from flask import Flask, render_template, abort

app = Flask(__name__)

posts = {
    1: {"title": "Welcome to My Blog", "content": "This is my first post on Flask!"},
    2: {"title": "Second Post", "content": "Another blog post powered by Flask."}
}

@app.route('/')
def home():
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = posts.get(post_id)
    if not post:
        abort(404)
    return render_template('post.html', post=post)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
