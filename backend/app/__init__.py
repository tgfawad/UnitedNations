from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import get_database_uri

db = SQLAlchemy()

__all__ = ["create_app", "db"]


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = get_database_uri()
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    CORS(app)
    db.init_app(app)

    # Import models package (exports AboutText) and routes blueprint
    from .models import AboutText
    from .routes import api_bp

    with app.app_context():
        db.create_all()
        # Seed AboutText once if empty
        if not AboutText.query.first():
            seed = AboutText(
                content=(
                    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut semper at quam eu pretium. "
                    "Aliquam ac pellentesque ex. Pellentesque fermentum imperdiet justo, ac feugiat ligula rhoncus sed. "
                    "Duis tempor diam nec purus hendrerit, vitae tempor sapien vulputate. Sed pharetra augue id dui convallis sollicitudin. "
                    "Aenean rhoncus, enim a rutrum molestie, tellus lorem feugiat tellus, eu consectetur lectus nisl in odio. "
                    "Curabitur convallis elit vitae eleifend eleifend. Quisque a magna id massa hendrerit dictum. "
                    "Fusce eu mollis lectus. Sed laoreet ligula eu mi finibus laoreet. Praesent id viverra nisl, a hendrerit justo. "
                    "Nulla eget augue nibh. Aenean vitae lobortis ante, sit amet interdum arcu. Sed non tortor ut ante bibendum lacinia."
                )
            )
            db.session.add(seed)
            db.session.commit()

    app.register_blueprint(api_bp, url_prefix='/api')
    return app
