import asyncio

import flet as ft
from app.database.database import init_db, SessionLocal
from app.menu import create_menu, handle_change


async def main(page: ft.Page):

    await init_db()

    page.title = "TrustVault"
    page.shadow = True
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Contenedor para las vistas
    container_view = ft.Column(expand=True)

    # Definir el NavigationDrawer en `page.drawer`
    loop = asyncio.get_running_loop()  # Obtiene el loop principal de Flet
    page.drawer = create_menu(handle_change, container_view, SessionLocal, loop)

    # Botón para abrir el menú lateral
    btn_menu = ft.IconButton(ft.Icons.MENU, on_click=lambda _: setattr(page.drawer, "open", True) or page.update())

    # Configurar barra superior
    page.appbar = ft.AppBar(title=ft.Text("Menu TrustVault"), leading=btn_menu)

    # Agregar contenedor de vistas al layout
    page.add(container_view)

ft.app(target=main, view=ft.AppView.FLET_APP)  # Modo escritorio
