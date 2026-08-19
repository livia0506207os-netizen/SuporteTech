import os
from flask import Blueprint, render_template, current_app, send_from_directory, abort

scripts_bp = Blueprint("scripts", __name__, url_prefix="/scripts", template_folder="../templates/scripts")

CATALOGO_SCRIPTS = [
    {
        "nome": "Limpar Cache",
        "descricao": "Remove arquivos temporários e cache do sistema para liberar espaço em disco.",
        "powershell": "limpar-cache.ps1",
        "batch": "limpar-cache.bat",
    },
    {
        "nome": "Verificar Espaço em Disco",
        "descricao": "Gera um relatório do espaço utilizado e disponível em cada unidade de disco.",
        "powershell": "verificar-disco.ps1",
        "batch": "verificar-disco.bat",
    },
    {
        "nome": "Mapear Unidade de Rede",
        "descricao": "Mapeia automaticamente uma unidade de rede compartilhada com letra de drive fixa.",
        "powershell": "mapear-rede.ps1",
        "batch": "mapear-rede.bat",
    },
]


def _ler_conteudo(pasta, nome_arquivo):
    caminho = os.path.join(current_app.config["SCRIPTS_DIR"], pasta, nome_arquivo)
    if not os.path.exists(caminho):
        return None
    with open(caminho, "r", encoding="utf-8") as f:
        return f.read()


@scripts_bp.route("/")
def index():
    """Lista todos os scripts de automação disponíveis (PowerShell e Batch)."""
    return render_template("scripts/index.html", scripts=CATALOGO_SCRIPTS)


@scripts_bp.route("/ver/<pasta>/<nome_arquivo>")
def visualizar(pasta, nome_arquivo):
    """Exibe o conteúdo de um script diretamente no navegador."""
    if pasta not in ("powershell", "batch"):
        abort(404)
    conteudo = _ler_conteudo(pasta, nome_arquivo)
    if conteudo is None:
        abort(404)
    linguagem = "powershell" if pasta == "powershell" else "batch"
    return render_template(
        "scripts/visualizar.html",
        nome_arquivo=nome_arquivo,
        conteudo=conteudo,
        pasta=pasta,
        linguagem=linguagem,
    )


@scripts_bp.route("/baixar/<pasta>/<nome_arquivo>")
def baixar(pasta, nome_arquivo):
    """Permite o download direto do arquivo de script."""
    if pasta not in ("powershell", "batch"):
        abort(404)
    diretorio = os.path.join(current_app.config["SCRIPTS_DIR"], pasta)
    return send_from_directory(diretorio, nome_arquivo, as_attachment=True)
