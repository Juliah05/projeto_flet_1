import flet as ft

def main(page: ft.page):
       #titulo da pagina
    page.title = "Aplicacao teste"
       #tema da pagina
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()


ft.app(target=main, view=ft.WEB_BROWSER)