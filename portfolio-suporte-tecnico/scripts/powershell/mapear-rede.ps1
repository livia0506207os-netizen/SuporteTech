<#
.SINOPSE
    Mapeia automaticamente uma unidade de rede compartilhada com letra de drive fixa.

.DESCRICAO
    Script de automacao para o portfolio de Suporte Tecnico.
    Edite as variaveis abaixo conforme o ambiente antes de executar.

.USO
    PS> .\mapear-rede.ps1
#>

# ==== CONFIGURACOES (ajustar conforme o ambiente) ====
$letraUnidade = "Z:"
$caminhoRede  = "\\servidor\compartilhamento"
$persistente  = $true
# =======================================================

Write-Host "===== Mapeamento de Unidade de Rede =====" -ForegroundColor Cyan

# Remove o mapeamento anterior, se existir, para evitar conflito
if (Test-Path $letraUnidade) {
    Write-Host "Removendo mapeamento anterior de $letraUnidade..." -ForegroundColor Yellow
    net use $letraUnidade /delete /y | Out-Null
}

try {
    if ($persistente) {
        New-PSDrive -Name ($letraUnidade.TrimEnd(":")) -PSProvider FileSystem -Root $caminhoRede -Persist -ErrorAction Stop
    } else {
        New-PSDrive -Name ($letraUnidade.TrimEnd(":")) -PSProvider FileSystem -Root $caminhoRede -ErrorAction Stop
    }
    Write-Host "[OK] Unidade $caminhoRede mapeada com sucesso como $letraUnidade" -ForegroundColor Green
}
catch {
    Write-Host "[ERRO] Nao foi possivel mapear a unidade de rede: $_" -ForegroundColor Red
}

Write-Host "===== Fim do mapeamento =====" -ForegroundColor Cyan
