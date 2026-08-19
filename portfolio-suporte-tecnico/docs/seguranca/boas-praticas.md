## Objetivo

Estabelecer diretrizes básicas de segurança da informação para estações de trabalho e usuários finais em um ambiente corporativo de pequeno/médio porte.

## 1. Antivírus

- Manter o antivírus corporativo sempre **ativo e atualizado** em todas as estações.
- Configurar varreduras automáticas periódicas (recomendado: diária, fora do horário comercial).
- Nunca desabilitar a proteção em tempo real, mesmo temporariamente, sem autorização formal.
- Verificar dispositivos USB externos antes de utilizá-los.

## 2. Firewall

- Manter o firewall do sistema operacional habilitado em todas as estações (ver módulo **Simulação de Firewall**).
- Bloquear portas não utilizadas pela estação (ex.: Telnet, RDP quando não necessário).
- Permitir apenas o tráfego essencial para as aplicações corporativas.
- Revisar periodicamente as regras configuradas.

## 3. Backup

- Seguir a estratégia **3-2-1**: 3 cópias dos dados, em 2 mídias diferentes, sendo 1 cópia fora do local (offsite/nuvem).
- Testar a restauração de backups periodicamente — um backup nunca testado não é confiável.
- Automatizar rotinas de backup sempre que possível (ver documento **Rotina de Backup**).

## 4. Senhas e autenticação

- Utilizar senhas com no mínimo 12 caracteres, combinando letras, números e símbolos.
- Habilitar autenticação em dois fatores (2FA) sempre que disponível.
- Nunca compartilhar credenciais entre usuários.
- Trocar senhas padrão de equipamentos de rede (roteadores, switches) imediatamente após a instalação.

## 5. Atualizações de sistema

- Manter o sistema operacional e aplicativos sempre atualizados com os últimos patches de segurança.
- Priorizar atualizações críticas/de segurança.

## 6. Boas práticas para os usuários finais

- Bloquear a estação sempre que se ausentar (`Win + L`).
- Não clicar em links ou anexos de remetentes desconhecidos (phishing).
- Reportar imediatamente qualquer comportamento suspeito ao suporte técnico.
- Não instalar softwares não homologados pela equipe de TI.

## Checklist rápido de segurança para o técnico

- [ ] Antivírus instalado, ativo e atualizado
- [ ] Firewall habilitado com regras revisadas
- [ ] Backup configurado e testado
- [ ] Sistema operacional atualizado
- [ ] Senha local forte configurada
- [ ] Usuário orientado sobre boas práticas básicas
