<#
.SINOPSE
    Gera um relatorio do espaco utilizado e disponivel em cada unidade de disco.

.DESCRICAO
    Script de automacao para o portfolio de Suporte Tecnico.
    Exibe um relatorio no console e emite um alerta caso alguma unidade
    esteja com menos de 15% de espaco livre.

.USO
    PS> .\verificar-disco.ps1
#>

Write-Host "===== Relatorio de Espaco em Disco =====" -ForegroundColor Cyan

$unidades = Get-PSDrive -PSProvider FileSystem | Where-Object { $_.Used -ne $null }

$relatorio = foreach ($u in $unidades) {
    $totalGB  = [math]::Round(($u.Used + $u.Free) / 1GB, 2)
    $livreGB  = [math]::Round($u.Free / 1GB, 2)
    $usadoGB  = [math]::Round($u.Used / 1GB, 2)
    $percLivre = if ($totalGB -gt 0) { [math]::Round(($livreGB / $totalGB) * 100, 1) } else { 0 }

    [PSCustomObject]@{
        Unidade        = $u.Name
        "Total (GB)"   = $totalGB
        "Usado (GB)"   = $usadoGB
        "Livre (GB)"   = $livreGB
        "% Livre"      = $percLivre
    }
}

$relatorio | Format-Table -AutoSize

foreach ($linha in $relatorio) {
    if ($linha."% Livre" -lt 15) {
        Write-Host "[ALERTA] Unidade $($linha.Unidade): apenas $($linha.'% Livre')% de espaco livre!" -ForegroundColor Red
    }
}

Write-Host "===== Fim do relatorio =====" -ForegroundColor Cyan
