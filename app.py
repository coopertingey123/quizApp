from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_heroku import Heroku

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://gkvpnjtrubkyld:7f8bdfb54846df9df7edba1f0b819a8bbf9715d1278d2f75d9e048996d75355b@ec2-3-210-23-22.compute-1.amazonaws.com:5432/d2r6ifa666j6u3"

db = SQLAlchemy(app)
ma = Marshmallow(app)

CORS(app)
Heroku(app)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String, nullable=False, unique=True)

    def __init(self, text):
        self.text = text

class QuestionSchema(ma.Schema):
    class Meta:
        fields = ("id", "text")

question_schema = QuestionSchema()
multiple_question_schema = QuestionSchema(many=True)




if __name__ == "__main__":
    app.run(debug=True)