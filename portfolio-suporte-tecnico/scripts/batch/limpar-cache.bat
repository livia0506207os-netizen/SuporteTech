@echo off
REM ============================================================
REM  Limpeza de Cache e Arquivos Temporarios
REM  Portfolio - Analista de Suporte Tecnico
REM  Executar como Administrador
REM ============================================================

echo ===== Limpeza de Cache e Arquivos Temporarios =====

echo Limpando pasta TEMP do usuario...
del /q /f /s "%TEMP%\*" >nul 2>&1
echo [OK] Pasta TEMP do usuario limpa.

echo Limpando pasta TEMP do Windows...
del /q /f /s "C:\Windows\Temp\*" >nul 2>&1
echo [OK] Pasta TEMP do Windows limpa.

echo Limpando cache do Windows Update...
net stop wuauserv >nul 2>&1
del /q /f /s "C:\Windows\SoftwareDistribution\Download\*" >nul 2>&1
net start wuauserv >nul 2>&1
echo [OK] Cache do Windows Update limpo.

echo Esvaziando a lixeira...
rd /s /q C:\$Recycle.Bin >nul 2>&1
echo [OK] Lixeira esvaziada.

echo ===== Limpeza concluida! =====
pause
