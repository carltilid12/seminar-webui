from flask import Flask
from config import API_BASE_URL

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_mapping(
        API_BASE_URL=API_BASE_URL,
    )

    from .routes.student_route import student_bp
    from .routes.course_route import course_bp

    app.register_blueprint(student_bp, url_prefix='/')
    app.register_blueprint(course_bp, url_prefix='/')

    return app