from sqlalchemy import ForeignKey

from src import db


class Aktie(db.Model):

    __tablename__ = "Aktie"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    lookup_id = db.Column(db.Integer, ForeignKey('LookUps.id'))
    datum_naechster_quarterly_report = db.Column(db.Date)
    aktueller_preis = db.Column(db.Float)
    aktiv = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<id {}>'.format(self.id)
