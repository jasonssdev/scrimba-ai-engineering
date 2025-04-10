import reflex as rx
from src.states.stock_state import StockState

@rx.page(route="/")
def home_page():
    return rx.flex(
        rx.box(
            rx.vstack(
                rx.heading("Stock AI Recommender", size="6", color="white", text_align="center"),
                rx.text(
                    "Enter stock tickers, a start and end date. Our AI will analyze price history and recommend whether to Buy, Hold or Sell.",
                    color="gray.300",
                    font_size="1rem",
                    text_align="center",
                    mb="6",
                ),
                rx.input(
                    placeholder="E.g. AAPL, TSLA, MSFT",
                    value=StockState.stocks,
                    on_change=StockState.set_stocks,
                    bg="gray.800",
                    color="white",
                    border_color="gray.700",
                    _placeholder={"color": "gray.500"},
                    mb="3",
                    width="100%"
                ),
                rx.hstack(
                    rx.input(
                        type_="date",
                        placeholder="Start Date",
                        value=StockState.start_date,
                        on_change=StockState.set_start_date,
                        bg="gray.800",
                        color="white",
                        border_color="gray.700",
                        _placeholder={"color": "gray.500"},
                        mb="3",
                        width="48%"
                    ),
                    rx.input(
                        type_="date",
                        placeholder="End Date",
                        value=StockState.end_date,
                        on_change=StockState.set_end_date,
                        bg="gray.800",
                        color="white",
                        border_color="gray.700",
                        _placeholder={"color": "gray.500"},
                        mb="4",
                        width="48%"
                    ),
                    style={"justifyContent": "space-between"}
                ),
                rx.button(
                    "Analyze Stocks",
                    on_click=StockState.analyze_stocks,
                    bg="blue.600",
                    _hover={"bg": "blue.700"},
                    color="white",
                    size="3",
                    width="100%",
                    border_radius="md",
                    mb="4",
                    disabled=StockState.is_loading  # Esto deshabilita el botón durante la carga.
                ),
                rx.cond(
                    StockState.is_loading,
                    rx.spinner(color="blue", size="3", mt="4"),
                    rx.box(
                        rx.text("AI Recommendation:", font_weight="bold", mb="2", color="white"),
                        rx.cond(
                            StockState.result != "",
                            rx.text(StockState.result, color="gray.300"),
                            rx.text("Your analysis result will appear here.", color="gray.500")
                        ),
                        border="1px solid #444",
                        border_radius="lg",
                        padding="4",
                        width="100%",
                        min_h="100px",
                        bg="gray.900",
                        mt="4"
                    )
                )
            ),
            bg="#263238",  # Fondo de la tarjeta (oscuro pero más claro que el fondo total)
            padding="6",
            border_radius="xl",
            box_shadow="lg",
            max_width="600px",
            width="100%",
            margin_x="auto"
        ),
        justify="center",
        align="center",
        direction="column",
        bg="#1f2a38",  # Fondo de toda la página, gris azulado
        height="100vh",
        padding_x="4"
    )