from datetime import datetime
from spotify_wordcloud import db


class Pictures(db.Model):

    __tablename__ = "pictures"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(255), nullable=False)
    file_name = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.now)
