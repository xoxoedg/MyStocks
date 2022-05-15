from flask import Blueprint, request

from src.aktien.aktien_dtos import AuswahlBestaetigenRequestDto
from src.aktien.aktien_service import AktienService
from src.common.response_customizer import respond

aktien = Blueprint("aktien", __name__, url_prefix='/aktien')

aktien_service = AktienService()


@aktien.route("", methods=["GET"])
def aktien_auswahl():
    return respond(aktien_service.get_aktien_auswahl)


@aktien.route("", methods=["POST"])
def auswahl_bestaetigen():
    data = AuswahlBestaetigenRequestDto(request.get_json())
    return respond(lambda: aktien_service.auswahl_bestaetigen(data.selected_aktien))
