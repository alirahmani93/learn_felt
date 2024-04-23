import time

import flet as ft


def main(page: ft.Page):
    t = ft.Text(value="Hello, world!", color="green", size=20)
    page.controls.append(t)
    page.update()
    page.add(t)  # it's a shortcut for page.controls.append(t) and then page.update()

    # for i in range(3):
    #     t.value = f"Step {i}"
    #     page.update()
    #     time.sleep(1) ## REMEMBER: You should double enter to see remain of page

    page.add(
        ft.Row(controls=[
            ft.TextField(label="Your name"),
            ft.ElevatedButton(text="Say my name!")
        ])
    )

ft.app(target=main)
