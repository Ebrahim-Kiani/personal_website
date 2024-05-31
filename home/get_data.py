import os

from flask import url_for

from .models import Skill, Project, Resume, Information


def db_skills():
    skills = Skill.query.all()
    return skills


def db_projects():
    projects = Project.query.all()
    return projects


def db_resumes():
    resumes = Resume.query.all()
    return resumes


def db_informations():
    information = Information.query.filter(Information.user.has(is_admin=True)).first()
    return information
