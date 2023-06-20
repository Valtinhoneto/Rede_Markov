# Compositor de Música Markoviana
Este projeto implementa um compositor de música baseado em cadeias de Markov que gera composições originais com base em um texto de entrada. Ele utiliza o conceito de um grafo direcionado, onde cada nó representa uma palavra e as arestas representam as probabilidades de transição entre as palavras.

# Como Usar
Prepare um arquivo de texto de entrada contendo as palavras que serão utilizadas para gerar as composições. Certifique-se de que o arquivo esteja formatado corretamente, com uma palavra por linha e sem caracteres especiais ou sinais de pontuação.

Execute o seguinte comando para gerar uma composição:

## python main.py caminho-do-arquivo-de-entrada.txt
Substitua caminho-do-arquivo-de-entrada.txt pelo caminho do arquivo de texto de entrada que você preparou.

Aguarde enquanto o programa analisa o arquivo de entrada e gera a composição.

Ao final do processo, o programa exibirá a composição gerada no console.

# Clone o repositório:

Instale as dependências necessárias:

pip install -r requirements.txt

# Prepare os arquivos de texto de entrada:

Crie um diretório para cada artista dentro do diretório songs.
Coloque os arquivos de texto contendo letras de música ou dados de músicas nos respectivos diretórios dos artistas.
Certifique-se de que os arquivos de texto estejam formatados corretamente, com uma palavra por linha e sem caracteres especiais ou sinais de pontuação.

# Execute o compositor:

python main.py nome-do-artista

Substitua nome-do-artista pelo nome do artista cujas músicas você deseja usar para a composição.

Aproveite a música composta! 

O programa irá gerar uma composição com base nas músicas do artista fornecido e exibi-la no console.

# Exemplo de Uso

Para compor músicas com base nas músicas do Queen, execute o seguinte comando:

python main.py queen
O programa irá analisar as letras das músicas do Queen e gerar uma composição de 100 palavras.

# Personalização

Você pode personalizar a composição gerada modificando o parâmetro length na função compor. Ao alterar o valor, você pode controlar o tamanho da composição.

# Contribuições

Contribuições para este projeto são bem-vindas. Se encontrar algum problema ou quiser adicionar novos recursos, abra um problema ou envie uma solicitação de pull no GitHub.

# Licença

Este projeto está licenciado sob a Licença MIT. Consulte o arquivo LICENSE para obter mais informações.

# Agradecimentos

Este projeto foi inspirado no conceito de cadeias de Markov e na ideia de utilizá-las para a composição de músicas.
