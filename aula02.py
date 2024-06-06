import flet as ft

def main(page):

    def login(e):
        if not entrada_nome.value:
            entrada_nome.error_text = "Por favor preencha o seu nome."
            page.update()
        if not entrada_senha.value:
            entrada_senha.error_text = "Campo de senha obrigatorio."
            page.update()
        else:
         nome = entrada_nome.value
         senha = entrada_senha.value
         print(f"nome: {nome}\nsenha: {senha}")
         page.clean() #funcao para limpar a pagina
         page.add(ft.Text(f"Ola, {nome}\nSeja bem vindo a nossa aplicacao"))
         pass

    entrada_nome = ft.TextField(label="Digite o seu nome")
    entrada_senha = ft.TextField(label= "Digite a sua senha")

    page.add(
        entrada_nome,
        entrada_senha,
        ft.ElevatedButton("Clique aqui", on_click=login)
    )
    pass

ft.app(target=main)