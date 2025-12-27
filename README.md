# Site FCT

Site do AromaWake de FCT

## 🚀 Como Executar

### Requisitos

- Python 3.8 ou superior
- Git

### Instalação Rápida

1. Clonar o repositório:

```bash
git clone <url-do-repo>
cd Site-FCT
```

2. Executar (Windows):

```bash
start_all.bat
```

O script vai automaticamente:

- Criar ambiente virtual
- Instalar dependências
- Iniciar servidores

### Acesso

- **Frontend:** http://localhost:8000
- **API Backend:** http://localhost:5000

### Instalação Manual

Se o script não funcionar:

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python database.py
python app.py  # Terminal 1
python server_frontend.py  # Terminal 2
```

## 📁 Estrutura

```
Site-FCT/
├── backend/         # API Flask + Servidor Frontend
├── codigo/          # HTML, CSS, JS
└── start_all.bat    # Script de início automático
```

## 👥 Equipa

- **Backend + Integração:** Santiago Costa
- **Frontend + Design:** Guilherme Eusébio

## 📋 API Endpoints

- `POST /api/formulario` - Criar formulário de interesse
- `GET /api/formularios` - Listar formulários
- `POST /api/contacto` - Enviar mensagem de contacto
- `GET /api/contactos` - Listar contactos
