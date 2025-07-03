import flet as ft
from sqlalchemy.ext.asyncio import AsyncSession

from app.components import pw_card
from app.services.managerService import ManagerService


async def list_passwords(container: ft.Column, session: AsyncSession):
    data = await ManagerService.get_all_password(session)

    # Crear contenido principal para la lista de contraseñas
    content = []
    for item in data:
        card = pw_card.password_card(ft.Icons.PASSWORD, item.service,item.username, item.password)
        containerCard = ft.Container(
            card,
            padding=5,
            col={"sm": 6, "md": 4, "xl": 2}
        )
        content.append(containerCard)

    # Crear el control `Text` para mostrar el ancho de la ventana
    pw = ft.Text(value="", style="displaySmall")

    def page_resize(e):
        # Actualizar el texto con el nuevo ancho de la ventana
        pw.update()

    # Agregar `pw` al overlay si no está ya presente
    if pw not in container.page.overlay:
        container.page.overlay.append(pw)
        container.page.update()  # Asegurar que se refleje en la UI


    # Asignar el evento de cambio de tamaño
    container.page.on_resize = page_resize

    row = ft.ResponsiveRow(content)

    # Llamar a `page_resize` para actualizar el valor inicial
    page_resize(None)

    # Agregar los controles al contenedor
    container.controls.clear()
    container.controls.append(row)

    # Actualizar el contenedor
    container.update()
