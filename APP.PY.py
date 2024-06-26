from flet import *


def main(page:page):
    page.add(
        Text("Ola mundo", size=30, color="red"),
        Container(
            width=200,
            height=200,
            bgcolor=colors.AMBER,
            Text("Teste")
        ),
        TextField("Digite o seu nome")

    )


app(target=main)