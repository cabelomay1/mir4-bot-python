@echo off
REM ========================================
REM MIR4 BOT - Instalador e Executador
REM ========================================
REM Este arquivo faz tudo automaticamente:
REM 1. Verifica Python
REM 2. Instala dependências
REM 3. Executa o bot
REM ========================================

setlocal enabledelayedexpansion

echo.
echo ============================================================
echo    MIRROR MIR4 BOT - MISS}ES AUTOM}TICAS
echo    v1.0.0
echo ============================================================
echo.

REM Cores do console (simulado com modo cor)
color 0A

REM ==========================================
REM 1. VERIFICAR SE PYTHON EST} INSTALADO
REM ==========================================
echo [*] Verificando Python...
python --version >nul 2>&1

if %errorlevel% neq 0 (
    echo.
    echo [!] ERRO: Python n~o est} instalado!
    echo [!] 
    echo [!] Por favor, instale Python 3.8 ou superior em:
    echo [!] https://www.python.org/downloads/
    echo [!]
    echo [!] IMPORTANTE: Marque "Add Python to PATH" durante a instala‡~o!
    echo.
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo [v] Python encontrado: %PYTHON_VERSION%
echo.

REM ==========================================
REM 2. CRIAR PASTAS NECESS}RIAS
REM ==========================================
echo [*] Criando pastas necess}rias...

if not exist "logs" mkdir logs
if not exist "screenshots" mkdir screenshots

echo [v] Pastas criadas!
echo.

REM ==========================================
REM 3. VERIFICAR SE requirements.txt EXISTE
REM ==========================================
echo [*] Verificando arquivo requirements.txt...

if not exist "requirements.txt" (
    echo.
    echo [!] ERRO: Arquivo requirements.txt n~o encontrado!
    echo [!] Certifique-se de que est} na pasta correta.
    echo.
    pause
    exit /b 1
)

echo [v] requirements.txt encontrado!
echo.

REM ==========================================
REM 4. INSTALAR DEPENDÊNCIAS
REM ==========================================
echo [*] Instalando depend°ncias do Python...
echo [*] Isto pode levar alguns minutos...
echo.

python -m pip install --upgrade pip >nul 2>&1
python -m pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo [!] ERRO ao instalar dependências!
    echo [!] Verifique sua conexão com a internet.
    echo.
    pause
    exit /b 1
)

echo.
echo [v] Depend°ncias instaladas com sucesso!
echo.

REM ==========================================
REM 5. EXECUTAR O BOT
REM ==========================================
echo [*] Iniciando MIR4 BOT...
echo.

python main.py

if %errorlevel% neq 0 (
    echo.
    echo [!] Erro ao executar o bot!
    echo.
    pause
    exit /b 1
)

echo.
echo [v] Bot finalizado!
pause
exit /b 0
