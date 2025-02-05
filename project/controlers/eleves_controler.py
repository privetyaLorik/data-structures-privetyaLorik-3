""" Ce fichier contient au départ toutes les routes de l'application
# Concernant le CRUD des élèves
"""
from flask import Blueprint, request, render_template, redirect, url_for


import services.eleves as svc


eleves_bp = Blueprint('eleves_bp', __name__)

@eleves_bp.route('/', methods=['GET'])
def liste_eleves():
    # Traitement du template et transmission du HTML généré au client
    return render_template('liste_eleves.jinja', eleves=svc.get_all_eleves())


@eleves_bp.route('/create', methods=['GET', 'POST'])
def create_eleve():
    if request.method == 'POST':
        # On utilise un POST pour créer un nouvel élève
        print("CREATION")
        id_eleve = svc.create_eleve(request.form['nom'], request.form['prenom'],request.form['age'])
        return redirect(url_for('eleves_bp.read_eleve', id=id_eleve))
    else:
        # On utilise un GET pour afficher le formulaire
        return render_template('form_eleve.jinja', eleve=None)


@eleves_bp.route('/<int:id>', methods=['GET'])
def read_eleve(id: int):
    e = svc.get_eleve(id)
    return render_template('detail_eleve.jinja', eleve=e, action='afficher')


@eleves_bp.route('/update/<int:eid>', methods=['GET', 'POST'])
def update_eleve(eid: int):
    if request.method == 'POST':
        # On utilise un POST pour créer un nouvel élève
        svc.update_eleve(eid, request.form['nom'], request.form['prenom'],request.form['age'])
        return redirect(url_for('eleves_bp.read_eleve', id=eid))
    else:
        # On utilise un GET pour afficher le formulaire
        e = svc.get_eleve(eid)
        print("Demande de modification",e)
        return render_template('form_eleve.jinja', eleve=e)


@eleves_bp.route('/delete/<int:eid>', methods=['GET'])
def delete_eleve(eid: int):
    svc.delete_eleve(eid)
    return redirect(url_for('eleves_bp.liste_eleves'))
