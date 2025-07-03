import flet as ft

def password_card(icon, service, username,password):
    pw_text = ft.Text("password : ******", size=12)

    def toggle_password(e):
        if pw_text not in e.page.controls:
            e.page.add(pw_text)

        pw_text.value = "password : ******" if pw_text.value != "password : ******" else "password : {}".format(password)
        pw_text.update()

    def copy_password(e):
        # Copiar la contraseña al portapapeles
        e.page.set_clipboard(password)
        e.page.snack_bar = ft.SnackBar(ft.Text("Contraseña copiada al portapapeles"))
        e.page.snack_bar.open()

    card = ft.Card(
            content=ft.Container(
                content=ft.Column(
                    [
                        ft.ListTile(
                            leading=ft.Icon(icon),
                            title=ft.Text(service),
                            subtitle=ft.Column(
                        [
                                    ft.Text(f"Username: {username}", size=12),
                                    pw_text
                                ],
                                spacing=2,  # Espaciado entre líneas
                            ),
                        ),
                        ft.Row(
                            [
                                ft.TextButton("Ver", on_click=toggle_password),  # Botón para mostrar/ocultar
                                ft.TextButton("Copiar", on_click=copy_password),  # Agrega más funcionalidad si quieres
                            ],
                            alignment=ft.MainAxisAlignment.END,
                        ),
                    ]
                ),
                width=400,
                padding=10,
            )
        )
    return card