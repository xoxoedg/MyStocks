from config import DevConfig, ProdConfig
from src import create_app, db

app = create_app(config_file=DevConfig)

if __name__ == "__main__":
    with app.app_context():

        db.create_all()
        db.session.commit()

    app.run(debug=True)
