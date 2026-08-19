# 🖥️ Portfólio — Analista de Suporte Técnico

Sistema web completo desenvolvido em **Python (Flask)** para demonstrar, de forma prática, as competências de um Analista de Suporte Técnico: documentação de Help Desk, gestão de chamados, laboratório virtual, automação com scripts e segurança básica de TI.

> Projeto criado para fins de **portfólio profissional**, podendo ser publicado no GitHub e executado localmente para demonstração em entrevistas ou processos seletivos.

---

## 📸 Visão geral

O sistema é uma aplicação web única, organizada em **5 módulos**, acessíveis a partir do menu principal:

| Módulo | Descrição | Rota principal |
|---|---|---|
| 📘 Documentação de Help Desk | Guias passo a passo (Wi-Fi, impressora, computador lento) | `/docs` |
| 🎫 Simulação de Chamados | Abertura e acompanhamento de tickets de suporte | `/chamados` |
| 🧪 Laboratório Virtual | Roteiro de VMs, scripts de rede e vídeos demonstrativos | `/laboratorio` |
| ⚙️ Scripts de Automação | Scripts PowerShell/Batch para download | `/scripts` |
| 🛡️ Segurança Básica | Boas práticas, simulação de firewall e backup | `/seguranca/firewall` |

---

## 🗂️ Estrutura do projeto

```
portfolio-suporte-tecnico/
├── app.py                     # Ponto de entrada da aplicação (application factory)
├── config.py                  # Configurações (banco de dados, caminhos)
├── models.py                  # Modelo de dados do módulo de Chamados (SQLAlchemy)
├── requirements.txt           # Dependências Python
├── .gitignore
│
├── blueprints/                # Rotas dos módulos de Documentação, Laboratório, Scripts e Segurança
│   ├── docs_bp.py
│   ├── lab_bp.py
│   ├── scripts_bp.py
│   └── security_bp.py
│
├── tickets/                   # Módulo de chamados (código-fonte)
│   ├── __init__.py
│   └── routes.py
│
├── docs/                      # Conteúdo em Markdown da documentação
│   ├── helpdesk/
│   │   ├── wifi.md
│   │   ├── impressora.md
│   │   └── computador-lento.md
│   └── seguranca/
│       ├── boas-praticas.md
│       ├── firewall.md
│       └── backup.md
│
├── lab/                        # Roteiro e instruções de laboratório virtual
│   ├── roteiro.md
│   ├── scripts-rede.md
│   └── videos/                 # Vídeos simulados (metadados apenas)
│
├── scripts/                    # Scripts de automação reais, prontos para uso
│   ├── powershell/
│   │   ├── limpar-cache.ps1
│   │   ├── verificar-disco.ps1
│   │   └── mapear-rede.ps1
│   └── batch/
│       ├── limpar-cache.bat
│       ├── verificar-disco.bat
│       └── mapear-rede.bat
│
├── templates/                  # Templates HTML (Jinja2 + Bootstrap 5)
│   ├── base.html
│   ├── index.html
│   ├── docs/
│   ├── tickets/
│   ├── lab/
│   ├── scripts/
│   └── security/
│
├── static/
│   ├── css/style.css
│   └── img/
│
└── instance/                   # Banco de dados SQLite (gerado automaticamente)
```

---

## 🚀 Instalação e execução

### Pré-requisitos
- Python 3.10 ou superior
- pip

### Passo a passo

```bash
# 1. Clone o repositório
git clone https://github.com/seu-usuario/portfolio-suporte-tecnico.git
cd portfolio-suporte-tecnico

# 2. Crie e ative um ambiente virtual (recomendado)
python -m venv venv

# Linux/Mac
source venv/bin/activate
# Windows
venv\Scripts\activate

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Execute a aplicação
python app.py
```

A aplicação estará disponível em: **http://127.0.0.1:5000**

O banco de dados SQLite (`instance/chamados.db`) é criado automaticamente na primeira execução — não é necessária nenhuma configuração adicional de banco de dados.

---

## 🧩 Detalhamento dos módulos

### 1. Documentação de Help Desk (`/docs`)
Guias em Markdown, renderizados dinamicamente em HTML, cobrindo os problemas mais comuns do dia a dia de suporte:
- **Wi-Fi não conecta** — diagnóstico de rede, comandos `ipconfig`, atualização de driver.
- **Impressora não imprime** — fila de spooler, driver, teste de impressão.
- **Computador lento** — uso de CPU/memória, limpeza de disco, malware, atualizações.

Cada guia conta com passo a passo numerado, blocos de código (comandos reais de PowerShell/CMD), tabelas de causas/soluções e "imagens simuladas" (placeholders visuais indicando onde entrariam capturas de tela reais).

### 2. Simulação de Chamados (`/chamados`)
Módulo CRUD completo, com persistência em banco de dados (SQLite via SQLAlchemy):
- Abertura de chamado com número sequencial automático (`TCK-0001`, `TCK-0002`, ...).
- Campos: usuário, problema, categoria, prioridade, status, técnico responsável e observações.
- Status possíveis: **Aberto**, **Em andamento**, **Resolvido**.
- Listagem com contadores e filtro por status.
- Endpoint JSON (`/chamados/api/chamados`) demonstrando integração via API REST.

### 3. Laboratório Virtual (`/laboratorio`)
- Roteiro detalhado para criação de VMs no **VirtualBox** e **VMware Workstation**.
- Orientações de configuração de rede (NAT, Bridge, Host-only).
- Scripts de configuração de rede, verificação de drivers e atualização de software.
- Cenários de teste sugeridos (réplica dos problemas do módulo de Help Desk em ambiente virtual).
- Área de vídeos demonstrativos **simulados** (metadados de título/duração/descrição — ver `lab/videos/README.md` para como evoluir para upload real).

### 4. Scripts de Automação (`/scripts`)
Scripts reais e funcionais, em duas linguagens, para as tarefas mais comuns de suporte:

| Script | PowerShell | Batch | Função |
|---|---|---|---|
| Limpar Cache | `limpar-cache.ps1` | `limpar-cache.bat` | Remove temporários, cache do Windows Update e esvazia a lixeira |
| Verificar Disco | `verificar-disco.ps1` | `verificar-disco.bat` | Relatório de espaço usado/livre por unidade, com alerta |
| Mapear Rede | `mapear-rede.ps1` | `mapear-rede.bat` | Mapeia uma unidade de rede compartilhada com letra fixa |

Todos os scripts podem ser **visualizados no navegador** ou **baixados diretamente** pela interface web.

### 5. Segurança Básica (`/seguranca/firewall`)
- Simulador interativo de regras de firewall (criação e remoção de regras fictícias — nome, porta, protocolo, direção, ação).
- Documentação de boas práticas (antivírus, firewall, senhas, atualizações).
- Documentação de rotina de backup seguindo a estratégia **3-2-1**, com exemplo de script `robocopy`.

> ⚠️ O simulador de firewall é **apenas educacional**: nenhuma regra é aplicada a um firewall real do sistema operacional.

---

## 🛠️ Tecnologias utilizadas

- **Python 3** + **Flask** — framework web
- **Flask-SQLAlchemy** — ORM / persistência dos chamados (SQLite)
- **Markdown** — renderização dos guias de documentação
- **Bootstrap 5** + **Font Awesome** — interface responsiva
- **PowerShell** e **Batch** — scripts de automação reais

---

## 📌 Possíveis evoluções futuras

- Autenticação de usuários (login de técnicos e administradores).
- Upload real de vídeos e imagens nos guias e no laboratório.
- Envio de e-mail automático ao abrir/atualizar um chamado.
- Dashboard com gráficos de indicadores (SLA, tempo médio de resolução).
- Deploy em nuvem (Render, Railway, Azure App Service, etc.).

---

## 👤 Autor

Projeto de portfólio desenvolvido para demonstração de competências técnicas na área de **Suporte Técnico / Help Desk / TI**, incluindo desenvolvimento web, automação e boas práticas de segurança.

## 📄 Licença

Este projeto é disponibilizado livremente para fins de estudo e uso em portfólio pessoal.
