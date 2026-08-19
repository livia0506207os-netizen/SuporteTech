import os
import markdown
from flask import Blueprint, render_template, abort, current_app

docs_bp = Blueprint("docs", __name__, url_prefix="/docs", template_folder="../templates/docs")

# Metadados dos guias de Help Desk (arquivo markdown, título e ícone/imagem simulada)
GUIAS_HELPDESK = {
    "wifi": {
        "titulo": "Wi-Fi não conecta",
        "arquivo": "wifi.md",
        "resumo": "Passo a passo para diagnosticar e resolver falhas de conexão sem fio.",
        "icone": "📶",
    },
    "impressora": {
        "titulo": "Impressora não imprime",
        "arquivo": "impressora.md",
        "resumo": "Checklist completo para resolver problemas de impressão local e em rede.",
        "icone": "🖨️",
    },
    "computador-lento": {
        "titulo": "Computador lento",
        "arquivo": "computador-lento.md",
        "resumo": "Diagnóstico de desempenho e otimização de estações de trabalho.",
        "icone": "🐢",
    },
}

GUIAS_SEGURANCA = {
    "boas-praticas": {
        "titulo": "Boas Práticas de Segurança",
        "arquivo": "boas-praticas.md",
        "resumo": "Antivírus, firewall, backup e higiene digital para usuários e técnicos.",
        "icone": "🛡️",
    },
    "firewall": {
        "titulo": "Configuração de Firewall",
        "arquivo": "firewall.md",
        "resumo": "Simulação de regras de firewall (Windows Defender Firewall / iptables).",
        "icone": "🧱",
    },
    "backup": {
        "titulo": "Rotina de Backup",
        "arquivo": "backup.md",
        "resumo": "Estratégia 3-2-1 e agendamento de rotinas de backup.",
        "icone": "💾",
    },
}


def _ler_markdown(caminho):
    if not os.path.exists(caminho):
        abort(404)
    with open(caminho, "r", encoding="utf-8") as f:
        conteudo = f.read()
    return markdown.markdown(conteudo, extensions=["fenced_code", "tables", "toc"])


@docs_bp.route("/")
def index():
    """Página inicial da documentação: lista Help Desk e Segurança."""
    return render_template(
        "docs/index.html",
        guias_helpdesk=GUIAS_HELPDESK,
        guias_seguranca=GUIAS_SEGURANCA,
    )


@docs_bp.route("/helpdesk/<slug>")
def helpdesk_guia(slug):
    """Exibe um guia de Help Desk renderizado a partir do markdown."""
    guia = GUIAS_HELPDESK.get(slug)
    if not guia:
        abort(404)
    caminho = os.path.join(current_app.config["DOCS_DIR"], "helpdesk", guia["arquivo"])
    html = _ler_markdown(caminho)
    return render_template("docs/guia.html", guia=guia, conteudo_html=html, categoria="Help Desk", voltar_url="docs.index")


@docs_bp.route("/seguranca/<slug>")
def seguranca_guia(slug):
    """Exibe um guia/documentação de segurança renderizado a partir do markdown."""
    guia = GUIAS_SEGURANCA.get(slug)
    if not guia:
        abort(404)
    caminho = os.path.join(current_app.config["DOCS_DIR"], "seguranca", guia["arquivo"])
    html = _ler_markdown(caminho)
    return render_template("docs/guia.html", guia=guia, conteudo_html=html, categoria="Segurança", voltar_url="docs.index")
