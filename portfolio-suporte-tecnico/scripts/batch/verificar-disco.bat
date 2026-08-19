@echo off
REM ============================================================
REM  Relatorio de Espaco em Disco
REM  Portfolio - Analista de Suporte Tecnico
REM ============================================================

echo ===== Relatorio de Espaco em Disco =====
echo.

wmic logicaldisk get Caption,VolumeName,FreeSpace,Size

echo.
echo Dica: divida FreeSpace por Size e multiplique por 100 para
echo obter o percentual de espaco livre de cada unidade.
echo.
echo ===== Fim do relatorio =====
pause
