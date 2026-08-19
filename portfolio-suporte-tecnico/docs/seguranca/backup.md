## Objetivo

Definir uma rotina de backup simples e confiável para estações de trabalho e servidores de pequeno porte.

<div class="simulated-image">🖼️ [Imagem simulada] Agendador de Tarefas do Windows configurando rotina de backup</div>

## Estratégia 3-2-1

- **3** cópias dos dados (1 original + 2 backups).
- **2** mídias de armazenamento diferentes (ex.: disco local + nuvem, ou disco local + NAS).
- **1** cópia armazenada fora do local físico principal (offsite / nuvem).

## Tipos de backup

| Tipo         | Descrição                                                        | Quando usar                          |
|--------------|--------------------------------------------------------------------|----------------------------------------|
| Completo     | Copia todos os dados selecionados                                   | Semanalmente / mensalmente             |
| Incremental  | Copia apenas o que mudou desde o último backup (completo ou incremental) | Diariamente                       |
| Diferencial  | Copia tudo que mudou desde o último backup completo                 | Alternativa ao incremental             |

## Exemplo de rotina recomendada (estação de usuário)

1. **Backup incremental diário** dos documentos do usuário (Desktop, Documentos, Downloads) às 19h.
2. **Backup completo semanal** aos sábados às 02h.
3. Retenção: manter os últimos 30 dias de backups incrementais e 3 backups completos.
4. Cópia sincronizada para armazenamento em nuvem corporativo.

## Exemplo de agendamento via PowerShell (robocopy)

```powershell
# Backup incremental simples de uma pasta de usuário para um destino de rede
robocopy "C:\Users\usuario\Documents" "\\servidor\backups\usuario\Documents" /MIR /R:3 /W:5 /LOG:C:\logs\backup.log
```

Parâmetros utilizados:
- `/MIR` — espelha a pasta de origem no destino (inclui exclusões).
- `/R:3` — tenta novamente 3 vezes em caso de falha.
- `/W:5` — aguarda 5 segundos entre tentativas.
- `/LOG` — grava um log da execução.

## Testes de restauração

Um backup só é considerado válido após ser **testado**. Recomenda-se:

- Testar a restauração de uma amostra de arquivos mensalmente.
- Documentar o resultado do teste (data, arquivos restaurados, sucesso/falha).
- Revisar o plano de backup sempre que houver mudança significativa na infraestrutura.

## Checklist da rotina de backup

- [ ] Job de backup agendado e ativo
- [ ] Destino de backup com espaço suficiente
- [ ] Cópia offsite/nuvem configurada
- [ ] Log de execução sendo monitorado
- [ ] Teste de restauração realizado no último mês
