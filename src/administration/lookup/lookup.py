from src import db


class LookUp(db.Model):

    __tablename__ = "LookUps"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    app_name = db.Column(db.String(50), nullable=False)
    api_name = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return '<User %r>' % self.api_name


