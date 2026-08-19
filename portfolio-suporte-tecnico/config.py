import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    """Configuração base da aplicação."""
    SECRET_KEY = os.environ.get("SECRET_KEY", "chave-secreta-portfolio-suporte-tecnico")
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        "DATABASE_URL", f"sqlite:///{os.path.join(BASE_DIR, 'instance', 'chamados.db')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # Diretórios de conteúdo usados pelos módulos de documentação e scripts
    DOCS_DIR = os.path.join(BASE_DIR, "docs")
    LAB_DIR = os.path.join(BASE_DIR, "lab")
    SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")
