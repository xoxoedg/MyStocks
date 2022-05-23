from flask import Blueprint, request

from src.aktien.aktien_dtos import AuswahlBestaetigenRequestDto
from src.aktien.aktien_service import AktienService
from src.common.response_customizer import respond

aktien = Blueprint("aktien", __name__, url_prefix='/aktie')

aktien_service = AktienService()


@aktien.route("", methods=["GET"])
def aktive_aktien():
    return respond(aktien_service.get_aktive_aktien)


@aktien.route("/auswahl", methods=["GET"])
def aktien_auswahl():
    return respond(aktien_service.get_aktien_auswahl)


@aktien.route("/auswahl", methods=["POST"])
def auswahl_bestaetigen():
    data = AuswahlBestaetigenRequestDto(request.get_json())
    return respond(lambda: aktien_service.auswahl_bestaetigen(data.selected_aktien))
