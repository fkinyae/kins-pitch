from flask import render_template,request,url_for,abort,redirect
from . import main
from flask_login import login_required, current_user
from ..models import User,Role,Categories,Pitches
from .forms import UpdateProfile,PitchForm
from .. import db,photos
import markdown2


@main.route('/')
def index():
    
    categories = Categories.query.all()
    
    return render_template('index.html',categories = categories)

@main.route('/pitch/<int:id>')
def pitch(id):
        category = Categories.query.filter_by(id=id).first().id
        title =Categories.query.filter_by(id=id).first().category
        pitches = Pitches.get_pitch(category)
        
        return render_template('index.html',title=title,category=category,pitches=pitches)

    

@main.route('/pitch/new/<int:id>', methods=['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
    cat = Categories.query.filter_by(id=id).first().id
    
    if form.validate_on_submit():
        pitch = form.pitch.data
        category_id = Categories.query.filter_by(id=id).first().id

        
        new_pitch = Pitches(pitch=pitch, category_id=category_id)
        
        db.session.add(new_pitch)
        db.session.commit()
        return redirect(url_for('main.index'))
    
    return render_template('new_pitch.html', pitch_form=form)

@main.route('/<int:id>')
def single_pitch(id):
    pitch=Pitches.query.get(id)
    if pitch is None:
        abort(404)
    format_pitch = markdown2.markdown(pitch.pitch,extras=["code-friendly", "fenced-code-blocks"])    
    return render_template('index.html',pitch = pitch, format_pitch=format_pitch)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username=uname).first()
    
    if user is None:
        abort(404)
        
    return render_template("profile/profile.html", user=user)    

@main.route('/user/<uname>/update',methods=['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username=uname).first()
    if user is None:
        abort(404)
        
    form = UpdateProfile()
    
    if form.validate_on_submit():
        user.bio = form.bio.data
        
        db.session.add(user)
        db.session.commit()
        
        return redirect(url_for('.profile', uname=user.username))
    
    return render_template('profile/update.html',form=form)    

@main.route('/user/<uname>/update/pic', methods=['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    