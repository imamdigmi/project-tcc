from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

DB_HOST = '188.166.237.104'
DB_PORT = '3306'
DB_USER = 'root'
DB_PASS = '@Root<<0'
DB_NAME = 'kulina'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(DB_USER,DB_PASS,DB_HOST,DB_PORT,DB_NAME)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
db = SQLAlchemy(app)
ma = Marshmallow(app)

class UserReview(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer)
    product_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer)
    rating = db.Column(db.Float)
    review = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, order_id, product_id, user_id, rating, review):
        self.order_id = order_id
        self.product_id = product_id
        self.user_id = user_id
        self.rating = rating
        self.review = review


class UserReviewSchema(ma.Schema):
    class Meta:
        fields = ('order_id', 'product_id', 'user_id', 'rating', 'review')

review_schema = UserReviewSchema()
reviews_schema = UserReviewSchema(many=True)


@app.route("/", methods=["GET"])
def all():
    reviews = UserReview.query.all()
    result = reviews_schema.dump(reviews)
    return jsonify(result.data)


@app.route("/review", methods=["POST"])
def create():
    order_id = request.json['order_id']
    product_id = request.json['product_id']
    user_id = request.json['user_id']
    rating = request.json['rating']
    review = request.json['review']

    new_review = UserReview(order_id, product_id, user_id, rating, review)
    result = review_schema.dump(new_review)

    db.session.add(new_review)
    db.session.commit()

    return jsonify(result)


@app.route("/review/<id>", methods=["GET"])
def detail(id):
    review = UserReview.query.get(id)
    return review_schema.jsonify(review)


@app.route("/review/<id>", methods=["PUT"])
def update(id):
    review_obj = UserReview.query.get(id)

    review_obj.order_id = request.json['order_id']
    review_obj.product_id = request.json['product_id']
    review_obj.user_id = request.json['user_id']
    review_obj.rating = request.json['rating']
    review_obj.review = request.json['review']

    db.session.commit()
    return review_schema.jsonify(review_obj)


@app.route("/review/<id>", methods=["DELETE"])
def delete(id):
    review = UserReview.query.get(id)
    db.session.delete(review)
    db.session.commit()

    return review_schema.jsonify(review)


if __name__ == '__main__':
    app.run(debug=True)