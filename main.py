import flet as ft
import pyperclip

import string
from random import choice

def main(page: ft.Page):
    page.title = "Gerador de senha"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.theme_mode = ft.ThemeMode.LIGHT 
    
    def handleChange(e):
        isCharPass = [checkboxUpper.value, checkboxLower.value, checkboxDigits.value, checkboxSimbols.value]
        charPass = [string.ascii_uppercase, string.ascii_lowercase, string.digits, string.punctuation]
        
        passwordLength.value = str(round(passwordLengthSlider.value))

        forPass = ""
        for i, value in enumerate(isCharPass):
            if value:
                forPass+=charPass[i]

        generatedPassword.content.value = generatePassword(forPass, int(passwordLength.value))

        page.update()

    def generatePassword(forPass, passLength):
        password = "".join(choice(forPass) for i in range(passLength))

        return password

    def copyPass(e):
        pyperclip.copy(generatedPassword.content.value)
        open_dlg(e)

    def open_dlg(e):
        page.dialog = dlg
        dlg.open = True
        page.update()

    # Alert Dialog
    dlg = ft.AlertDialog(
        title=ft.Text("Senha copiada na área de transferência"), 
        content=ft.Text("Para colar a senha em outro lugar, pressione as teclas CTRL + V.")
    )

    # Title
    title = ft.Text("Gerador de Senha", theme_style=ft.TextThemeStyle.DISPLAY_MEDIUM, weight=ft.FontWeight.W_500)

    # Row 1
    generatedPassword = ft.Container(
        content=ft.Text("", theme_style=ft.TextThemeStyle.TITLE_MEDIUM),
        padding=ft.padding.symmetric(10, 25),
        width=450,
        bgcolor=ft.colors.PRIMARY_CONTAINER,
        border_radius=50,
    )

    btnCopy = ft.ElevatedButton(text="Copiar", on_click=copyPass)

    # Row 2
    passwordLengthText = ft.Text("Tamanho da senha:", theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
    passwordLength = ft.Text("1", theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
    passwordLengthSlider = ft.CupertinoSlider(
        divisions=49,
        max=50,
        min=1,
        active_color=ft.colors.PRIMARY,
        thumb_color=ft.colors.PRIMARY,
        on_change=handleChange,
    )

    # Row 3
    charText = ft.Text("Caracteres usados:", theme_style=ft.TextThemeStyle.TITLE_MEDIUM)
    checkboxUpper = ft.Checkbox(adaptive=True, label="ABC", value=True, on_change=handleChange)
    checkboxLower = ft.Checkbox(adaptive=True, label="abc", value=True, on_change=handleChange)
    checkboxDigits = ft.Checkbox(adaptive=True, label="123", value=True, on_change=handleChange)
    checkboxSimbols = ft.Checkbox(adaptive=True, label="#$&", value=False, on_change=handleChange)

    page.add(
        ft.Column(
            [
                title,
                ft.Row(
                    [
                        generatedPassword,
                        btnCopy
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        passwordLengthText,
                        passwordLength,
                        passwordLengthSlider
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
                ft.Row(
                    [
                        charText,
                        checkboxUpper,
                        checkboxLower,
                        checkboxDigits,
                        checkboxSimbols
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                )
            ],
            spacing=40,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

ft.app(target=main)