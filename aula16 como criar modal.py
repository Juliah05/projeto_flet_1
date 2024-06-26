from flet import *


def main(page: page):

    #Parte1- criar a alerta
    alerta = AlertDialog(
        title= Text('informação importante'),
        content=Text('Ola usuário da nossa aplicação,estamos felizes por te ter aqui conosco!'),
        on_dismiss=lambda e:print('Alerta fechada!')
    )

    # Parte2- criar a funcao que permite abrir a alerta
    def abrir_alerta(e):
        page.dialog = alerta
        alerta.open = True
        page.update()

    #Parte3- criar o botao que vai abrir a alerta
    page.add(
        Text('Ola Mundo!'),
        ElevatedButton('Informacao', on_click=abrir_alerta)
    )




app(target=main)