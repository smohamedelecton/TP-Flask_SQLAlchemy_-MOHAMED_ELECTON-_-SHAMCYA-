from .models import Chambre, Client, Reservation
from flask import Blueprint, jsonify, request
from .database import db
from datetime import datetime

main = Blueprint("main", __name__)

#AJOUTER UNE CHAMBRE
@main.route('/api/chambres', methods=['POST'])
def ajouter_chambre():
    data = request.get_json()
    numero= data['numero']
    type= data['type']
    prix= data['prix']
    new_room = Chambre(numero=numero, type=type, prix=prix)
    db.session.add(new_room)
    db.session.commit()
    return jsonify({"success": True, "message": "Chambre ajoutee avec succes."})
  
#AJOUTER UN CLIENT
@main.route('/api/clients', methods=['POST'])
def ajouter_client():
    data = request.get_json()
    nom= data['nom']
    email= data['email']
    new_client = Client(nom=nom, email=email)
    db.session.add(new_client)
    db.session.commit()
    return jsonify({"success": True, "message": "Client ajoute avec succes."})

#AJOUTER UNE RESERVATION
@main.route('/api/reservations', methods=['POST'])
def ajouter_reservation():
    data = request.get_json()
    id_client= data['id_client']
    id_chambre= data['id_chambre']
    date_arrivee= datetime.strptime(data['date_arrivee'], "%d %B, %Y")
    date_depart= datetime.strptime(data['date_depart'], "%d %B, %Y")
    new_reservation = Reservation(id_client=id_client, id_chambre=id_chambre, date_arrivee=date_arrivee, date_depart=date_depart, statut='confirme')
    db.session.add(new_reservation)
    db.session.commit()
    return jsonify({"success": True, "message": "Reservation creee avec succes."})

#ANNULER UNE RESERVATION
@main.route('/api/reservations/<int:id>', methods=['DELETE'])
def supprimer_reservation(id):
  delete_reservation= Reservation.query.get_or_404(id)
  db.session.delete(delete_reservation)
  db.session.commit()
  return jsonify( {"success": True, "message": "Reservation annulee avec succes."})


#SUPPRIMER UNE CHAMBRE
@main.route('/api/chambres/<int:id>', methods=['DELETE'])
def supprimer_chambre(id):
  delete_chambre= Chambre.query.get_or_404(id)
  db.session.delete(delete_chambre)
  db.session.commit()
  return jsonify( {"success": True, "message": "Chambre suprimee avec succes."})

#METTRE UNE CHAMBRE A JOUR
@main.route('/api/chambres/<int:id>', methods=['PUT'])
def mettre_a_jour_chambre(id):
  data = request.get_json()
  update_chambre= Chambre.query.get_or_404(id)
  if  'type' in data: 
     update_chambre.type = data['type']
  if 'prix' in data :
     update_chambre.prix = data['prix'],
  if 'numero' in data :
   update_chambre.numero = data['numero'],
  db.session.commit()
  return jsonify( {"success": True, "message": "Chambre modifiee avec succes."})

#CHERCHER LES CHAMBRES DISPONIBLES
@main.route('/api/chambres/disponibles', methods=['GET'])
def chambre_disponible():
  data = request.get_json()
  date_arrivee= datetime.strptime(data['date_arrivee'], "%d %B, %Y")
  date_depart= datetime.strptime(data['date_depart'], "%d %B, %Y")
  chambre_non_dispo = Reservation.query.filter(
  (Reservation.id_chambre == data['id_chambre']) &
  ((Reservation.date_arrivee < date_depart) & (Reservation.date_depart > date_arrivee))).all()
  if chambre_non_dispo:
    return jsonify({'success': False, 'message': 'La chambre n est pas disponible pour les dates que vous voulez.'})
  else:
     return jsonify({'success': True, 'message': 'La chambre est disponible, vous pouvez la reserver.'})
