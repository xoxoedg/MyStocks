from flask import Blueprint, jsonify
from flask import request

from src.administration.lookup.lookup_service import LookupService

administration_page = Blueprint("administration", __name__, url_prefix='/administration')


@administration_page.route("/lookups", methods=["GET"])
def get_all_lookups():
    look_up_service = LookupService()
    return jsonify(look_up_service.get_alle_aktien())


@administration_page.route("/lookups/anlegen", methods=["POST"])
def post_neuen_lookup():
    data = request.get_json()
    print(data)
    look_up_service = LookupService()
    look_up_service.add_aktie_lookup(data["app_name"], data["api_name"])
    return jsonify({"msg": "successful"})