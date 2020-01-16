Projeto criado a nível academico para responder a avaliação 1 da disciplina de captura e visualização de dados.

# Unipê - MBA em Business Inteligence com bigdata.

- Disciplina: Captura e visualização de dados - Avaliação 1.
- Professor: Diénert Vieira (dienertalencar@gmail.com)
- Aluno: Jean Júnio da Silva Lobo
  ​

### Questão 1

​
Implemente um programa que entre no site do UOL e imprima apenas a seguinte mensagem: A cotação atual do dólar é: <cotação>, onde <cotação> vai ser o valor capturado do site no momento. Procure uma forma de omitir as mensagens de log na execução do seu programa para aparecer apenas essa mensagem como saída.

**_para validar essa atividade, acesse o terminal e digita o comando abaixo_**

**scrapy crawl PegarCotacaoDolarUol -s LOG_ENABLED=False**
​​

### Questão 2

Implemente um programa que receba um produto como parâmetro e liste o nome e o preço de todos esses produtos no mercado livre, com paginação incluída. Busque uma forma de passar um parâmetro para o seu programa.

**_para validar essa atividade, acesse o terminal e digita o comando abaixo_**

**scrapy crawl PegarProdutosMercadoLivre -s LOG_ENABLED=False -o pesquisa_produtos_mercado_livre.csv -a pesquisa=livro-python**

### Questão 3

Quais cuidados devem ser observados ao capturar dados de um site?

**_É primordial entender a estrutura do html do site que será analisado, analisar algumas informações como 'tags' com atributos 'id' gerados dinamicamente e também atributos 'class' que são motificados por javascript após o carregamento da página, pois, o cralwer não funcionará para qualquer busca nesses casos, e deve-se testar com entrada de dados diferentes para validar varios cenários, além disso, é importante observar o tempo em que o crawler está sendo escutado, pois dependendo da quantidade de dados e velocidade em que os mesmos são capturados, o acesso aos dados por ser bloqueado pelo servidor da aplicação do site._**

### Questão 4

Quais ameaças capturadas automáticas proporcionam para sistemas web?

**_Esse tipo de captura se mal intecionada pode ser utilizada para roubar conteúdos protegidos por direitos autorais e gerar cotações de um produto/serviços proporcionando em alguns casos concorrência desleal além de possibilitar também que hackers/fraudadores obtenham benefícios através do trabalho de outras empresas/instituições para prejudicar os negócios das mesmas._**

### Questão 5

Você diria que bots ou crawlers são programas facilmente paralelizáveis? Se sim, explique como isso seria implementado dando um exemplo?

**_Sim, são sim, e já é comum esse tipo de implemntação, pois no caso de coleta de dados em ecommerces, é eventualmente necessário acessar a página de detalhes de cada item para cada lista de resultados, a exemplo do que foi feito na questão 2 dessa atividade no caso do spider PegarProdutosMercadoLivre, abaixo segue o exemplo_**

    def parse(self, response):
        # produtos = response.xpath('/html/body/main/div[1]/div/section/ol/li')
        produtos = response.xpath('.//ol[contains(@class,"section") and contains(@class,"search-results")]/li')

        if self.proxima_pagina == 1:
            print('Iniciando crawler...')
            print('Lendo página 1')

        for produto in produtos:

            link_detail = produto.xpath('.//a[contains(@class,"item__js-link")]/@href').extract_first()

            yield scrapy.Request(
                url=link_detail,
                callback=self.parse_detail
            )

**_Dentro do metodo parse(self, response), a página de resultados é interada para ler produto a produto, e a cada interação, o link da página de detalhes é capturado para realizar um novo request para pegar os detalhes do item atual e após isso segue para a próxima interação._**

​
