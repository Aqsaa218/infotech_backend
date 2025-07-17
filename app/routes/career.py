from flask import Blueprint, request, jsonify
from app import db, mail
from app.model import Application
from app.util import save_file
from flask_mail import Message
import os

career_routes = Blueprint('career', __name__)

@career_routes.route('/apply', methods=['POST'])
def apply_job():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    position = request.form.get('position')
    message_text = request.form.get('message')
    resume = request.files.get('resume')

    if not all([name, email, phone, position, resume]):
        return jsonify({"error": "Missing fields"}), 400

    existing = Application.query.filter_by(email=email, position=position).first()
    if existing:
        return jsonify({"error": "Already applied for this position"}), 409

    filename = save_file(resume)
    filepath = os.path.join(os.getcwd(), 'uploads', filename)

    # Save to DB
    application = Application(
        name=name,
        email=email,
        phone=phone,
        position=position,
        message=message_text,
        resume_filename=filename
    )
    db.session.add(application)
    db.session.commit()

    # Send Email with Resume
    msg = Message(
        subject=f"New Job Application: {position}",
        recipients=['solutioninfotech76@gmail.com'],
        body=f"""
New job application submitted:

Name: {name}
Email: {email}
Phone: {phone}
Position: {position}
Message: {message_text}
        """
    )
    with open(filepath, 'rb') as fp:
        msg.attach(filename, 'application/pdf', fp.read())

    mail.send(msg)

    return jsonify({"message": "Application submitted and email sent!"}), 200
