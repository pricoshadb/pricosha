from flask import Flask, session, request, jsonify, make_response, render_template, send_file
from flask_cors import CORS
import helpers


'''
Full documentation: https://pricoshaapi.drew.hu
Optional features:

Paginated results
User avatar?


'''
# Initialize Flask app
app = Flask(__name__)

# Set secret key for sessions
app.secret_key = 'super secret key!98nu9f8u2f'

# Allow all clients to access our api
CORS(app, resources={r"/*": {"origins": '*'}})


# API Documentation
@app.route('/')
def index():
    return render_template('api.html')

@app.route('/favicon.ico')
def favicon():
    return send_file('img/favicon.ico')


# 1. View public content posted in the last 24 hours
# + Optional feature 5: Paginated results
# Tested WORKING on 12/4
@app.route('/public_content')
def public_content():
    page = int(request.form.get('page',1))
    results_per_page = int(request.form.get('results_per_page',10))
    content = helpers.get_public_content(page,results_per_page)
    return jsonify(content)


# 2. Login - POST email and password
# + Optional feature 1: User avatar. Avatar is url to static image. Avatars are public so no need to make private
# Tested WORKING on 12/4
@app.route('/login', methods=['POST'])
def login():
    # Get info from request
    email = request.form['email']
    password = request.form['password']

    # Attempt login
    user = helpers.get_login(email, password)

    if login['success']:
        session['email'] = user['email']
        session['first_name'], session['last_name'] = user['first_name'], user['last_name']
        session['avatar'] = user['avatar']
        return jsonify(f"successfully logged in {session['first_name']} {session['last_name']}")
    else:
        return jsonify('login failed')


# Logs out user
# Tested WORKING on 12/4
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('email', None)
    return jsonify('logged out')


# Registers new user
@app.route('/register', methods=['POST'])
def register():
    email = request.form['email']
    password = request.form['password']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    new_user = helpers.register(email, password, first_name, last_name)
    return jsonify(new_user)

# Resets user password
@app.route('/reset_password', methods=['POST'])
def reset_password():
    email = session['email']
    old_password = request.form['old_password']
    new_password = request.form['new_password']
    pw_reset = helpers.reset_password(email, old_password, new_password)
    return jsonify(pw_reset)


# 3. View shared content items and info about them
# + Optional feature 5: Paginated results
# Tested WORKING on 12/4
@app.route('/get_shared_content')
def get_shared_content():
    if 'email' not in session:
        return 'User not logged in'
    email = session['email']
    page = request.form.get('page',1)
    results_per_page = request.form.get('results_per_page',10)
    content = helpers.get_shared_content(email, page=page, results_per_page=results_per_page)
    return jsonify(content)


# 4. Manage tags
# 4a. Get proposed tags e.g. where tagee is user and status is false
# Tested WORKING on 12/4
@app.route('/get_proposed_tags')
def get_proposed_tags():
    if 'email' not in session:
        return 'User not logged in'
    email = session['email']
    page = request.form.get('page',1)
    results_per_page = request.form.get('results_per_page',10)
    proposed_tags = helpers.get_proposed_tags(email, page=page, results_per_page=results_per_page)
    return jsonify(proposed_tags)

# 4b. Modify proposed tag
# Tested WORKING on 12/4
@app.route('/modify_proposed_tag', methods=['POST'])
def modify_proposed_tag():
    if 'email' not in session:
        return 'User not logged in'
    email_tagger = request.form['email_tagger']
    email_tagged = session['email']
    item_id = request.form['item_id']
    decision = request.form['decision']
    result = helpers.modify_proposed_tag(email_tagger, email_tagged, item_id, decision)
    return jsonify(result)


# 5. Post a content item
# Optional feature 4: Post image content
# Tested WORKING on 12/4
@app.route('/post_content_item', methods=['POST'])
def post_content_item():
    if 'email' not in session:
        return 'User not logged in'
    email = session['email']
    item_name = request.form['item_name']
    is_pub = request.form['is_pub']
    image_content = request.form.get('image_content', None)
    result = helpers.create_content_item(email,item_name,is_pub,image_content)
    return jsonify(result)


# 6. Tag a content item
# Tested WORKING on 12/4
@app.route('/tag_content_item', methods=['POST'])
def tag_content_item():
    if 'email' not in session:
        return 'User not logged in'
    current_user = session['email']
    tagee_email = request.form['tagee_email']
    item_id = request.form['item_id']
    helpers.tag_item(current_user,tagee_email,item_id)
    return 'ok'


# 7. Adds friend to friendgroup that person owns
# Tested WORKING on 12/4
@app.route('/add_friend', methods=['POST'])
def add_friend():
    if 'email' not in session:
        return 'User not logged in'
    owner_email = session['email']
    fg_name = request.form['fg_name']
    friend_fname, friend_lname = request.form['friend_fname'], request.form['friend_lname']

    return jsonify(helpers.add_friend(owner_email, fg_name, friend_fname, friend_lname))



# Optional feature 2: Profile pages
# Profile info is always public
@app.route('/get_profile_info')
def get_profile_info():
    email = request.form.get('email', session['email'])
    profile_info = helpers.get_profile_info(email)
    return jsonify(profile_info)


@app.route('/set_profile_bio')
def set_profile_bio():
    email = session['email']
    new_bio = request.form.get('new_bio')
    profile_info = helpers.set_profile_bio(email,new_bio)
    return jsonify(profile_info)


@app.route('/set_profile_avatar')
def set_profile_avatar():
    email = session['email']
    new_avatar = request.form.get('new_avatar')
    profile_info = helpers.set_profile_avatar(email, new_avatar)
    return jsonify(profile_info)


# Optional feature 3: Saved posts. Gets post that user has saved
# + Optional feature 5: Paginated results
# Tested WORKING on 12/4
@app.route('/get_saved_posts')
def get_saved_posts():
    if 'email' not in session:
        return 'User not logged in'
    email = session['email']
    page = request.form.get('page',1)
    results_per_page = request.form.get('results_per_page',10)
    saved_posts = helpers.get_saved_posts(email=email, page=page, results_per_page=results_per_page)
    return jsonify(saved_posts)


# Tested WORKING on 12/4
@app.route('/save_post', methods=['POST'])
def save_post():
    if 'email' not in session:
        return 'User not logged in'
    email = session['email']
    item_id = request.form['item_id']
    helpers.save_post(email, item_id)
    return 'ok'


# Tested WORKING on 12/4
@app.route('/unsave_post', methods=['POST'])
def unsave_post():
    if 'email' not in session:
        return 'User not logged in'
    email = session['email']
    item_id = request.form['item_id']
    helpers.unsave_post(email, item_id)
    return 'ok'

# Optional feature 6: Add comments
# Tested WORKING on 12/4
@app.route('/post_comment', methods=['POST'])
def post_comment():
    if 'email' not in session:
        return 'User not logged in'
    email = session['email']
    item_id = request.form['item_id']
    comment = request.form['comment']
    helpers.post_comment(email, item_id, comment)
    return 'ok'


@app.route('/get_comments')
def get_comments():
    email = session['email']
    item_id = request.form['item_id']
    comments = helpers.get_comments(email, item_id)
    return jsonify(comments)


# deletes comment if user
@app.route('/delete_comment', methods=['POST'])
def delete_comment():
    email = session['email']
    item_id = request.form['item_id']
    comment_id = request.form['comment_id']


@app.route("/img/<path:path>")
def images(path):
    import os.path
    full_path = "./img/" + path
    if not os.path.exists(full_path):
        return jsonify('Image not found on this server')
    b = open(full_path, 'rb').read()
    resp = make_response(b)
    resp.content_type = "image/jpeg"
    return resp
