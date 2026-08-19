# Vídeos do Laboratório Virtual

Esta pasta representa o local onde vídeos curtos (screencasts) de resolução de problemas
seriam armazenados em uma versão de produção do sistema.

No portfólio, os vídeos são **simulados** através de metadados (título, duração, descrição)
exibidos na página `/laboratorio`, evitando a necessidade de hospedar arquivos de vídeo reais.

## Como evoluir para upload real

Para transformar isso em um upload funcional:

1. Adicionar um formulário com `<input type="file" accept="video/*">` na página do laboratório.
2. Criar uma rota Flask que receba o arquivo via `request.files`, valide a extensão/tamanho
   e salve nesta pasta (ou em um bucket de armazenamento, como S3).
3. Persistir os metadados do vídeo (nome, caminho, duração, descrição) em uma tabela do banco
   de dados, similar ao modelo `Ticket` já existente no projeto.
