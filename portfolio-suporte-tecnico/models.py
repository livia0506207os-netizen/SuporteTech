from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

STATUS_CHOICES = ["Aberto", "Em andamento", "Resolvido"]
PRIORIDADE_CHOICES = ["Baixa", "Média", "Alta"]


class Ticket(db.Model):
    """Representa um chamado de suporte técnico (Help Desk)."""

    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    numero = db.Column(db.String(20), unique=True, nullable=False)
    usuario = db.Column(db.String(120), nullable=False)
    problema = db.Column(db.Text, nullable=False)
    categoria = db.Column(db.String(50), default="Geral")
    prioridade = db.Column(db.String(20), default="Média")
    status = db.Column(db.String(20), default="Aberto", nullable=False)
    tecnico_responsavel = db.Column(db.String(120), default="Não atribuído")
    observacoes = db.Column(db.Text, default="")
    criado_em = db.Column(db.DateTime, default=datetime.utcnow)
    atualizado_em = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "numero": self.numero,
            "usuario": self.usuario,
            "problema": self.problema,
            "categoria": self.categoria,
            "prioridade": self.prioridade,
            "status": self.status,
            "tecnico_responsavel": self.tecnico_responsavel,
            "observacoes": self.observacoes,
            "criado_em": self.criado_em.strftime("%d/%m/%Y %H:%M"),
            "atualizado_em": self.atualizado_em.strftime("%d/%m/%Y %H:%M"),
        }

    @staticmethod
    def gerar_numero():
        """Gera um número sequencial de ticket no formato TCK-0001."""
        ultimo = Ticket.query.order_by(Ticket.id.desc()).first()
        proximo_id = (ultimo.id + 1) if ultimo else 1
        return f"TCK-{proximo_id:04d}"
