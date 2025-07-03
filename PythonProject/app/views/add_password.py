import flet as ft
from sqlalchemy.ext.asyncio import AsyncSession

from app.services.managerService import ManagerService

async def add_password(container: ft.Column, db: AsyncSession):
    async def on_submit(e):
        await ManagerService.store_password(db=db, site=service.value, username=username.value, password=password.value)
        service.value = ""
        username.value = ""
        password.value = ""

        container.update()


    service = ft.TextField(label="Service")
    username = ft.TextField(label="Username")
    password = ft.TextField(label="Password")
    btn_add = ft.ElevatedButton("Agregar Usuario", on_click=on_submit)
    user_list = ft.Column()

    # Agregar controles al contenedor
    container.controls.clear()
    container.controls.extend([service, username, password, btn_add, user_list])
    container.update()