from flask import Flask
from flask_talisman import Talisman
from flask_seasurf import SeaSurf
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("spotify_wordcloud.config")

csrf = SeaSurf(app)

if not app.config["FLASK_DEBUG"]:
    talisman = Talisman(
        app,
        content_security_policy="default-src https: self; "
                                "script-src https: 'unsafe-inline'; "
                                "style-src https: 'unsafe-inline'; "
                                "img-src * blob:;",
    )
db = SQLAlchemy(app)
