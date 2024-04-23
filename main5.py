import flet as ft


def main(page):
    first_name = ft.TextField()
    last_name = ft.TextField(dense=False)
    first_name.disabled = True
    last_name.disabled = False
    page.add(first_name, last_name)

    first_name = ft.TextField()
    last_name = ft.TextField()
    c = ft.Column(controls=[
        first_name,
        last_name
    ])
    c.disabled = True
    page.add(c)
ft.app(target=main)
