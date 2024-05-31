from flask import Blueprint, render_template, url_for, send_file
from flask import request
from config.settings import db
from .get_data import db_resumes, db_skills, db_projects, db_informations
from .models import ContactMe

home_bp = Blueprint('home', __name__, template_folder='templates')


@home_bp.route('', methods=['GET', 'POST'])
def home():
    skills = db_skills()
    projects = db_projects()
    resumes = db_resumes()
    informations = db_informations()

    # get image urls from informations table
    image1 = informations.image1
    image2 = informations.image2
    image1_url = url_for('static', filename='images/profile/' + image1)
    image2_url = url_for('static', filename='images/profile/' + image2)

    if request.method == 'POST':

        name = request.form.get('name')
        email = request.form.get('email')
        subject = request.form.get('subject')
        message = request.form.get('message')

        if name and email and subject and message:
            new_contantme = ContactMe(name=name, email=email, subject=subject, message=message)
            db.session.add(new_contantme)
            db.session.commit()

    return render_template('index.html', skills=skills, projects=projects
                           , resumes=resumes, informations=informations, image1_url=image1_url, image2_url=image2_url)


@home_bp.route('/download_pdf')
def download_pdf():

    informations = db_informations()

    # Provide the path to PDF file
    file_name = informations.resume_file
    pdf_path = '../static/files/'+file_name

    return send_file(pdf_path, as_attachment=True)
