from flask import Blueprint, request, jsonify
from app import db
from app.model import Application
from app.util import save_file

career_routes = Blueprint('career', __name__)


@career_routes.route('/apply', methods=['POST'])
def apply_job():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    position = request.form.get('position')
    message = request.form.get('message')
    resume = request.files.get('resume')

    if not all([name, email, phone, position, resume]):
        return jsonify({"error": "Missing fields"}), 400

    existing = Application.query.filter_by(email=email, position=position).first()
    if existing:
        return jsonify({"error": "Already applied for this position"}), 409

    filename = save_file(resume)

    application = Application(
        name=name,
        email=email,
        phone=phone,
        position=position,
        message=message,
        resume_filename=filename
    )
    db.session.add(application)
    db.session.commit()

    return jsonify({"message": "Application submitted!"}), 200
