from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Meals(db.Model):
    __tablename__ = 'Meals'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    photo = db.Column(db.String())

    def __init__(self, name, photo):
        self.name = name
        self.photo = photo

    def __repr__(self):
        return f"{self.name}:{self.photo}"

class Ingredients(db.Model):
    __tablename__ = 'Ingredients'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String())
    amount = db.Column(db.String())
    calorie = db.Column(db.Integer())
    photo = db.Column(db.String())
    meal_id = db.Column(db.Integer(), db.ForeignKey(Meals.id))


    def __init__(self, name, amount, calorie, photo, meal_id):
        self.name = name
        self.amount = amount
        self.calorie = calorie
        self.photo = photo
        self.meal_id = meal_id

    def __repr__(self):
        return f"{self.name}:{self.photo}"