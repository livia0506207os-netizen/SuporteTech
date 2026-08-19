[README (4).md](https://github.com/user-attachments/files/31237653/README.4.md)
# Portfólio de Analista de Suporte Técnico

Projeto desenvolvido para apresentar, de forma prática e organizada, conhecimentos e habilidades relacionados à área de Suporte Técnico e Help Desk.

O sistema reúne documentação técnica, simulação de chamados, laboratório virtual, scripts de automação e um projeto de segurança básica em uma única aplicação web.

## Sobre o Projeto

O **SuporteTech** é uma aplicação web desenvolvida com Python e Flask, estruturada em módulos independentes. A proposta é transformar conhecimentos de suporte técnico em exemplos práticos que possam ser consultados, executados e demonstrados em um ambiente de portfólio.

A aplicação possui uma página inicial com informações sobre os chamados registrados e integra diferentes módulos por meio de Blueprints do Flask. O projeto utiliza banco de dados SQLite para armazenar os chamados e organiza seus recursos em pastas específicas para documentação, laboratório, automação, segurança, templates e arquivos estáticos.

## Módulos

### Documentação de Help Desk

Reúne conteúdos e materiais relacionados ao atendimento de usuários, procedimentos de suporte e resolução de problemas comuns de TI.

### Simulação de Chamados

Permite trabalhar com uma representação prática de chamados de suporte, incluindo informações de quantidade, status e resolução.

### Laboratório Virtual

Área destinada à demonstração de atividades práticas e cenários de laboratório relacionados ao suporte técnico.

### Scripts de Automação

Reúne scripts voltados à automação de tarefas que podem fazer parte da rotina de um profissional de suporte técnico.

### Projeto de Segurança Básica

Apresenta uma área dedicada a conceitos e práticas introdutórias de segurança da informação aplicáveis ao ambiente de suporte técnico.

## Tecnologias Utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- SQLite
- Markdown
- python-dotenv
- HTML e CSS
- Arquitetura modular com Blueprints

## Como Instalar e Executar

### 1. Clonar o repositório

```bash
git clone https://github.com/livia0506207os-netizen/Suporte.git
cd Suporte/portfolio-suporte-tecnico
```

### 2. Criar um ambiente virtual

No Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

No Linux/macOS:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a aplicação

```bash
python app.py
```

### 5. Acessar no navegador

```text
http://localhost:5000
```

## Estrutura do Projeto

```text
Suporte/
└── portfolio-suporte-tecnico/
    ├── app.py
    ├── config.py
    ├── models.py
    ├── requirements.txt
    ├── .gitignore
    ├── README.md
    │
    ├── blueprints/
    │   ├── docs_bp.py
    │   ├── lab_bp.py
    │   ├── scripts_bp.py
    │   └── security_bp.py
    │
    ├── docs/
    │   └── Documentação de Help Desk
    │
    ├── instance/
    │   └── Banco de dados SQLite
    │
    ├── lab/
    │   └── Laboratório Virtual
    │
    ├── scripts/
    │   └── Scripts de Automação
    │
    ├── static/
    │   └── Arquivos estáticos
    │
    ├── templates/
    │   └── Páginas HTML
    │
    └── tickets/
        └── Simulação de Chamados
```

## Objetivo do Projeto

O principal objetivo é demonstrar **habilidades práticas em suporte técnico**, indo além da apresentação de conhecimentos teóricos.

O projeto busca evidenciar competências como:

- Atendimento e organização de chamados;
- Documentação de procedimentos técnicos;
- Identificação e resolução de problemas;
- Organização de rotinas de Help Desk;
- Automação de tarefas por meio de scripts;
- Noções de segurança da informação;
- Desenvolvimento e manutenção de aplicações web;
- Organização de projetos utilizando uma estrutura modular;
- Uso de banco de dados para armazenamento de informações.

Dessa forma, o projeto funciona como um portfólio profissional para demonstrar conhecimentos aplicáveis à rotina de um Analista de Suporte Técnico.

## Status do Projeto

Projeto em desenvolvimento e evolução contínua, com possibilidade de inclusão de novos cenários de suporte, documentações, scripts e atividades práticas.

## Créditos

Desenvolvido por **Lívia**.

Repositório:

https://github.com/livia0506207os-netizen/Suporte
