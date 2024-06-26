from flet import *


def main(page:page):
    page.add(Text(f'Rota inicial: {page.route}'))


    def nova_rota(route):
        page.add(Text(f'nova rota: {route}'))

        page.on_route_change = nova_rota
        page.update()
        page.add(ElevatedButton("Ir para compras", on_click= rota_compras ))
    def rota_compras(e):
        page.route = "/compras"
        page.update()

app(target=main, view=WEB_BROWSER)