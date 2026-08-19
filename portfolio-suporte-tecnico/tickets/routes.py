from flask import Blueprint, render_template, request, redirect, url_for, flash, jsonify
from models import db, Ticket, STATUS_CHOICES, PRIORIDADE_CHOICES

tickets_bp = Blueprint("tickets", __name__, url_prefix="/chamados", template_folder="../templates/tickets")


@tickets_bp.route("/")
def listar():
    """Lista todos os chamados, com filtro opcional por status."""
    status_filtro = request.args.get("status", "")
    query = Ticket.query
    if status_filtro:
        query = query.filter_by(status=status_filtro)
    chamados = query.order_by(Ticket.criado_em.desc()).all()

    total = Ticket.query.count()
    resumo = {
        s: Ticket.query.filter_by(status=s).count() for s in STATUS_CHOICES
    }

    return render_template(
        "tickets/listar.html",
        chamados=chamados,
        status_filtro=status_filtro,
        status_choices=STATUS_CHOICES,
        resumo=resumo,
        total=total,
    )


@tickets_bp.route("/novo", methods=["GET", "POST"])
def novo():
    """Abre um novo chamado."""
    if request.method == "POST":
        usuario = request.form.get("usuario", "").strip()
        problema = request.form.get("problema", "").strip()
        categoria = request.form.get("categoria", "Geral")
        prioridade = request.form.get("prioridade", "Média")

        if not usuario or not problema:
            flash("Preencha o nome do usuário e a descrição do problema.", "danger")
            return redirect(url_for("tickets.novo"))

        ticket = Ticket(
            numero=Ticket.gerar_numero(),
            usuario=usuario,
            problema=problema,
            categoria=categoria,
            prioridade=prioridade,
            status="Aberto",
        )
        db.session.add(ticket)
        db.session.commit()
        flash(f"Chamado {ticket.numero} aberto com sucesso!", "success")
        return redirect(url_for("tickets.detalhe", ticket_id=ticket.id))

    return render_template(
        "tickets/novo.html",
        prioridade_choices=PRIORIDADE_CHOICES,
        categorias=["Rede", "Hardware", "Software", "Impressora", "Segurança", "Geral"],
    )


@tickets_bp.route("/<int:ticket_id>")
def detalhe(ticket_id):
    """Exibe o detalhe de um chamado específico."""
    ticket = Ticket.query.get_or_404(ticket_id)
    return render_template(
        "tickets/detalhe.html",
        ticket=ticket,
        status_choices=STATUS_CHOICES,
    )


@tickets_bp.route("/<int:ticket_id>/atualizar", methods=["POST"])
def atualizar(ticket_id):
    """Atualiza o status, técnico responsável e observações de um chamado."""
    ticket = Ticket.query.get_or_404(ticket_id)

    novo_status = request.form.get("status")
    if novo_status in STATUS_CHOICES:
        ticket.status = novo_status

    ticket.tecnico_responsavel = request.form.get("tecnico_responsavel", ticket.tecnico_responsavel).strip() or ticket.tecnico_responsavel
    ticket.observacoes = request.form.get("observacoes", ticket.observacoes)

    db.session.commit()
    flash(f"Chamado {ticket.numero} atualizado.", "success")
    return redirect(url_for("tickets.detalhe", ticket_id=ticket.id))


@tickets_bp.route("/<int:ticket_id>/excluir", methods=["POST"])
def excluir(ticket_id):
    """Remove um chamado (uso administrativo/demonstração)."""
    ticket = Ticket.query.get_or_404(ticket_id)
    numero = ticket.numero
    db.session.delete(ticket)
    db.session.commit()
    flash(f"Chamado {numero} removido.", "info")
    return redirect(url_for("tickets.listar"))


@tickets_bp.route("/api/chamados")
def api_listar():
    """Endpoint JSON simples, útil para demonstrar integração/API REST."""
    chamados = Ticket.query.order_by(Ticket.criado_em.desc()).all()
    return jsonify([c.to_dict() for c in chamados])
