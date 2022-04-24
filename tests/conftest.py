import pytest
from src import create_app, db
from src.administration.lookup.lookup import LookUp
from src.administration.lookup.lookup_service import LookupService


@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def db_client(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///:memory:"
    app.config["TESTING"] = True
    with app.app_context():
        db.init_app(app)
        db.create_all()
        db.session.commit()

        yield db

        db.session.remove()


