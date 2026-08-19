## Sintoma relatado pelo usuário

> "Meu notebook não consegue se conectar ao Wi-Fi do escritório."

## Diagnóstico passo a passo

### 1. Verificar se o Wi-Fi está habilitado

Confirme se o adaptador de rede sem fio está ativado no sistema operacional e se não há uma tecla física (Fn) desabilitando o rádio Wi-Fi.

```
Painel de Controle > Rede e Internet > Central de Rede e Compartilhamento > Alterar configurações do adaptador
```

Verifique se o ícone do adaptador Wi-Fi não está acinzentado ("Desabilitado").

### 2. Verificar se a rede correta está sendo selecionada

Confirme com o usuário o SSID correto da rede corporativa e certifique-se de que ele não está tentando conectar a uma rede de convidados ou a um SSID antigo salvo no dispositivo.

<div class="simulated-image">🖼️ [Imagem simulada] Tela de configurações de Wi-Fi &mdash; opção "Esquecer rede"</div>

### 3. Esquecer e reconectar a rede

1. Acesse as configurações de Wi-Fi do sistema.
2. Selecione a rede e clique em **Esquecer**.
3. Reconecte digitando novamente a senha.

### 4. Reiniciar o adaptador de rede

```powershell
# PowerShell (executar como Administrador)
Disable-NetAdapter -Name "Wi-Fi" -Confirm:$false
Start-Sleep -Seconds 5
Enable-NetAdapter -Name "Wi-Fi" -Confirm:$false
```

### 5. Liberar e renovar o IP

```
ipconfig /release
ipconfig /flushdns
ipconfig /renew
```

### 6. Atualizar o driver do adaptador de rede

Acesse o **Gerenciador de Dispositivos**, localize o adaptador de rede sem fio, clique com o botão direito e selecione **Atualizar driver**.

### 7. Verificar o roteador / ponto de acesso

- Confirme se outros dispositivos conseguem se conectar normalmente (isola o problema entre estação x infraestrutura).
- Reinicie o roteador/access point, se necessário.
- Verifique se há limite de dispositivos conectados atingido.

## Soluções mais comuns (resumo)

| Causa provável                         | Solução                                           |
|----------------------------------------|----------------------------------------------------|
| Adaptador de rede desabilitado          | Habilitar o adaptador nas configurações de rede    |
| Senha da rede incorreta ou desatualizada| Esquecer a rede e reconectar com a senha correta   |
| Driver de rede desatualizado/corrompido | Atualizar ou reinstalar o driver                   |
| Endereço IP conflitante                 | Renovar o IP via `ipconfig /renew`                 |
| Roteador com falha                      | Reiniciar o roteador/access point                  |

## Escalonamento

Se após todos os passos acima o problema persistir, abra um chamado categorizado como **Rede** com prioridade **Alta**, informando:

- Modelo do notebook/desktop.
- Sistema operacional e versão.
- Se o problema ocorre em outras redes também.
- Log de erro (se disponível em `Visualizador de Eventos`).
