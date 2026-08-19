import os
import markdown
from flask import Blueprint, render_template, current_app, abort

lab_bp = Blueprint("lab", __name__, url_prefix="/laboratorio", template_folder="../templates/lab")

# Vídeos simulados (metadados apenas, sem upload real de binário neste portfólio)
VIDEOS_SIMULADOS = [
    {
        "titulo": "Resolvendo falha de rede em VM (VirtualBox)",
        "duracao": "04:32",
        "descricao": "Demonstração da configuração de adaptador de rede em modo Bridge para restaurar conectividade.",
    },
    {
        "titulo": "Instalação de driver de impressora em ambiente virtualizado",
        "duracao": "03:10",
        "descricao": "Passo a passo de instalação e teste de driver universal de impressão.",
    },
    {
        "titulo": "Atualização de software via script automatizado",
        "duracao": "02:47",
        "descricao": "Execução de script PowerShell para atualização em lote de aplicativos.",
    },
]


@lab_bp.route("/")
def index():
    """Página principal do laboratório virtual."""
    caminho = os.path.join(current_app.config["LAB_DIR"], "roteiro.md")
    conteudo_html = ""
    if os.path.exists(caminho):
        with open(caminho, "r", encoding="utf-8") as f:
            conteudo_html = markdown.markdown(f.read(), extensions=["fenced_code", "tables"])
    return render_template("lab/index.html", conteudo_html=conteudo_html, videos=VIDEOS_SIMULADOS)


@lab_bp.route("/scripts-rede")
def scripts_rede():
    """Página com scripts de configuração de rede, drivers e atualização."""
    caminho = os.path.join(current_app.config["LAB_DIR"], "scripts-rede.md")
    if not os.path.exists(caminho):
        abort(404)
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo_html = markdown.markdown(f.read(), extensions=["fenced_code", "tables"])
    return render_template("lab/scripts_rede.html", conteudo_html=conteudo_html)
