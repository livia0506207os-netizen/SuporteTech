from flask import Blueprint, render_template, request, redirect, url_for, flash

security_bp = Blueprint("security", __name__, url_prefix="/seguranca", template_folder="../templates/security")

# Estado em memória apenas para fins de DEMONSTRAÇÃO da simulação de firewall.
# Em um cenário real, isso jamais aplicaria regras a um firewall de verdade.
REGRAS_FIREWALL = [
    {"id": 1, "nome": "Permitir HTTP", "porta": 80, "protocolo": "TCP", "acao": "PERMITIR", "direcao": "Entrada"},
    {"id": 2, "nome": "Permitir HTTPS", "porta": 443, "protocolo": "TCP", "acao": "PERMITIR", "direcao": "Entrada"},
    {"id": 3, "nome": "Bloquear Telnet", "porta": 23, "protocolo": "TCP", "acao": "BLOQUEAR", "direcao": "Entrada"},
]


@security_bp.route("/firewall", methods=["GET", "POST"])
def firewall():
    """Simulação educacional de um painel de configuração de firewall."""
    if request.method == "POST":
        try:
            nova_regra = {
                "id": (max([r["id"] for r in REGRAS_FIREWALL]) + 1) if REGRAS_FIREWALL else 1,
                "nome": request.form.get("nome", "Nova regra").strip(),
                "porta": int(request.form.get("porta", 0)),
                "protocolo": request.form.get("protocolo", "TCP"),
                "acao": request.form.get("acao", "PERMITIR"),
                "direcao": request.form.get("direcao", "Entrada"),
            }
            REGRAS_FIREWALL.append(nova_regra)
            flash(f"Regra '{nova_regra['nome']}' criada (simulação).", "success")
        except ValueError:
            flash("Porta inválida. Informe um número.", "danger")
        return redirect(url_for("security.firewall"))

    return render_template("security/firewall.html", regras=REGRAS_FIREWALL)


@security_bp.route("/firewall/<int:regra_id>/remover", methods=["POST"])
def remover_regra(regra_id):
    global REGRAS_FIREWALL
    REGRAS_FIREWALL = [r for r in REGRAS_FIREWALL if r["id"] != regra_id]
    flash("Regra removida (simulação).", "info")
    return redirect(url_for("security.firewall"))
