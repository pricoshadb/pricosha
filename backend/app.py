from flask import Flask, session, request, jsonify, make_response, render_template, send_file, g
from flask_cors import CORS, cross_origin
import os.path
from helpers.util import response
import helpers.helpers as helpers
import json

'''
Full documentation: https://pricoshaapi.drew.hu
Optional features:

Paginated results
User avatar?


'''
# Initialize Flask app
app = Flask(__name__,
            static_folder="./dist/static",
            template_folder="./dist")

# Set secret key for sessions
app.secret_key = 'super secret key!98nu9f8u2f'
app.config['UPLOAD_FOLDER'] = '/home/user/pricosha/backend/img'

# Allow all clients to access our api
CORS(app, resources={r"/*": {"origins": '*'}}, supports_credentials=True)

@app.before_request
def before_request():
    g.connection = helpers.connect_db()

@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'connection'):
        g.connection.close()


@app.route('/')
def index():
    return render_template('index.html')


# API Documentation
@app.route('/api')
def docs():
    return render_template('api.html')

@app.route('/favicon.ico')
def favicon():
    return send_file('img/favicon.ico')


# 2. Login - POST email and password
# + Optional feature 1: User avatar. Avatar is url to static image. Avatars are public so no need to make private
# Tested WORKING on 12/4
@app.route('/login', methods=['POST'])
@cross_origin(supports_credentials=True)
def login():
    auth = request.authorization

    # Get info from request
    email = auth.username
    password = auth.password

    # Attempt login
    login_ = helpers.get_login(email, password)

    if login_['success']:
        user = login_['response']
        session['email'] = user['email']
        session['first_name'], session['last_name'] = user['first_name'], user['last_name']
        session['avatar'] = user['avatar']
        session.modified = True
        return response(True, f"successfully logged in {session['first_name']} {session['last_name']}")
    else:
        return response(False, 'Login failed')


# Logs out user
# Tested WORKING on 12/4
@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('email', None)
    return response(True, 'Logged out')


# Registers new user
@app.route('/register', methods=['POST'])
def register():
    req = request.get_json()
    auth = request.authorization
    new_user = helpers.register(auth['username'], auth['password'], req['first_name'], req['last_name'])
    return response(new_user['success'], new_user['response'])

# Resets user password
@app.route('/reset_password', methods=['POST'])
def reset_password():
    req = request.get_json()
    pw_reset = helpers.reset_password(session['email'], req['old_password'], req['new_password'])
    return response(True, pw_reset)


# 1. View public content posted in the last 24 hours
# + Optional feature 5: Paginated results
# Tested WORKING on 12/4
@app.route('/posts/public')
def public_content():
    req = request.args
    page = int(req.get('page', 1))
    results_per_page = int(req.get('results_per_page', 10))
    content = helpers.get_public_content(page, results_per_page)
    return response(True, content)


@app.route('/post')
def get_post():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.args
    post = helpers.get_post(req['item_id'])
    return response(True, post)


# 5. Post a content item
# Optional feature 4: Post image content
# Tested WORKING on 12/4
@app.route('/post/create', methods=['POST'])
def create_post():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    email = session['email']
    data = json.loads(request.form['data'])
    item_name = data['item_name']
    is_pub = data['is_pub']
    filepath = None
    if 'file' in request.files:
        file = request.files['file']
        if file.filename == '':
            return response(True, 'empty filename')
        filepath = os.path.join('/home/user/pricosha/backend/img/', file.filename)
        file.save(filepath)
    result = helpers.create_content_item(email,item_name,is_pub,filepath)
    return response(True, result)


# 3. View shared content items and info about them
# + Optional feature 5: Paginated results
# Tested WORKING on 12/4
@app.route('/posts/shared')
def get_shared_content():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.args
    email = session['email']
    page = int(req.get('page', 1))
    results_per_page = int(req.get('results_per_page',10))
    content = helpers.get_shared_content(email, page=page, results_per_page=results_per_page)
    return response(True, content)


# Optional feature 3: Saved posts. Gets post that user has saved
# + Optional feature 5: Paginated results
# Tested WORKING on 12/4
@app.route('/posts/saved')
def get_saved_posts():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.args
    email = session['email']
    page = int(req.get('page', 1))
    results_per_page = int(req.get('results_per_page', 10))
    saved_posts = helpers.get_saved_posts(email=email, page=page, results_per_page=results_per_page)
    return response(True, saved_posts)


# Tested WORKING on 12/4
@app.route('/post/save', methods=['POST'])
def save_post():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    email = session['email']
    item_id = req['item_id']
    helpers.save_post(email, item_id)
    return 'ok'


# Tested WORKING on 12/4
@app.route('/post/unsave', methods=['POST'])
def unsave_post():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    email = session['email']
    item_id = req['item_id']
    helpers.unsave_post(email, item_id)
    return 'ok'


@app.route('/rate', methods=['POST'])
def rate_content_item():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    email = session['email']
    emoji = req['emoji']
    item_id = req['item_id']
    helpers.rate_post(email, item_id, emoji)
    return "ok"

@app.route('/ratings')
def ratings_content_item():
    req = request.args
    email = ''
    if 'email' in session:
        email = session['email']
    item_id = req['item_id']
    resp = helpers.post_ratings(email, item_id)
    return response(resp[0], resp[1])


# 6. Tag a content item
# Tested WORKING on 12/4
@app.route('/tags/create', methods=['POST'])
def tag_content_item():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    current_user = session['email']
    tagee_email = req['tagee_email']
    item_id = req['item_id']
    tag_item = helpers.tag_item(current_user, tagee_email,item_id)
    return response(True, tag_item)

# 4. Manage tags
# 4a. Get proposed tags e.g. where tagee is user and status is false
# Tested WORKING on 12/4
@app.route('/tags/proposed')
def get_proposed_tags():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.args
    email = session['email']
    page = req.get('page',1)
    results_per_page = req.get('results_per_page',10)
    proposed_tags = helpers.get_proposed_tags(email, page=page, results_per_page=results_per_page)
    return response(True, proposed_tags)

# 4b. Modify proposed tag
# Tested WORKING on 12/4
@app.route('/tags/modify', methods=['POST'])
def tags_modify():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    email_tagger = req['email_tagger']
    email_tagged = session['email']
    item_id = req['item_id']
    decision = req['decision']
    result = helpers.modify_proposed_tag(email_tagger, email_tagged, item_id, decision)
    return response(True, result)

# 7. Adds friend to friendgroup that person owns
# Tested WORKING on 12/4
@app.route('/group/members/add', methods=['POST'])
def add_friend():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    email_owner = session['email']
    email_member = req['email']
    fg_name = req['fg_name']
    friend = helpers.add_member(email_owner, email_member, fg_name)
    return response(friend[0], friend[1])

@app.route('/group/members/remove', methods=['POST'])
def remove_friend():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    email_owner = session['email']
    email_member = req['email']
    fg_name = req['fg_name']
    unfriend = helpers.remove_member(email_owner, email_member, fg_name)
    return response(True, unfriend)


@app.route('/group/create', methods=['POST'])
def create_group():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    email_owner = session['email']
    fg_name = req['fg_name']
    description = None #req.get('description', None)
    fg = helpers.create_group(email_owner, fg_name, description)
    return response(True, fg)

@app.route('/group/remove', methods=['POST'])
def remove_group():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    email_owner = session['email']
    fg_name = req['fg_name']
    fg = helpers.remove_group(email_owner, fg_name)
    return response(True, fg)


@app.route('/groups')
def get_groups():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.args
    names_only = 'true' == req.get('names_only', False)
    email_owner = session['email']
    fg = helpers.get_groups(email_owner, names_only)
    return response(True, fg)


# Optional feature 2: Profile pages
# Profile info is always public
@app.route('/profile')
def get_profile_info():
    # return:
    # user: {
    #   bio: '',
    #   avatar: '',
    #   first_name: '',
    #   last_name: '',
    #   friend: false,
    # }
    req = request.args
    email_other = req['email']
    email = ''
    if 'email' in session:
        email = session['email']
    profile_info = helpers.get_profile_info(email, email_other)
    return response(True, profile_info)


@app.route('/set_profile_bio', methods=['POST'])
def set_profile_bio():
    req = request.get_json()
    email = session['email']
    new_bio = req.get('new_bio')
    profile_info = helpers.set_profile_bio(email,new_bio)
    return response(True, profile_info)


@app.route('/set_profile_avatar', methods=['POST'])
def set_profile_avatar():
    email = session['email']
    new_avatar = request.form.get('new_avatar')
    profile_info = helpers.set_profile_avatar(email, new_avatar)
    return response(True, profile_info)




# Optional feature 6: Add comments
# Tested WORKING on 12/4
@app.route('/comments/post', methods=['POST'])
def post_comment():
    if 'email' not in session:
        return response(False, 'User not logged in')
    email = session['email']
    req = request.get_json()
    item_id = req['item_id']
    comment = req['comment']
    new_comment = helpers.post_comment(email, item_id, comment)
    return response(True, new_comment)


@app.route('/comments')
def get_comments():
    req = request.args
    email = None
    if 'email' in session:
        email = session['email']
    item_id = req['item_id']
    comments = helpers.get_comments(email, item_id)
    return response(comments[0], comments[1])


# deletes comment if user wrote comment or if user owns post
@app.route('/comments/delete', methods=['POST'])
def delete_comment():
    req = request.get_json()
    email = session['email']
    item_id = req['item_id']
    comment_id = req['comment_id']


@app.route('/friends')
def get_friends():
    if 'email' not in session:
        return response(False, 'User not logged in')
    email = session['email']
    friends = helpers.get_friends(email)
    return response(True, friends)


@app.route('/friend', methods=['POST'])
def friend():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    email = session['email']
    email_other = req['email']
    friends = helpers.add_friend(email, email_other)
    return response(True, friends)


@app.route('/unfriend', methods=['POST'])
def unfriend():
    if 'email' not in session:
        return response(False, 'User not logged in')
    req = request.get_json()
    email = session['email']
    email_other = req['email']
    friends = helpers.remove_friend(email, email_other)
    return response(True, friends)


@app.route("/img/<path:path>")
def images(path):
    import os.path
    full_path = "./img/" + path
    if not os.path.exists(full_path):
        return response(True, 'Image not found on this server')
    b = open(full_path, 'rb').read()
    resp = make_response(b)
    resp.content_type = "image/jpeg"
    return resp
