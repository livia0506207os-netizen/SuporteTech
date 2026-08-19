## O que é este documento

Este guia descreve, em nível conceitual, como regras de firewall são estruturadas, e referencia o **simulador interativo** disponível no sistema (`/seguranca/firewall`) usado para fins de demonstração e aprendizado.

<div class="simulated-image">🖼️ [Imagem simulada] Painel do Firewall do Windows Defender com regras de entrada</div>

## Estrutura de uma regra de firewall

Toda regra de firewall, seja no Windows Defender Firewall, em um firewall de borda ou em `iptables`, geralmente é composta por:

| Campo       | Descrição                                              |
|-------------|-----------------------------------------------------------|
| Nome        | Identificação da regra                                    |
| Direção     | Entrada (Inbound) ou Saída (Outbound)                      |
| Protocolo   | TCP, UDP, ICMP, etc.                                       |
| Porta       | Porta ou intervalo de portas afetado                        |
| Ação        | Permitir ou Bloquear                                        |
| Escopo      | Endereços IP/redes de origem ou destino                     |

## Exemplo — Windows Defender Firewall (PowerShell)

```powershell
# Bloquear a porta 23 (Telnet) de entrada
New-NetFirewallRule -DisplayName "Bloquear Telnet" -Direction Inbound -Protocol TCP -LocalPort 23 -Action Block

# Permitir HTTPS de entrada
New-NetFirewallRule -DisplayName "Permitir HTTPS" -Direction Inbound -Protocol TCP -LocalPort 443 -Action Allow
```

## Exemplo — Linux (iptables)

```bash
# Bloquear porta 23 (Telnet)
sudo iptables -A INPUT -p tcp --dport 23 -j DROP

# Permitir porta 443 (HTTPS)
sudo iptables -A INPUT -p tcp --dport 443 -j ACCEPT
```

## Boas práticas ao configurar regras

1. Sempre parta do princípio de **negar tudo por padrão** e liberar apenas o necessário.
2. Documente cada regra criada (motivo, solicitante, data).
3. Evite regras amplas demais (ex.: liberar todas as portas para um IP).
4. Revise regras obsoletas periodicamente.
5. Teste em ambiente de laboratório antes de aplicar em produção (ver módulo **Laboratório Virtual**).

## Simulador de regras

O sistema conta com uma página de simulação onde é possível cadastrar regras fictícias de firewall (nome, porta, protocolo, ação e direção), útil para fins de treinamento e demonstração de portfólio. Acesse em **Segurança → Simulação de Firewall**.

> ⚠️ Importante: o simulador deste portfólio **não aplica regras reais** a nenhum firewall — ele existe apenas para fins educacionais e de demonstração de conhecimento técnico.
