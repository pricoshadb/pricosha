from flask import Flask, session, request, jsonify, make_response
from flask_cors import CORS
import helpers

# Initialize Flask app
app = Flask(__name__)

# Set secret key for sessions
app.secret_key = 'super secret key!98nu9f8u2f'

# Allow all clients to access our api
CORS(app, resources={r"/*": {"origins": '*'}})


# Test route
@app.route('/')
def index():
    return jsonify('ok')


# 1. View public content posted in the last 24 hours
# + Optional feature 5: Paginated results
@app.route('/public_content/', methods=['GET', 'POST'])
def public_content():
    page = int(request.args.get('page',None))
    results_per_page = int(request.args.get('results_per_page',10))
    content = helpers.get_public_content(page=page,results_per_page=results_per_page)
    return jsonify(content)


# 2. Login - POST email and password
# + Optional feature 1: User avatar. Avatar is url to static image. Avatars are public so no need to make private
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


@app.route('/logout/')
def logout():
    # remove the username from the session if it's there
    session.pop('email', None)
    return jsonify('logged out')


# 3. View shared content items and info about them
# + Optional feature 5: Paginated results
@app.route('/get_shared_content')
def get_shared_content():
    email = session['email']


# 4. Manage tags
@app.route('/get_proposed_tags')
def get_proposed_tags():
    pass


# 5. Post a content item
# Optional feature 4: Post image content
@app.route('/post_content_item')
def post_content_item():
    if not session['email']:
        return jsonify('User not logged in')
    email = session['email']
    item_name = request.form['item_name']
    is_pub = request.form['is_pub']
    if 'image_content' in request.form:
        image_content = request.form['image_content']



# 6. Tag a content item
@app.route('/tag_content_item', methods=['POST'])
def tag_content_item():
    pass


# 7. Add friend
@app.route('/add_friend', methods=['POST'])
def add_friend():
    friend_group = request.form['friend_group']
    first_name, last_name = request.form['first_name'], request.form['last_name']

# Optional feature 2: Profile pages
@app.route('/get_profile_info')
def profile_info():
    pass

# Optional feature 3: Saved posts
# + Optional feature 5: Paginated results
@app.route('/get_saved_posts')
def get_saved_posts():
    pass

# Optional feature 6: Add comments
@app.route('/post_comment')
def post_comment():
    pass

@app.route("/img/<path:path>")
def images(path):
    full_path = "./img/" + path
    b = open(full_path, 'rb').read()
    resp = make_response(b)
    resp.content_type = "image/jpeg"
    return resp
