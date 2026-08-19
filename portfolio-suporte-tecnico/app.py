import os
from flask import Flask, render_template

from config import Config
from models import db, Ticket
from tickets import tickets_bp
from blueprints.docs_bp import docs_bp
from blueprints.lab_bp import lab_bp
from blueprints.scripts_bp import scripts_bp
from blueprints.security_bp import security_bp


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Garante que a pasta 'instance' exista para o banco SQLite
    os.makedirs(os.path.join(app.root_path, "instance"), exist_ok=True)

    db.init_app(app)

    # Registro dos módulos (blueprints)
    app.register_blueprint(docs_bp)
    app.register_blueprint(tickets_bp)
    app.register_blueprint(lab_bp)
    app.register_blueprint(scripts_bp)
    app.register_blueprint(security_bp)

    @app.route("/")
    def home():
        total_chamados = Ticket.query.count()
        abertos = Ticket.query.filter_by(status="Aberto").count()
        resolvidos = Ticket.query.filter_by(status="Resolvido").count()
        return render_template(
            "index.html",
            total_chamados=total_chamados,
            abertos=abertos,
            resolvidos=resolvidos,
        )

    @app.errorhandler(404)
    def nao_encontrado(e):
        return render_template("404.html"), 404

    with app.app_context():
        db.create_all()

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
