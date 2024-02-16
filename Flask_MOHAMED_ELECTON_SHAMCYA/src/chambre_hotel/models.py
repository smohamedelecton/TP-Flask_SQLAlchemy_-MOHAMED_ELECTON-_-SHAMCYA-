from .database import db


class Client(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  nom = db.Column(db.String(80), nullable=False)
  email = db.Column(db.String(80), nullable=False)
  reservations= db.relationship('Reservation', backref='client', lazy='dynamic')

class Chambre(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  numero = db.Column(db.Integer, unique=True, nullable=False)
  type = db.Column(db.String(80))
  prix = db.Column(db.Float)
  reservations= db.relationship('Reservation', backref='chambre', lazy='dynamic')


class Reservation(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  id_client = db.Column(db.Integer, db.ForeignKey('client.id'))
  id_chambre = db.Column(db.Integer, db.ForeignKey('chambre.id'))
  date_arrivee = db.Column(db.DateTime)
  date_depart = db.Column(db.DateTime)
  statut = db.Column(db.String(80))