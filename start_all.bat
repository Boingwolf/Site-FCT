@echo off
title AromaWake - Servidores
color 0A

echo.
echo ========================================
echo    AROMAWAKE - Iniciando Servidores
echo ========================================
echo.

REM Verificar se o venv existe
if not exist "backend\venv\" (
    echo [!] Ambiente virtual nao encontrado!
    echo [*] Criando ambiente virtual...
    cd backend
    python -m venv venv
    if errorlevel 1 (
        echo [ERRO] Falha ao criar venv. Certifica-te que Python esta instalado.
        pause
        exit /b 1
    )
    
    echo [*] Instalando dependencias...
    call venv\Scripts\activate
    pip install -r requirements.txt
    if errorlevel 1 (
        echo [ERRO] Falha ao instalar dependencias.
        pause
        exit /b 1
    )
    cd ..
    echo [OK] Ambiente configurado com sucesso!
    echo.
)

echo [1/2] Iniciando Backend API...
echo       Porta: 5000
start "Backend API" cmd /k "cd backend && venv\Scripts\activate && python api.py"

echo.
timeout /t 2 /nobreak >nul

echo [2/2] Iniciando Frontend Server...
echo       Porta: 8000
start "Frontend Server" cmd /k "cd backend && venv\Scripts\activate && python server_frontend.py"

echo.
echo ========================================
echo    SERVIDORES INICIADOS COM SUCESSO!
echo ========================================
echo.
echo  Backend API:    http://localhost:5000
echo  Frontend Web:   http://localhost:8000
echo.
echo ========================================
echo.
echo Podes fechar esta janela.
echo Para parar os servidores, fecha as janelas abertas.
echo.
pause