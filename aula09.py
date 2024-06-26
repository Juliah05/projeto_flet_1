import os
import flet as ft


os.environ["FLET_WS_MAX_MESSAGE_SIZE"] = "8000000"

def main(page: ft.page):
    gv = ft.GridView(expand=True, max_extent=150, child_aspect_ratio=1)
    page.add(gv)

    for i in range(1000):
        gv.controls.append(
            ft.Container(
                ft.Text(f"Item {i}", size=20, color="#001188"),
                alignment=ft.alignment.center,
                bgcolor=ft.colors.AMBER_100,
                border=ft.border.all(2, ft.colors.AMBER_600),
                border_radius=ft.border_radius.all(8)
            )
        )
    page.update()

ft.app(target=main, view=ft.WEB_BROWSER)