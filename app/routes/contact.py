from flask import Blueprint, request, jsonify
from app import db
from app.model import Contact
from app.util import save_file

contact_routes = Blueprint('contact', __name__)

@contact_routes.route('/contact', methods=['POST'])
def contact_form():
    tab = request.form.get('tab')  # 'cooperation' or 'career'

    if tab == 'cooperation':
        contact = Contact(
            tab='cooperation',
            company_email=request.form.get('companyEmail'),
            phone=request.form.get('phone'),
            project_details=request.form.get('projectDetails'),
            referral=request.form.get('referral')
        )
    elif tab == 'career':
        resume = request.files.get('resume')
        resume_filename = save_file(resume) if resume else None

        contact = Contact(
            tab='career',
            first_name=request.form.get('firstName'),
            last_name=request.form.get('lastName'),
            email=request.form.get('email'),
            phone=request.form.get('phone'),
            linked_in=request.form.get('linkedIn'),
            referral=request.form.get('referral'),
            resume_filename=resume_filename
        )
    else:
        return jsonify({"error": "Invalid tab selection"}), 400

    db.session.add(contact)
    db.session.commit()
    return jsonify({"message": "Form submitted successfully!"}), 200
