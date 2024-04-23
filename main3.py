import time

import flet as ft


def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green", size=20)
    page.controls.append(t)

    def button_clicked(e):
        page.add(ft.Text("Clicked!"))

    page.add(ft.ElevatedButton(text="Click me", on_click=button_clicked))

ft.app(target=main)
