## Sintoma relatado pelo usuário

> "Enviei o documento para impressão, mas nada sai da impressora."

<div class="simulated-image">🖼️ [Imagem simulada] Fila de impressão do Windows travada</div>

## Diagnóstico passo a passo

### 1. Verificar conexões físicas e energia

- Confirme que a impressora está ligada e sem indicadores de erro (luzes piscando).
- Verifique o cabo USB ou a conexão de rede/Wi-Fi da impressora.

### 2. Verificar se a impressora está definida como padrão

```
Painel de Controle > Dispositivos e Impressoras
```

Clique com o botão direito na impressora correta e selecione **Definir como impressora padrão**.

### 3. Limpar a fila de impressão travada

Documentos travados na fila costumam impedir novas impressões.

```powershell
# PowerShell (executar como Administrador)
Stop-Service -Name Spooler -Force
Remove-Item "C:\Windows\System32\spool\PRINTERS\*" -Force
Start-Service -Name Spooler
```

### 4. Verificar níveis de tinta/toner e papel

Confirme visualmente (ou pelo utilitário do fabricante) se há suprimento suficiente e papel na bandeja.

### 5. Reinstalar ou atualizar o driver da impressora

1. Remova a impressora em **Dispositivos e Impressoras**.
2. Baixe o driver mais recente do site do fabricante.
3. Reinstale e realize um teste de impressão.

### 6. Testar em outra estação

Se possível, tente imprimir a partir de outro computador na mesma rede para isolar se o problema é da impressora ou da estação do usuário.

## Soluções mais comuns (resumo)

| Causa provável                    | Solução                                             |
|------------------------------------|------------------------------------------------------|
| Fila de impressão travada          | Reiniciar o serviço de Spooler e limpar a fila       |
| Impressora errada definida         | Definir a impressora correta como padrão             |
| Driver corrompido ou desatualizado | Reinstalar/atualizar o driver                        |
| Sem papel ou toner                 | Repor suprimentos                                    |
| Problema de conectividade de rede  | Verificar IP/Wi-Fi da impressora                      |

## Escalonamento

Caso o problema persista, abra um chamado categorizado como **Impressora**, informando modelo do equipamento, tipo de conexão (USB/Rede) e mensagens de erro exibidas no painel da impressora.
