from . import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    position = db.Column(db.String(120))
    message = db.Column(db.Text)
    resume_filename = db.Column(db.String(255))
    __table_args__ = (db.UniqueConstraint('email', 'position', name='unique_app'),)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tab = db.Column(db.String(20))  # cooperation or career

    # Cooperation
    company_email = db.Column(db.String(120))
    phone = db.Column(db.String(20))
    project_details = db.Column(db.Text)

    # Career
    first_name = db.Column(db.String(100))
    last_name = db.Column(db.String(100))
    email = db.Column(db.String(120))
    linked_in = db.Column(db.String(255))
    resume_filename = db.Column(db.String(255))

    referral = db.Column(db.String(50))

