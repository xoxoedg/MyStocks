from flask import Blueprint

administration_page = Blueprint("/administration", __name__)


@administration_page.route("/lookups", method=["GET"])
def get_all_lookups():
    return "Hello"