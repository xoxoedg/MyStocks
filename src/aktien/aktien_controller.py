from flask import Blueprint

from src.aktien.aktien_service import AktienService
from src.common.response_customizer import respond

aktien = Blueprint("aktien", __name__, url_prefix='/aktien')

aktien_service = AktienService()


@aktien.route("", methods=["GET"])
def aktien_auswahl():
    return respond(aktien_service.get_aktien_auswahl)
