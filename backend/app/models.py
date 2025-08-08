from dataclasses import dataclass
from . import db


@dataclass
class AboutText(db.Model):
    __tablename__ = 'about_text'

    id: int = db.Column(db.Integer, primary_key=True)
    content: str = db.Column(db.Text, nullable=False)
