import flet as ft
import requests
from flet import *

# URL da API de cotação de moedas
API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

# Lista de moedas fortes para conversão
TARGET_CURRENCIES = ["BRL", "EUR", "GBP", "JPY", "CAD", "AUD"]

def fetch_exchange_rates():
    """Fetch exchange rates for USD to target currencies."""
    response = requests.get(API_URL)
    data = response.json()
    rates = {currency: data["rates"].get(currency, 0) for currency in TARGET_CURRENCIES}
    return rates

def main(page: ft.Page):
    page.title = "Cotação de Moedas"
    page.theme_mode = "light"
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.window.resizable = False

    # Definir imagem de fundo com as novas propriedades
    background = ft.Image(
        src="https://img.freepik.com/fotos-gratis/montao-de-moedas-de-chocolate_23-2147748111.jpg",
        fit=ft.ImageFit.COVER,
        width=page.window.width,
        height=page.window.height,
    )

    # Título do App
    title = ft.Text("Cotação do Dólar", size=30, weight="bold", color=ft.colors.WHITE)

    # Área de exibição das cotações
    rates_text = ft.Column([], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER)

    def update_rates(e):
        # Buscar cotações e atualizar a exibição
        rates = fetch_exchange_rates()
        rates_text.controls.clear()
        for currency, rate in rates.items():
            rates_text.controls.append(ft.Text(f"1 USD = {rate:.2f} {currency}", color=ft.colors.WHITE, size=18))
        page.update()

    # Botão para atualizar as cotações
    update_button = ft.ElevatedButton("Atualizar Cotações", on_click=update_rates, bgcolor='#166e4e', color=ft.colors.WHITE)

    # Layout principal centralizado
    layout = ft.Column(
        controls=[title, rates_text, update_button],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
    )

    # Adiciona o fundo e o conteúdo sobre ele usando Stack
    page.add(
        ft.Stack(
            controls=[
                background,  # Fundo
                ft.Container(  # Container centralizado para os controles
                    content=layout,
                    alignment=ft.alignment.center,
                    padding=20,
                )
            ]
        )
    )

ft.app(target=main)

