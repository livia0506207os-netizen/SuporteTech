<#
.SINOPSE
    Limpa arquivos temporários e cache do sistema para liberar espaço em disco.

.DESCRICAO
    Script de automação para o portfólio de Suporte Técnico.
    Remove arquivos temporários do usuário, do sistema e limpa a lixeira.

.USO
    Executar como Administrador:
    PS> .\limpar-cache.ps1
#>

Write-Host "===== Limpeza de Cache e Arquivos Temporarios =====" -ForegroundColor Cyan

function Remove-Safely {
    param (
        [string]$Caminho
    )
    if (Test-Path $Caminho) {
        try {
            Remove-Item -Path "$Caminho\*" -Recurse -Force -ErrorAction SilentlyContinue
            Write-Host "[OK] Limpo: $Caminho" -ForegroundColor Green
        }
        catch {
            Write-Host "[AVISO] Alguns arquivos nao puderam ser removidos em: $Caminho" -ForegroundColor Yellow
        }
    }
}

# Pasta de temporarios do usuario
Remove-Safely -Caminho $env:TEMP

# Pasta de temporarios do Windows
Remove-Safely -Caminho "C:\Windows\Temp"

# Cache do Windows Update (opcional - libera bastante espaco)
Write-Host "Limpando cache do Windows Update..." -ForegroundColor Cyan
Stop-Service -Name wuauserv -Force -ErrorAction SilentlyContinue
Remove-Safely -Caminho "C:\Windows\SoftwareDistribution\Download"
Start-Service -Name wuauserv -ErrorAction SilentlyContinue

# Esvaziar a lixeira
Write-Host "Esvaziando a lixeira..." -ForegroundColor Cyan
Clear-RecycleBin -Force -ErrorAction SilentlyContinue

Write-Host "===== Limpeza concluida! =====" -ForegroundColor Green
