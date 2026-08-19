@echo off
REM ============================================================
REM  Mapeamento de Unidade de Rede
REM  Portfolio - Analista de Suporte Tecnico
REM  Ajuste as variaveis abaixo conforme o ambiente antes de usar
REM ============================================================

set LETRA=Z:
set CAMINHO=\\servidor\compartilhamento

echo ===== Mapeamento de Unidade de Rede =====

echo Removendo mapeamento anterior de %LETRA% (se existir)...
net use %LETRA% /delete /y >nul 2>&1

echo Mapeando %CAMINHO% como %LETRA% ...
net use %LETRA% %CAMINHO% /persistent:yes

if %ERRORLEVEL% EQU 0 (
    echo [OK] Unidade mapeada com sucesso.
) else (
    echo [ERRO] Falha ao mapear a unidade de rede. Verifique o caminho e as permissoes.
)

echo ===== Fim do mapeamento =====
pause
