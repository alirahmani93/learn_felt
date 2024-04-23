import flet as ft


class AdaptiveNavigationDestination(ft.NavigationDestination):
    def __init__(self, ios_icon, android_icon, label):
        super().__init__()
        self._ios_icon = ios_icon
        self._android_icon = android_icon
        self.label = label

    def build(self):
        # we can check for platform in build method because self.page is known
        self.icon = (
            self._ios_icon
            if self.page.platform == ft.PagePlatform.IOS
               or self.page.platform == ft.PagePlatform.MACOS
            else self._android_icon
        )


def main(page):
    page.adaptive = True

    page.navigation_bar = ft.NavigationBar(
        selected_index=2,
        destinations=[
            AdaptiveNavigationDestination(
                ios_icon=ft.cupertino_icons.PERSON_3_FILL,
                android_icon=ft.icons.PERSON,
                label="Contacts",
            ),
            AdaptiveNavigationDestination(
                ios_icon=ft.cupertino_icons.CHAT_BUBBLE_2,
                android_icon=ft.icons.CHAT,
                label="Chats",
            ),
            AdaptiveNavigationDestination(
                ios_icon=ft.cupertino_icons.SETTINGS,
                android_icon=ft.icons.SETTINGS,
                label="Settings",
            ),
        ],
    )

    page.update()


ft.app(target=main)
