# Avaliação 1 Questão 2

# Implemente um programa que receba um produto como parâmetro e liste o nome e
# o preço de todos esses produtos no mercado livre, com paginação incluída.
# Busque uma forma de passar um parâmetro para o seu programa.

import scrapy


class PegarprodutosmercadolivreSpider(scrapy.Spider):
    name = 'PegarProdutosMercadoLivre'
    pesquisa = 'cadeira'
    start_urls = ['https://lista.mercadolivre.com.br/' + pesquisa + '/']

    def parse(self, response):
        produtos = response.xpath('/html/body/main/div[1]/div/section/ol/li')

        for produto in produtos:
            descricao = produto.xpath(
                './/h2/span[@class="main-title"]/text()').extract_first()
            precoFracao = produto.xpath(
                './/span[@class="price__fraction"]/text()').extract_first()
            precoDecimal = produto.xpath(
                './/span[@class="price__decimals"]/text()').extract_first()
            precoFinal = precoFracao + ',' + \
                ('00' if precoDecimal == None else precoDecimal)
            print('Produto | Preço')
            print(descricao + ' | ' + precoFinal)
