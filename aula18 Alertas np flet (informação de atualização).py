from flet import *


def main(page: page):
    def atualizar_agora(e):
        page.banner.open = False
        print('Atualizando...')
        page.update()

    def lembrar_mais_tarde(e):
        page.banner.open = False
        print('Vou te lembrar mais tarde...')
        page.update()

    def cancelar(e):
        page.banner.open = False
        print('Cancelado!')
        page.update()


    #1 - Criar o nosso banner de informacao
    page.banner = Banner(
        bgcolor= colors.AMBER_900,
        leading=Icon(icons.WARNING_OUTLINED),
        content=Text( 'Ola, ja temos uma nova atuazalicao para essa sua aplicacao disponivel. O que desejas fazer por agora?'),
        actions=[
            TextButton('Atualizar agora',
                       on_click=atualizar_agora),
            TextButton('Lembrar mais tarde',
                       on_click=lembrar_mais_tarde),
            TextButton('Cancelar',
                       on_click=cancelar),
        ],
    )

    #funcao para abrir o banner
    def abrir_banner(e):
        page.banner.open=True
        page.update()


    page.add(
        Text('Ola mundo!'),
        ElevatedButton('Executar', on_click=abrir_banner )
    )


app(target=main)
