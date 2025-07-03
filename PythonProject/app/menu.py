import flet as ft
import asyncio
from app.views.add_password import add_password
from app.views.list_passwords import list_passwords


async def handle_change(e, container, SessionLocal):
    container.controls.clear()

    if e.control.selected_index == 0:
        container.controls.append(ft.Text("🏠 Vista General"))
    elif e.control.selected_index == 1:
        async with SessionLocal() as session:
            await add_password(container, session)
    elif e.control.selected_index == 2:
        async with SessionLocal() as session:
            await list_passwords(container, session)

    container.update()


def create_menu(on_change_callback, container, SessionLocal, loop):
    def on_change(e):
        # ✅ Ejecuta en el mismo loop de Flet de forma segura
        asyncio.run_coroutine_threadsafe(
            on_change_callback(e, container, SessionLocal), loop
        )
    return ft.NavigationDrawer(
        on_change=on_change,
        controls=[
            ft.NavigationDrawerDestination(label="General", icon=ft.icons.HOME),
            ft.NavigationDrawerDestination(label="Gestión de Usuarios", icon=ft.icons.PERSON),
            ft.NavigationDrawerDestination(label="Otros", icon=ft.icons.INFO),
        ],
    )
