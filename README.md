# Site FCT - AromaWake 🌟

> Website de e-commerce para o produto fictício "AromaWake"

## 🚀 Links do Projeto

| Tipo | URL | Status |
|------|-----|--------|
| **🌐 Website** | [boingwolf.github.io/Site-FCT](https://boingwolf.github.io/Site-FCT/) | ![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-online-success) |
| **🔌 API** | [site-fct.onrender.com](https://site-fct.onrender.com/) | ![Render](https://img.shields.io/badge/Render-online-success) |

## 📸 Sobre o Projeto

Projeto full-stack educacional desenvolvido no âmbito da FCT (Formação em Contexto de Trabalho). Simula um sistema de e-commerce para o produto fictício "AromaWake", incluindo gestão de mensagens de contacto.

## 🛠️ Tech Stack

### Backend
- **Python 3.8+** - Linguagem principal
- **Flask** - Framework web e API REST
- **SQLite** - Base de dados
- **Render** - Hosting e deployment

### Frontend
- **HTML5, CSS3, JavaScript** - Interface do utilizador
- **Integração REST API** - Comunicação com backend

## 📋 API Endpoints

**Base URL:** `https://site-fct.onrender.com`

### Contactos
```http
POST /api/contacto
Content-Type: application/json

{
  "nome": "Maria Santos",
  "email": "maria@example.com",
  "assunto": "Informações",
  "mensagem": "Gostaria de saber mais..."
}
```

```http
GET /api/contactos
```
Retorna lista de todas as mensagens de contacto (acesso admin).

## 📁 Estrutura do Projeto

```
Site-FCT/
├── backend/              # API Flask
│   ├── app.py           # Aplicação principal
│   ├── database.py      # Configuração da BD
│   ├── routes/          # Endpoints da API
│   │   └── ...
│   ├── requirements.txt # Dependências Python
│   └── server_frontend.py
├── codigo/              # Frontend
│   ├── HTML, CSS, JS
│   └── assets/
└── start_all.bat       # Script de início (dev local)
```

## 🌐 Deployment

### Backend (Render)
A API está hospedada no **Render** com deploy automático:
- Push para `main` → Deploy automático
- URL de produção: https://site-fct.onrender.com/
- Logs e monitorização através do dashboard Render

### Frontend (GitHub Pages)
O website está hospedado no **GitHub Pages**:
- URL de produção: https://boingwolf.github.io/Site-FCT/
- Deploy automático via Actions do GitHub
- Integração com API Render via CORS configurado

## 👥 Equipa

| Papel | Desenvolvedor | GitHub |
|-------|--------------|--------|
| **Backend & API** | Santiago Costa | [@Its-SMAC](https://github.com/Its-SMAC) |
| **Frontend & Design** | Guilherme Eusébio | [@Boingwolf](https://github.com/Boingwolf) |

## 💻 Desenvolvimento Local

<details>
<summary>Setup local (apenas para desenvolvimento)</summary>

### Requisitos
- Python 3.8 ou superior
- Git

### Instalação Rápida (Windows)
```bash
git clone 
cd Site-FCT
start_all.bat
```

O script vai automaticamente:
- Criar ambiente virtual
- Instalar dependências do `requirements.txt`
- Inicializar base de dados
- Iniciar servidores backend e frontend

### Acesso Local
- **Frontend:** http://localhost:8000
- **API Backend:** http://localhost:5000

### Instalação Manual

Se o script automático não funcionar:

```bash
# Backend
cd backend
python -m venv venv
venv\Scripts\activate  # Windows
# source venv/bin/activate  # Linux/Mac
pip install -r requirements.txt
python database.py
python app.py
```

Em outro terminal:
```bash
# Servidor Frontend
cd backend
python server_frontend.py
```

</details>

## 📝 Notas

- A API em produção usa SQLite para persistência de dados
- Frontend integra com API através de chamadas AJAX
- Sistema preparado para escalar com PostgreSQL se necessário

## 🔒 Segurança

- Validação de inputs nos endpoints
- CORS configurado para domínios autorizados
- Rate limiting implementado no Render

---

**Desenvolvido como projeto de FCT (Formação em Contexto de Trabalho)**
