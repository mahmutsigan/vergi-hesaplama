import os

import flet as ft
from vergi_hesaplama.main import main as vergi_hesapla

os.environ['FLET_SERVER_IP'] = "0.0.0.0"


def flet_main(page: ft.Page):
    page.title = "Vergi Hesaplama"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def _hesapla(_):
        result_number.value = str(vergi_hesapla(int(txt_number.value)))
        page.update()

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100, on_change=_hesapla)
    result_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    page.add(
        ft.Row(
            [
                txt_number,
                result_number,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


def main():
    ft.app(flet_main)


if __name__ == '__main__':
    main()
