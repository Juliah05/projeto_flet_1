import flet as ft


def main(page: ft.page):
    page.bgcolor = ft.colors.BLACK

    def change_main_image(e):
        for elem in options.controls:
            if elem == e.controls:
                elem.opacity = 1
                main_image.src = elem.image_src
            else:
                elem.opacity = 0.5

        main_image.update()
        options.update()



    product_images = ft.Container(
        bgcolor=ft.colors.WHITE,
        padding=ft.padding.all(30),
        aspect_ratio=9/16,
        content=ft.Column(
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            controls=[
                  main_image := ft.Image(
                     src='https://images.tcdn.com.br/img/img_prod/839866/poltrona_para_sala_decorativa_opala_luxo_suede_amarelo_adonai_estofados_173_3_20200819084559.jpg',
                  ),

                 options := ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                         ft.Container(
                            image_src='https://images.tcdn.com.br/img/img_prod/829281/poltrona_decorativa_para_sala_79_cm_impala_pes_palito_madeira_veludo_preto_sosofa_153_1_56dea153b8567a3217f24da6ceba59fa_20221212152902.jpg',
                            width=80,
                            height=80,
                            opacity=1,
                            on_click=change_main_image
                         ),

                         ft.Container(
                            image_src='https://images.tcdn.com.br/img/img_prod/829281/poltrona_decorativa_para_sala_79_cm_impala_pes_palito_madeira_veludo_bordo_sosofa_155_1_046d27fdb9456a602b689ea633188ef2_20221212152903.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                         ),

                         ft.Container(
                            image_src='https://a-static.mlcdn.com.br/450x450/poltrona-decorativa-canoa-retro-suede-rosa-para-sala-de-estar-luxo-escritorio-quarto-opala/belamoveis/15932711730/92f62f46b9b0ddc9f02eab91467a89c9.jpg',
                            width=80,
                            height=80,
                            opacity=0.5,
                            on_click=change_main_image
                         )
                    ]
                )
            ]
        )
    )

    product_details = ft.Container(
        padding=ft.padding.all(30),
        bgcolor=ft.colors.BLACK87,
        aspect_ratio=9/16,
        content=ft.Column(
            controls=[
                ft.Text(
                    value='CADEIRAS',
                    color=ft.colors.AMBER,
                    weight=ft.FontWeight.BOLD,
                ),

                ft.Text(
                    value='Poltrona Amarela Moderna',
                    color=ft.colors.WHITE,
                    weight=ft.FontWeight.BOLD,
                    size=30,
                ),

                ft.Text(value='Sala de estar', color=ft.colors.GREY, italic=True),

                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Text(
                            col={'xs': 12, 'sm': 6},
                            value='R$ 399',
                            color=ft.colors.WHITE,
                            size=30,
                        ),
                        ft.Row(
                            col={'xs': 12, 'sm': 6},
                            controls=[
                                ft.Icon(
                                    name=ft.icons.STAR,
                                    color=ft.colors.AMBER if _ < 4 else ft.colors.WHITE,
                                ) for _ in range(5)
                            ]
                        )
                    ]
                ),
                ft.Tabs(
                    selected_index=0,
                    height=150,
                    indicator_color=ft.colors.AMBER,
                    label_color=ft.colors.AMBER,
                    unselected_label_color=ft.colors.GREY,
                    tabs=[
                        ft.Tab(
                            text='Descrição',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='A Poltrona Decorativa Cadeira reforçada Opala Bege cor amarelo desenho do tecido suede é perfeita para criar um ambiente moderno e aconchegante na sua casa. com seu design retrô e cor amarela vibrante. ',
                                    color=ft.colors.GREY,
                                )
                            )
                        ),

                        ft.Tab(
                            text='Detalhes',
                            content=ft.Container(
                                padding=ft.padding.all(10),
                                content=ft.Text(
                                    value='Dimensões 0.8m de largura, 0.9m de altura e 0.76m de profundidade.',
                                    color=ft.colors.GREY,
                                )
                            )
                        )
                    ]
                ),

                ft.ResponsiveRow(
                    columns=12,
                    controls=[
                        ft.Dropdown(
                            col=6,
                            label='Cor',
                        )
                    ]
                )

            ]
        )
    )


    layout = ft.Container(
        width=900,
        margin=ft.margin.all(30),
        shadow=ft.BoxShadow(blur_radius=300, color=ft.colors.CYAN),
        content=ft.ResponsiveRow(
            columns=12,
            spacing=0,
            run_spacing=0,
            controls=[
                 #product_images,
                 product_details

            ]

        )
    )

    page.add(layout)

if __name__ == '__main__':
     ft.app(target=main)