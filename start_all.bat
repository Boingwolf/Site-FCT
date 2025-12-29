@echo off
title AromaWake - Servidores
color 0A

echo.
echo ========================================
echo    AROMAWAKE - Iniciando Servidores
echo ========================================
echo.

echo [1/2] Iniciando Backend (API)...
echo       Porta: 5000
start "Backend API" cmd /k "cd backend && venv\Scripts\activate && python api.py"

echo.
timeout /t 2 /nobreak >nul

echo [2/2] Iniciando Frontend (HTML)...
echo       Porta: 8000
start "Frontend Server" cmd /k "cd backend && venv\Scripts\activate && python server_frontend.py"

echo.
echo ========================================
echo    SERVIDORES INICIADOS!
echo ========================================
echo.
echo  Backend (API):  http://localhost:5000
echo  Frontend (Web): http://localhost:8000
echo.
echo ========================================
echo.
echo Podes fechar esta janela.
echo Para parar os servidores, fecha as outras janelas.
echo.
pause