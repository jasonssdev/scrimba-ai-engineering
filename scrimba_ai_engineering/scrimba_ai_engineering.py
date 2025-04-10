import reflex as rx
from src.pages import home_page

app = rx.App()
app.add_page(home_page, route="/")