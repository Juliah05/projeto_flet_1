from flet import *


def main(page:Page):
     page.title= "Rotas"

     page.navigation_bar = NavigationBar(
         destinations=[
             NavigationDestination(icon=icons.HOME, label="Home"),
             NavigationDestination(icon=icons.EXPLORE, label="Explorar"),
             NavigationDestination(icon=icons.COMMUTE, label="Rotas")
         ]
     )

     page.add(Text("Corpo da Aplicacao"),
              ElevatedButton(text="Fazer viagem"))






app(target=main)