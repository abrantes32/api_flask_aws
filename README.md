# Nome do Projeto 
ou
<h1 align="center">API Flask</h1>

<h1 align="center">
    <a href="https://pt-br.reactjs.org/">🔗 React</a>
</h1>
<p align="center">🚀 API em flask que consome uma API Genius, utilizando DynamoDB </p>

<h4 align="center"> 
	🚧 Em construção...  🚧
</h4>

### Features

- [ ] Utilizar serviço da AWS
- [x] Criar uma API REST em Python (FLASK)
- [x] Consumir API do Genius
- [x] liste as 10 músicas mais populares do artista pesquisado
- [ ] Salvar um id de transação no formato uuid versão 4
- [ ] Pesquisar por nome do artista
- [ ] Salvar em uma coleção no DynamoDB
- [ ] Dados com o retorno da consulta à API devem ser salvos no Redis por 7 dias
- [ ] Verificar se existe transações salvas ao buscar um artista e encontra-se disponível em cache (Redis)
- [ ] A consulta deverá permitir a passagem via query string a opção de manter os dados
em cache, caso enviado o parâmetro cache=False limpar a transação do Redis e
atualizar o DynamoDB com a opção de escolhida pelo usuário, o não envio do
parâmetro indica que deve-se utilizar os dados em cache

# Clone este repositório
$ git clone <https://github.com/tgmarinho/nlw1>

# Acesse a pasta do projeto no terminal/cmd
$ cd nlw1

# Vá para a pasta server
$ cd server

# Instale as dependências
$ npm install

# Execute a aplicação em modo de desenvolvimento
$ npm run dev:server

# O servidor inciará na porta:3333 - acesse <http://localhost:3333> 


