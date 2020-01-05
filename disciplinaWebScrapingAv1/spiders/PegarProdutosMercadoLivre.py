# Avaliação 1 Questão 2

# Implemente um programa que receba um produto como parâmetro e liste o nome e
# o preço de todos esses produtos no mercado livre, com paginação incluída.
# Busque uma forma de passar um parâmetro para o seu programa.

# scrapy crawl PegarProdutosMercadoLivre -o pesquisa_produtos_mercado_livre.csv -a pesquisa=super-mario

import scrapy


class PegarprodutosmercadolivreSpider(scrapy.Spider):

    name = 'PegarProdutosMercadoLivre'

    def __init__(self, pesquisa=None, *args, **kwargs):
        super(PegarprodutosmercadolivreSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://lista.mercadolivre.com.br/%s' % pesquisa]

    def parse(self, response):
        produtos = response.xpath('/html/body/main/div[1]/div/section/ol/li')

        for produto in produtos:

            link_detail = produto.xpath(
                './/a[contains(@class,"item__js-link")]/@href').extract_first()

            yield scrapy.Request(
                url=link_detail,
                callback=self.parse_detail
            )

        next_page = response.xpath(
            './/a[contains(@class,"prefetch")]/@href')

        print(next_page.extract_first())

        if next_page:
            yield scrapy.Request(
                url=next_page.extract_first(),
                callback=self.parse
            )

    def parse_detail(self, response):

        descricao = (response.xpath(
            './/h1[contains(@class,"item-title__primary")]/text()').extract_first()).strip()

        imagem = response.xpath(
            './/div/figure[contains(@class, "gallery-image-container")]/a/img/@src').extract_first()
        imagem = 'sem imagem' if imagem == None else imagem

        precoFracao = response.xpath(
            './/span[@class="price-tag-fraction"]/text()').extract_first()

        precoDecimal = response.xpath(
            './/span[@class="price-tag-cents"]/text()').extract_first()

        precoFinal = float(precoFracao + '.' +
                           ('00' if precoDecimal == None else precoDecimal))

        quantidade_disponivel = response.xpath(
            './/span[@class="dropdown-quantity-available"]/text()').extract_first()

        produto_nota = response.xpath(
            './/span[@class="review-summary-average"]/text()').extract_first()

        yield {
            'produto': descricao,
            'preço': precoFinal,
            'nota': produto_nota,
            'disponibilidade': quantidade_disponivel,
            'imagem': imagem
        }
