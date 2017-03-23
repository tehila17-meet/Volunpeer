from flask import *
from flask import session as login_session
from database import *
from werkzeug.utils import secure_filename
import os


app= Flask(__name__)
app.secret_key = "MY_SUPER_SECRET_KEY"
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
UPLOAD_FOLDER = 'static\images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/login' , methods=['GET','POST'])
def login():
    if(request.method=='GET'):
        return render_template('login.html')
    return render_template('placesToVolunteer.html')
@app.route('/signup')
def signup():
    return render_template('signup.html')
@app.route('/place')
def place():
    return render_template('place.html')
@app.route('/placesToVolunteer')
def placesToVolunteer():
    return render_template('placesToVolunteer.html')
@app.route('/volunteer')
def volunteer():
    return render_template('volunteer.html')
@app.route('/logout')
def logout():
    return render_template('login.html')
if __name__== '__main__' :
    app.run(debug=True)