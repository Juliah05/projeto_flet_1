import os
import flet as ft

os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "80000000"


def main(page: ft.page):
    linha = ft.Row(wrap=True, scroll="always", expand=True)
    page.add(linha)


    for i in range(100):
        linha.controls.append(
            ft.Container(
                ft.Text(f"Item {i}"),
                 width=100,
                 height=100,
                 alignment=ft.alignment.center,
                 bgcolor=ft.colors.AMBER_100,
                 border=ft.border.all(2, ft.colors.AMBER_600),
                 border_radius=ft.border_radius.all(8)
            )
        )
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)