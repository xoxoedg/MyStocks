from src.administration.lookup.lookup_dto import LookupDto


class LookupAdapter:

    @staticmethod
    def to_dto(lookup):
        lock_up_dto = LookupDto()
        lock_up_dto.app_name = lookup.app_name
        lock_up_dto.api_name = lookup.api_name

        return lock_up_dto