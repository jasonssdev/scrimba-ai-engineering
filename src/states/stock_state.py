import reflex as rx
from src.services.polygon_service import get_stock_data
from src.services.openai_service import get_response

class StockState(rx.State):
    stocks: str = ""
    start_date: str = ""
    end_date: str = ""
    result: str = ""
    is_loading: bool = False

    async def analyze_stocks(self):
        # Activa el estado de carga
        self.is_loading = True

        # Validación de campos
        tickers = [t.strip() for t in self.stocks.split(",") if t.strip()]
        if not tickers or not self.start_date or not self.end_date:
            self.result = "Please fill in all the fields correctly."
            self.is_loading = False
            return

        # Obtiene datos históricos y genera el prompt
        historical_data = get_stock_data(tickers, self.start_date, self.end_date)
        prompt = "Analyze the following stock price data:\n\n"
        for ticker, data in historical_data.items():
            prompt += f"{ticker}: {data}\n\n"

        # Llama a la API y almacena la respuesta
        response = get_response(prompt)
        self.result = response or "Something went wrong with the AI response."

        # Termina el estado de carga
        self.is_loading = False