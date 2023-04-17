import yfinance as yf
import json

import utils.config as config

class Finance():
    def __init__(self):
        self.tickers = json.loads(config.INDEXES)
        
    def get_close_peice(self, ticker):
        
        prices = yf.Ticker(ticker).history(period='2d')
        
        try:
            close = prices.iloc[1].loc["Close"]
            last_close = prices.iloc[0].loc["Close"]
        
            change = close - last_close
            pct_change = change/last_close
        
            return close, change, pct_change
        except Exception as e:
            return 0, 0, 0
    
    def get_formatted_html(self):
        
        for ticker in self.tickers:
            name = ticker['name']
            symbol = ticker['ticker']
            self.get_close_peice(symbol)
            
            
        
        html_result = "<h2>Today's Markets:</h2>"
        
        html_result += """<table>
                            <tr>
                                <th>INDEX</th>
                                <th>CLOSE</th>
                                <th>CHANGE</th>
                            </tr>
                        """
        for ticker in self.tickers:
            name = ticker['name']
            symbol = ticker['ticker']
            close, change, pct_change = self.get_close_peice(symbol)
            
            html_result += f"""<tr>
                                <td>{name}</td>
                                <td>{round(close, 2)}</td>
            """
            if change >= 0:
                html_result += f'<td><font color="green">+{round(change, 2)}(+{round(pct_change*100, 2)}%)</font></td></tr>'
            else:
                html_result += f'<td><font color="red">{round(change, 2)}({round(pct_change*100, 2)}%)</font></td></tr>'

        html_result += '</table><hr>'
        return html_result
    

