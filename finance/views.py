# django-server-traderguessr/finance/views.py
import yfinance as yf
from django.http import JsonResponse

def get_stock_data(request, ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(period="1mo")
    hist.reset_index(inplace=True)
    data = hist[['Date', 'Open', 'High', 'Low', 'Close']].to_dict(orient="records")
    return JsonResponse(data, safe=False)