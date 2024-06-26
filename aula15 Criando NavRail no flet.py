from flet import *


def main(page:page):
    page.title = "NavRail"

    Rail = NavigationRail(
        extended=True,
        selected_index=0,
        min_width=100,
        min_extended_width=200,
        label_type=NavigationRailLabelType.ALL,
        leading=FloatingActionButton(icon=icons.CREATE, text="Criar"),
        group_alignment=-0.9,
        destinations=[
            NavigationRailDestination(
                icon=icons.FAVORITE_BORDER,
                selected_icon=icons.FAVORITE,
                label="Favoritar"
            ),
            NavigationRailDestination(
                icon_content=Icon(icons.BOOKMARK_BORDER),
                selected_icon_content=Icon(icons.BOOKMARK),
                label="Marcar"
            ),
            NavigationRailDestination(
                icon=icons.SETTINGS_OUTLINED,
                selected_icon=icons.SETTINGS,
                label= 'Definicoes'
            )
        ],
        on_change = lambda e: print("Pagina selecionada:", e.control.selected_index),
    )

    page.add(
        Row(
            [
                Rail,
                VerticalDivider(width=1),
                Column([Text("Corpo da Aplicacao")], alignment=MainAxisAlignment.START, expand=True),
            ],
            expand=True
        )
    )
app(target=main)
