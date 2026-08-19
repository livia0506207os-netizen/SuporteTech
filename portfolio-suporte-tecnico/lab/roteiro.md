## Objetivo do laboratório

Simular, em um ambiente seguro e isolado, cenários reais de suporte técnico (falha de rede, drivers, atualização de software) usando máquinas virtuais.

## Pré-requisitos

- **VirtualBox** (gratuito) ou **VMware Workstation Player**.
- Imagem ISO do sistema operacional a ser testado (ex.: Windows 10/11, Ubuntu).
- Mínimo recomendado: 4 GB de RAM disponíveis para a VM e 40 GB de disco.

## Passo 1 — Criar a máquina virtual (VirtualBox)

1. Abra o VirtualBox e clique em **Nova**.
2. Defina nome, tipo (Windows/Linux) e versão do sistema operacional.
3. Aloque memória RAM (recomendado: 4096 MB para Windows, 2048 MB para Linux leve).
4. Crie um disco virtual novo, do tipo **VDI**, com alocação dinâmica (mínimo 40 GB).
5. Em **Configurações > Sistema**, habilite pelo menos 2 processadores virtuais, se disponível.
6. Em **Configurações > Armazenamento**, monte a ISO do sistema operacional na unidade óptica virtual.
7. Inicie a VM e siga o processo normal de instalação do sistema operacional.

## Passo 2 — Criar a máquina virtual (VMware Workstation)

1. Clique em **Create a New Virtual Machine**.
2. Selecione **Typical (recommended)** e aponte para o arquivo ISO.
3. Defina nome e localização da VM.
4. Configure o tamanho do disco (recomendado: 40-60 GB, "Store virtual disk as a single file" para simplicidade).
5. Finalize e inicie a instalação do sistema operacional.

## Passo 3 — Configuração de rede da VM

| Modo de rede         | Quando usar                                                       |
|-----------------------|---------------------------------------------------------------------|
| NAT                   | Acesso à internet sem expor a VM à rede local (padrão para testes)  |
| Bridge (Em ponte)     | A VM recebe IP da rede local, útil para testar cenários de rede real|
| Somente Host-Only     | Comunicação isolada apenas entre host e VM                          |

Para simular problemas de conectividade (como no guia **Wi-Fi não conecta**), recomenda-se o modo **Bridge**, pois aproxima o comportamento da VM de uma estação real na rede.

## Passo 4 — Instalação de drivers

Após a instalação do sistema operacional:

1. No VirtualBox, instale o **Guest Additions** (`Dispositivos > Inserir imagem de CD das Guest Additions`).
2. No VMware, instale o **VMware Tools**.
3. Isso garante drivers de vídeo, mouse e rede adequados para a VM, evitando falsos positivos de "driver ausente" durante os testes.

## Passo 5 — Atualização de software na VM

Utilize os scripts do módulo **Scripts de Automação** para simular rotinas reais de atualização:

```powershell
# Exemplo simplificado de atualização de aplicativos via winget
winget upgrade --all --silent
```

## Passo 6 — Cenários de teste sugeridos

1. **Falha de Wi-Fi/rede** — desabilitar o adaptador de rede da VM e seguir o guia de Help Desk correspondente.
2. **Impressora não imprime** — instalar uma impressora virtual (ex.: Microsoft Print to PDF) e simular fila travada.
3. **Computador lento** — limitar a RAM/CPU da VM propositalmente e aplicar o roteiro de otimização.
4. **Configuração de firewall** — aplicar regras de firewall na VM e validar bloqueios/liberações de porta.

## Boas práticas de laboratório

- Utilize **snapshots** antes de cada teste, permitindo reverter a VM ao estado anterior rapidamente.
- Documente cada cenário testado (o que foi feito, o que foi observado, solução aplicada).
- Nunca utilize a VM de laboratório para armazenar dados sensíveis reais.
