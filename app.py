from flask import Flask, request, render_template,  redirect, flash,  jsonify, session
from random import randint,  choice, sample
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

MOVIES = {'Amadeus', 'Chicken Run', 'Dances With Wolves'}
COMPLIMENTS = ['cool', 'clever', 'tenacious', 'awesome', 'handsome']


@app.route('/')
def home_page():
    """Shows home page"""
    session['fav_number'] = 42
    return render_template('home.html')


@app.route('/old-home-page')
def redirect_to_home():
    """Redirects to new home page"""
    flash('That page has moved!  This is our new home page!')
    return redirect("/")


@app.route('/movies')
def show_all_movies():
    """Show list of all movies in fake DB"""
    return render_template('movies.html', movies=MOVIES)


@app.route('/movies/json')
def get_movies_json():
    return jsonify(list(MOVIES))


@app.route('/movies/new', methods=["POST"])
def add_movie():
    title = request.form['title']
    # Add to pretend DB

    if title in MOVIES:
        flash('Movie Already Exists!', 'error')
    else:
        MOVIES.add(title)
        flash("Created Your Movie!", 'success')
    # import pdb
    # pdb.set_trace()
    return redirect('/movies')


@app.route('/form')
def show_form():
    """Shows form page"""
    return render_template('form.html')


@app.route('/greet')
def get_greeting():
    username = request.args['username']
    nice_thing = choice(COMPLIMENTS)
    return render_template("greet.html", username=username, compliment=nice_thing)


@app.route('/form-2')
def show_form_2():
    """Shows form-2 page"""
    return render_template('form_2.html')


@app.route('/greet-2')
def get_greeting_2():
    username = request.args['username']
    wants = request.args.get("wants_compliments")
    nice_things = sample(COMPLIMENTS, 3)
    return render_template("greet_2.html", username=username, wants_compliments=wants, compliments=nice_things)


@app.route('/lucky')
def lucky_number():
    """Shows lucky page"""
    num = randint(1, 10)
    return render_template('lucky.html', lucky_num=num, msg="You are so lucky!")


@app.route('/hello')
def say_hello():
    """Shows hello page"""
    # html = """
    # <html>
    #     <body>
    #         <h1>Hello, world! 🦝</h1>
    #         <p>This is the hello page</p>
    #     </body>
    # </html>
    # """
    # return html
    return render_template('hello.html')


@app.route('/goodbye')
def say_bye():
    """Shows goodbye page"""
    # html = """
    # <html>
    #     <body>
    #         <h1>Goodbye, world! 🦝</h1>
    #         <h2>👋🏻</h2>
    #     </body>
    # </html>
    # """
    # return html
    return render_template('goodbye.html')


@app.route('/spell/<word>')
def spell_word(word):
    """Shows spelling page"""
    caps_word = word.upper()
    return render_template('spell_word.html', word=caps_word)


@app.route('/search')
def search():
    # print (request.args)
    term = request.args["term"]
    sort = request.args["sort"]
    return f"<h1>Search Results For: {term}</h1><p>Sorting by: {sort}</p>"


@app.route('/add-comment')
def add_comment_form():
    """Show form for adding a comment"""
    return """
    <h1>Add Comment</h1>
    <form method="POST">
        <input type='text' placeholder='Comment' name='comment'/>
        <input type='text' placeholder='Username' name='username'/>
        <input type='password' placeholder='Password' name='password'/>
        <button>Submit</button>
    </form>
    """


@app.route('/add-comment', methods=['POST'])
def save_comment():
    """Handle adding comment"""
    comment = request.form["comment"]
    username = request.form["username"]
    password = request.form["password"]
    print(request.form)
    return f"""
        <h1> SAVED YOUR COMMENT</h1>
        <ul>
            <li>Username: {username}</li>
            <li>Comment: {comment}</li>
        </ul>
    """


@app.route('/r/<subreddit>')
def show_subreddit(subreddit):
    return f"<h1>YOU ARE BROWSING THE {subreddit} SUBREDDIT</h1>"


@app.route('/r/<subreddit>/comments/<int:post_id>')
def show_comments(subreddit, post_id):
    return f"<h1>VIEWING COMMENTS FOR POST WITH ID: {post_id}</h1> <h2>FROM THE {subreddit} SUBREDDIT</h2>"


POSTS = {
    1: "<h1>I like chicken tenders</h1>",
    2: "<h1>I hate mayo</h1>",
    3: "<h1>Double rainbow all the way</h1>",
    4: "<h1>YOLO OMG (kill me)</h1>"
}

SUBREDDIT = {
    1: "<h1>SAMMY</h1>",
    2: "<h1>MAPACHITO</h1>",
    3: "<h1>WOT</h1>",
    4: "<h1>CHANCLAS</h1>"
}


@app.route('/posts/<int:id>')
def find_comment(id):
    # post = POSTS[id]
    post = POSTS.get(id, "<h1>REEEE Error: Post not found</h1>")
    return f"<p>{post}</p>"


# @app.route('/sr/<id>')
# def find_subreddit(id):
#     # post = POSTS[id]
#     subreddit = SUBREDDIT.get(id, "<h1>REEEE Error: Subreddit not found</h1>")
#     return f"<p>{subreddit}</p>"
