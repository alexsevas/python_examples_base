# ENV ytpy310
# pip install flet

import flet as ft

def main(page: ft.Page):
    page.title = "Flet App"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    def button_click(e):
        page.add(ft.Text(f"Привет, {name_input.value}!"))

    name_input = ft.TextField(label="Введите имя", width=300)
    greet_button = ft.ElevatedButton("Поздороваться", on_click=button_click)

    page.add(name_input, greet_button)

ft.app(target=main)
