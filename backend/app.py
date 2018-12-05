from flask import Flask, session, request, jsonify, make_response, redirect
from flask_cors import CORS
import helpers

# Initialize Flask app
app = Flask(__name__)

# Set secret key for sessions
app.secret_key = 'super secret key!98nu9f8u2f'

# Allow all clients to access our api
CORS(app, resources={r"/*": {"origins": '*'}})


# Test route
@app.route('/', methods=['GET'])
def index():
    return jsonify('ok')


# 1. View public content posted in the last 24 hours
# 3. View shared content items and info about them
# + Optional feature 5: Paginated results
@app.route('/login/', methods=['POST'])
def login():
    # Get info from request
    email = request.form['email']
    password = request.form['password']

    # Attempt login
    user = helpers.get_login(email, password)

    if login:
        session['email'] = user['email']
        session['first_name'], session['last_name'] = user['first_name'], user['last_name']
        session['avatar'] = user['avatar']
        return jsonify(f"successfully logged in {session['first_name']} {session['last_name']}")
    else:
        return jsonify('login failed')


# 2. Login - POST email and password
@app.route('/posts/<channel>', methods=['GET', 'POST'])
def get_posts(channel):
    page = int(request.args.get('page', 1))
    results_per_page = int(request.args.get('results_per_page', 10))
    if channel == 'shared':
        if 'email' not in session:
            return 'Unauthorized', 400
        email = session['email']
        content = helpers.get_shared_content(email, page, results_per_page)
    elif channel == 'public':
        content = helpers.get_public_content(page=page, results_per_page=results_per_page)
    else:
        return redirect('/posts/public')
    return jsonify(content)
# + Optional feature 1: User avatar. Avatar is url to static image. Avatars are public so no need to make private


@app.route('/logout/')
def logout():
    # remove the username from the session if it's there
    session.pop('email', None)
    return jsonify('logged out')


# 4. Manage tags
# 4a. Get proposed tags e.g. where tagee is user and status is false
# Tested WORKING on 12/4
@app.route('/get_proposed_tags')
def get_proposed_tags():
    email = session['email']
    proposed_tags = helpers.get_proposed_tags(email)
    return jsonify(proposed_tags)


# 4b. Modify proposed tag
# Tested WORKING on 12/4
@app.route('/modify_proposed_tag', methods=['POST'])
def modify_proposed_tag():
    email_tagger = request.form['email_tagger']
    email_tagged = session['email']
    item_id = request.form['item_id']
    decision = request.form['decision']
    helpers.modify_proposed_tag(email_tagger, email_tagged, item_id, decision)
    return 'ok'


# 5. Post a content item
# Optional feature 4: Post image content
# Tested WORKING on 12/4
@app.route('/post_content_item', methods=['POST'])
def post_content_item():
    if not session['email']:
        return jsonify('User not logged in')
    email = session['email']
    item_name = request.form['item_name']
    is_pub = request.form['is_pub']
    image_content = request.form.get('image_content', None)
    helpers.create_content_item(email,item_name,is_pub,image_content)
    return 'ok'


# 6. Tag a content item
# Tested WORKING on 12/4
@app.route('/tag_content_item', methods=['POST'])
def tag_content_item():
    current_user = session['email']
    tagee_email = request.form['tagee_email']
    item_id = request.form['item_id']
    helpers.tag_item(current_user,tagee_email,item_id)
    return 'ok'


# 7. Adds friend to friendgroup that person owns
# Tested WORKING on 12/4
@app.route('/add_friend', methods=['POST'])
def add_friend():
    owner_email = session['email']
    fg_name = request.form['fg_name']
    friend_fname, friend_lname = request.form['friend_fname'], request.form['friend_lname']

    return jsonify(helpers.add_friend(owner_email, fg_name, friend_fname, friend_lname))



# Optional feature 2: Profile pages
@app.route('/get_profile_info')
def profile_info():
    pass


# Optional feature 3: Saved posts. Gets post that user has saved
# + Optional feature 5: Paginated results
# Tested WORKING on 12/4
@app.route('/get_saved_posts')
def get_saved_posts():
    email = session['email']
    page = request.form.get('page',1)
    results_per_page = request.form.get('results_per_page',10)
    saved_posts = helpers.get_saved_posts(email=email, page=page, results_per_page=results_per_page)
    return jsonify(saved_posts)


# Tested WORKING on 12/4
@app.route('/save_post', methods=['POST'])
def save_post():
    email = session['email']
    item_id = request.form['item_id']
    helpers.save_post(email, item_id)
    return 'ok'


# Tested WORKING on 12/4
@app.route('/unsave_post', methods=['POST'])
def unsave_post():
    email = session['email']
    item_id = request.form['item_id']
    helpers.unsave_post(email, item_id)
    return 'ok'

# Optional feature 6: Add comments
# Tested WORKING on 12/4
@app.route('/post_comment', methods=['POST'])
def post_comment():
    email = session['email']
    item_id = request.form['item_id']
    comment = request.form['comment']
    helpers.post_comment(email, item_id, comment)
    return 'ok'


@app.route("/img/<path:path>")
def images(path):
    full_path = "./img/" + path
    b = open(full_path, 'rb').read()
    resp = make_response(b)
    resp.content_type = "image/jpeg"
    return resp
