from flet import *


def main(page: page):

    # passo4 -- Criar função para fechar o modal
    def confirmar(e):
        alerta_dialogo.open = False
        print('Item apagado com sucesso')
        page.update()
    def cancelar(e):
        alerta_dialogo.open = False
        print('Cancelado com sucesso')
        page.update()

    #passo1 -- Criar a alerta de dialogo
    alerta_dialogo = AlertDialog(
        modal=True,
        title=Text('Confirme a ação'),
        content=Text('Deseja mesmo apagar os itens que acabaste de selecionar?\nSe continuar com essa acção não terá mais volta!'),
        actions=[
            TextButton(' Apagar', on_click=confirmar),
            TextButton('Cancelar', on_click=cancelar)

        ],
        actions_alignment=MainAxisAlignment.END
    )

    #passo3 -- criar a função para abrit modal
    def abrir_modal(e):
        page.dialog = alerta_dialogo
        alerta_dialogo.open = True
        page.update()


    # passo2 -- Criar o botao que vai abrir a alerta
    page.add(
        Text('Ola mundo!'),
        ElevatedButton(' Apagar item',icon=icons.DELETE, icon_color='red',
                       on_click=abrir_modal)
    )


app(target=main)