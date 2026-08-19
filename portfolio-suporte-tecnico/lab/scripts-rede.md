## Scripts utilizados no laboratório virtual

Estes scripts complementam o roteiro do laboratório e podem ser executados dentro das máquinas virtuais de teste.

### Configuração de rede — definir IP estático (Windows)

```powershell
New-NetIPAddress -InterfaceAlias "Ethernet" -IPAddress 192.168.1.50 -PrefixLength 24 -DefaultGateway 192.168.1.1
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ServerAddresses ("8.8.8.8","8.8.4.4")
```

### Configuração de rede — voltar para DHCP

```powershell
Set-NetIPInterface -InterfaceAlias "Ethernet" -Dhcp Enabled
Set-DnsClientServerAddress -InterfaceAlias "Ethernet" -ResetServerAddresses
```

### Instalação de drivers (verificação de dispositivos com problema)

```powershell
Get-PnpDevice | Where-Object { $_.Status -eq "Error" } | Select-Object FriendlyName, InstanceId, Status
```

Após identificar o dispositivo, utilize o Gerenciador de Dispositivos ou o driver oficial do fabricante para reinstalar.

### Atualização de software em lote (Windows Package Manager)

```powershell
# Lista todos os softwares desatualizados
winget upgrade

# Atualiza todos os softwares de uma vez, sem interação
winget upgrade --all --silent --accept-package-agreements --accept-source-agreements
```

### Teste de conectividade básica

```powershell
Test-Connection -ComputerName 8.8.8.8 -Count 4
Test-NetConnection -ComputerName google.com -Port 443
```

> Estes scripts também estão disponíveis, prontos para download, no módulo **Scripts de Automação**.
