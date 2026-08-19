## Sintoma relatado pelo usuário

> "Meu computador está muito lento para abrir programas e navegar."

<div class="simulated-image">🖼️ [Imagem simulada] Gerenciador de Tarefas mostrando alto uso de CPU/Memória</div>

## Diagnóstico passo a passo

### 1. Verificar uso de CPU, memória e disco

Abra o **Gerenciador de Tarefas** (`Ctrl + Shift + Esc`) e identifique processos consumindo recursos excessivos.

### 2. Verificar espaço livre em disco

Discos quase cheios (especialmente HDs/SSDs do sistema) impactam diretamente a performance.

```powershell
Get-PSDrive -PSProvider FileSystem | Select-Object Name, @{N="LivreGB";E={[math]::Round($_.Free/1GB,2)}}
```

### 3. Verificar programas de inicialização

Muitos aplicativos abrindo junto com o Windows aumentam o tempo de boot e o consumo de memória.

```
Gerenciador de Tarefas > Aba Inicializar > Desabilitar itens desnecessários
```

### 4. Executar limpeza de disco e cache

Utilize o script de automação `limpar-cache` (disponível no módulo **Scripts de Automação**) para remover arquivos temporários.

### 5. Verificar presença de malware

Execute uma varredura completa com o antivírus corporativo antes de prosseguir com outras otimizações.

### 6. Verificar atualizações pendentes do sistema

Sistemas desatualizados podem apresentar lentidão e problemas de compatibilidade.

```
Configurações > Windows Update > Verificar atualizações
```

### 7. Verificar fragmentação/saúde do disco (HDDs)

```powershell
Optimize-Volume -DriveLetter C -Analyze -Verbose
```

> Não execute desfragmentação em unidades SSD — utilize apenas o comando `TRIM`, já gerenciado automaticamente pelo Windows.

## Soluções mais comuns (resumo)

| Causa provável                        | Solução                                              |
|-----------------------------------------|--------------------------------------------------------|
| Muitos programas na inicialização       | Desabilitar itens desnecessários                        |
| Disco quase cheio                       | Executar limpeza de disco/cache                          |
| Malware ou processo suspeito            | Executar varredura completa do antivírus                 |
| Sistema desatualizado                   | Aplicar atualizações pendentes                            |
| Hardware insuficiente (RAM/HD antigo)   | Avaliar upgrade de memória RAM ou migração para SSD       |

## Escalonamento

Se, após os passos acima, o desempenho continuar inadequado, registre um chamado categorizado como **Hardware**, anexando um print do Gerenciador de Tarefas e as especificações do equipamento (RAM, tipo de disco, modelo).
