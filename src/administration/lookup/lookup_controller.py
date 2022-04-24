from flask import Blueprint
from flask import request

from src.administration.lookup.lookup_service import LookupService
from src.common.response_customizer import respond

administration_page = Blueprint("administration", __name__, url_prefix='/administration')

look_up_service = LookupService()



@administration_page.route("/lookups", methods=["GET"])
def get_all_lookups():
    return respond(look_up_service.get_alle_lookup)


@administration_page.route("/lookups/<aktien_name>", methods=["GET"])
def get_specific_lookups(aktien_name):
    specific_aktie = lambda: look_up_service.get_specific_lookup(aktien_name)
    return respond(specific_aktie)


@administration_page.route("/lookups/anlegen", methods=["POST"])
def post_neuen_lookup():
    data = request.get_json()
    created_lookup = lambda: look_up_service.add_aktie_lookup(data).serialize()
    return respond(created_lookup)


@administration_page.route("/lookups/bearbeiten", methods=["PUT"])
def bearbeite_lookup_eintrag():
    data = request.get_json()
    modified_lookup = lambda: look_up_service.bearbeite_lookup(data).serialize()
    return respond(modified_lookup)


@administration_page.route("/lookups/loeschen/<aktie>", methods=["DELETE"])
def loesche_lookup_eintrag(aktie):
    deleted_lookup = lambda: look_up_service.loesche_lookup(aktie).serialize()
    return respond(deleted_lookup)
