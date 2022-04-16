from flask import Blueprint, jsonify
from flask import request

from src.administration.lookup.lookup_service import LookupService
from src.common.response_customizer import respond

administration_page = Blueprint("administration", __name__, url_prefix='/administration')


@administration_page.route("/lookups", methods=["GET"] )
def get_all_lookups():
    look_up_service = LookupService()
    return respond(look_up_service.get_alle_lookup)


@administration_page.route("/lookups/<aktien_name>", methods=["GET"])
def get_specific_lookups(aktien_name):
    look_up_service = LookupService()
    print(look_up_service.get_specific_lookup(aktien_name))
    return jsonify(look_up_service.get_specific_lookup(aktien_name))


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
