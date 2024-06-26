from flet import *


def main(page:page):

      page.appbar = AppBar(
          leading=Icon(icons.CODE_OFF),
          leading_width=20,
          bgcolor="#003377",
          title=Text("Minha Loja"),
          center_title=True,
          actions=[
              IconButton(icons.WB_SUNNY_OUTLINED),
              PopupMenuButton(
                  items=[
                      PopupMenuItem(text="Logar"),
                      PopupMenuItem(),
                      PopupMenuItem(
                          text="Sair"
                      )

                  ]
              )
          ]
      )

      page.add(Text("Corpo!"))


app(target=main)