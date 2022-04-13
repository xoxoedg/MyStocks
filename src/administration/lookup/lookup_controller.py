import json

from flask import Blueprint, jsonify
from flask import request

from src import app
from src.administration.lookup.lookup_service import LookupService

administration_page = Blueprint("administration", __name__, url_prefix='/administration')


@administration_page.route("/lookups", methods=["GET"])
def get_all_lookups():
    look_up_service = LookupService()
    try:
        lookup = look_up_service.get_alle_lookup()
    except ValueError as e:
        return app.response_class(response=json.dumps({"msg": "THIS IS AN ERROR"}),
                                  status=401,
                                  mimetype='application/json')
    return app.response_class(response=json.dumps(lookup),
                              status=200,
                              mimetype='application/json')


@administration_page.route("/lookups/anlegen", methods=["POST"])
def post_neuen_lookup():
    data = request.get_json()
    look_up_service = LookupService()
    look_up_service.add_aktie_lookup(data)
    return jsonify({"msg": "successful"})


@administration_page.route("/lookups/bearbeiten", methods=["PUT"])
def bearbeite_lookup_eintrag():
    data = request.get_json()
    look_up_service = LookupService()
    look_up_service.bearbeite_lookup(data)
    return jsonify("Sucssfull")


@administration_page.route("/lookups/loeschen/<aktie>", methods=["DELETE"])
def loesche_lookup_eintrag(aktie):
    look_up_service = LookupService()
    look_up_service.loesche_lookup(aktie)
    return jsonify("Sucssfull")
