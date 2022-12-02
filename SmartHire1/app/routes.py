from flask import render_template, url_for, flash, redirect, request, send_file
from app import app, db, bcrypt
import os
#from ResumeParser import getAllEmployees,DBConnect,getAllCandidates,getResumeLink
from app.ResumeParser import *
import secrets
from app.forms import RegistrationForm, LoginForm, ReviewForm, JobForm, ApplicationForm
from app.models import User, Jobs, Review, Application
from flask_login import login_user, current_user, logout_user, login_required
import random


rev = [
    {
        'username': 'SmartHire',
        'review': 'Hiring is Tedious but SmartHire makes it easy'
    },
    {
        'username': 'Hire Better for great business',
        'review': ''
    },
    {
        'username': 'SmartHire better decision',
        'review': ''
    }
]

db_recruit = DBConnect()
connection = db_recruit.connect()
cursor = db_recruit.get_cursor()

def parse_resume():
    resume_links = getResumeLink(cursor)
    downloadResumeFromS3(resume_links, connection, cursor)

    resume_links = getResumeLink(cursor)
    parseResume(resume_links, connection, cursor)

parse_resume()

# db.create_all()
# review = Review(username="John Doe",
#                     review="Needs improvement on basic coding concepts")
# db.session.add(review)
# db.session.commit()

Review_Obj = Review.query.all()
if len(Review_Obj) < 3:
    Random_Review = rev
else:
    Random_Review = random.sample(Review_Obj, 3)

@app.route("/")
@app.route("/home", methods=['GET', 'POST'])
def home():
    return render_template('layout.html', Random_Review=Random_Review)


@app.route("/resumeparse", methods=['GET', 'POST'])
def resumeparse():
    result = getAllEmployees(cursor)
    print(getAllCandidates(cursor))
    print(result)
    #employees = result.query.filter_by(Employee_Name=Employee_Name).all()
    return render_template('resumeparse.html', Random_Review=Random_Review)

def getRL():
    grl = getResumeLink(cursor)
    print(grl)
    #employees = result.query.filter_by(Employee_Name=Employee_Name).all()
    return render_template('resumeparse.html', Random_Review=Random_Review)

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        if current_user.usertype == 'Job Seeker':
            return redirect(url_for('show_jobs'))
        elif current_user.usertype == 'Company':
            return redirect(url_for('posted_jobs'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, usertype=form.usertype.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('You account has been created! You are now able to log in', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form, Random_Review=Random_Review)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        if current_user.usertype == 'Job Seeker':
            return redirect(url_for('show_jobs'))
        elif current_user.usertype == 'Company':
            return redirect(url_for('posted_jobs'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        print(user)
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            print('password clear')
            print(form.usertype.data)
            if form.usertype.data == user.usertype and form.usertype.data == 'Company':
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('show_jobs'))
                #redirect(url_for('show_jobs'))
            elif form.usertype.data == user.usertype and form.usertype.data == 'Job Seeker':
                login_user(user, remember=form.remember.data)
                next_page = request.args.get('next')
                return redirect(next_page) if next_page else redirect(url_for('show_jobs'))
                #redirect(url_for('show_jobs'))
            else:
                flash('Login Unsuccessful. Please check email, password and usertype', 'danger')
        else:
            flash('Login Unsuccessful. Please check email, password and usertype', 'danger')
            return render_template('login.html', form=form, Random_Review=Random_Review)
    return render_template('login.html', form=form, Random_Review=Random_Review)

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

def save_picture(form_picture):
    f_name, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = f_name + f_ext
    picture_path = os.path.join(app.root_path, 'static', picture_fn)
    form_picture.save(picture_path)
    return picture_fn

# Post CVs not required (NOTE)
# @app.route("/post_cvs/<jobid>", methods=['GET', 'POST'])
# @login_required
# def post_cvs(jobid):
#     form = ApplicationForm()
#     job = Jobs.query.filter_by(id=jobid).first()
#     if form.validate_on_submit():
#         application = Application(gender=form.gender.data,
#                               degree=form.degree.data,
#                               industry=form.industry.data,
#                               experience=form.experience.data,
#                               cover_letter=form.cover_letter.data,
#                               application_submiter=current_user,
#                               application_jober=job,
#                               cv=form.cv.data.filename)
#         print(form.cv.data)
#         picture_file = save_picture(form.cv.data)
#         db.session.add(application)
#         db.session.commit()
#         return redirect(url_for('show_jobs'))
#     return render_template('post_cvs.html', form=form, Random_Review=Random_Review)

@app.route("/post_jobs", methods=['GET', 'POST'])
@login_required
def post_jobs():
    form = JobForm()
    print(form)
    if form.validate_on_submit():
        insertOpenJobRole(
            connection=connection,
            cursor=cursor, 
            role_name=form.title.data,
            work_experience=form.work_experience.data,
            skillset=form.skillset.data,
            description=form.description.data)
        return redirect(url_for('posted_jobs'))
    print("Render", form.title, form.description, form.work_experience, form.skillset)
    return render_template('post_jobs.html', form=form, Random_Review=Random_Review)



@app.route("/review", methods=['GET', 'POST'])
@login_required
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        submitFeedback(
            cursor=cursor, 
            connection=connection,
            c_name=form.candidate_name.data,
            c_feedback=form.candidate_feedback.data,
            role_name=form.role_name.data
        )
        flash('Thank you for providing the review!', 'success')
        return redirect(url_for('show_jobs'))
    return  render_template('review.html', form=form, Random_Review=Random_Review)

@app.route("/show_feedback", methods=['GET', 'POST'])
@login_required
def show_feedback():
    feedback = getAllFeedback(cursor)
    print(feedback)
    return render_template('show_feedback.html', feedback=feedback, Random_Review=Random_Review)

@app.route("/posted_jobs")
@login_required
def posted_jobs():
    jobs = getOpenRoles(cursor)
    return render_template('show_jobs.html', jobs=jobs, Random_Review=Random_Review)


@app.route("/show_applications/<role_name>/", methods=['GET'])
@login_required
def show_applications(role_name):
    print("Show application", role_name)
    if current_user.usertype == "Company":
        candidates = getRelevantCandidates(connection=connection, cursor=cursor, role_name=role_name)
        print(candidates)

        return render_template('show_applications.html', applications=candidates, Random_Review=Random_Review, role_name=role_name)
    else:
        # TODO (Permission denied)
        pass


@app.route("/schedule_interview/<candidate_name>/<role_name>/<candidate_email>", methods=['GET'])
@login_required
def schedule_interview(candidate_name, role_name, candidate_email):
    print("Schedule interview: ", candidate_name, role_name, candidate_email)
    if current_user.usertype == "Company":
        interviewer = getMostRelevantInterviewer(cursor=cursor, role_name=role_name)
        print(interviewer)
        return render_template(
            'schedule_interview.html', 
            interviewer=interviewer, 
            candidate_name=candidate_name, 
            role_name=role_name, 
            candidate_email=candidate_email,
            Random_Review=Random_Review,
        )
    else:
        # TODO (Permission denied)
        pass

@app.route("/meeting/<application_id>")
@login_required
def meeting(application_id):
    applicant_id = Application.query.get(int(application_id)).user_id
    applicant = User.query.get(applicant_id)
    return render_template('meeting.html', applicant=applicant, Random_Review=Random_Review)

# @app.route("/resume_parse")
# @login_required
# def resume_parse():
#     data = resumeparse.read_file('C:\Users\pranu\OneDrive\Desktop\SmartHire\Resumes\data-scientist-resume-example')
#     return render_template('resumeparse.html', Random_Review=Random_Review)

#@app.route("/")
@app.route("/show_jobs")
def show_jobs():
    jobs = getOpenRoles(cursor)
    print(jobs)
    return render_template('show_jobs.html', jobs=jobs, Random_Review=Random_Review)


@app.route("/close_role/<role_name>")
def close_role(role_name):
    closeJobRole(cursor=cursor, connection=connection, role_name=role_name)
    return redirect(url_for('show_jobs'))
    

@app.route("/display_resume/<resume_path>", methods=['GET'])
def display_resume(resume_path):
    return render_template('resume.html', resume_path=resume_path, Random_Review=Random_Review)

@app.route("/resume/<candidate_name>", methods=['GET'])
def resume(candidate_name):
    print("Resume called: ", candidate_name)
    resume_path = getResumeLinkForCandidate(cursor=cursor, candidate_name=candidate_name)
    print("Path: ", resume_path)
    return redirect(f"/display_resume/{resume_path}")


@app.route("/candidates", methods=['GET', 'POST'])
@login_required
def candidates():
    if current_user.usertype == 'Company':
        result = getAllCandidates(cursor)
        print(result)
        candidates=result
        return render_template('candidates.html',candidates=candidates, Random_Review=Random_Review)
    else:
        pass

@app.route("/employees", methods=['GET', 'POST'])
@login_required
def employees():
    if current_user.usertype == 'Company':
        result = getAllEmployees(cursor)
        print(result)
        employees=result
        return render_template('employees.html',employees=employees, Random_Review=Random_Review)
    else:
        pass