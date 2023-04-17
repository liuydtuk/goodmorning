import requests
import os
import json

class FixerFX():
    def __init__(self) -> None:
        base = "AUD"
        symbols = "GBP,USD,EUR,CNY"

        url = f"https://api.apilayer.com/fixer/latest?symbols={symbols}&base={base}"

        payload = {}
        headers= {
        "apikey": os.environ.get('FIXER_API_KEY')
        }
        
        print(headers)
        self.response = requests.request("GET", url, headers=headers, data = payload)
    
    def get_html_result(self):
        
        html_result = "<h2>Today's FX rates:</h2>"
        
        try:
            result = json.loads(self.response.text)
        
            html_result += f"<h3>{result['date']}</h3>"
            
            html_result +=  f"""<table>
                                <tr>
                                    <td><strong>AUD to CNY</strong></td><td>{round(result['rates']['CNY'],4)}</td>
                                </tr>
                                <tr>
                                    <td><strong>AUD to GBP</strong></td><td>{round(result['rates']['GBP'],4)}</td>
                                </tr>
                                <tr>
                                    <td><strong>AUD to EUR</strong></td><td>{round(result['rates']['EUR'],4)}</td>
                                </tr>
                                <tr>
                                    <td><strong>AUD to USD</strong></td><td>{round(result['rates']['USD'],4)}</td>
                                </tr>
                                <tr>
                                    <td><strong>GBP to CNY</strong></td><td>{round(result['rates']['CNY']/result['rates']['GBP'],4)}</td>
                                </tr>
                                <tr>
                                    <td><strong>USD to CNY</strong></td><td>{round(result['rates']['CNY']/result['rates']['USD'],4)}</td>
                                </tr>
                                <tr>
                                    <td><strong>EUR to CNY</strong></td><td>{round(result['rates']['CNY']/result['rates']['EUR'],4)}</td>
                                </tr>
                            </table>"""
                            
            
        except Exception as e:
            html_result += ""
            
        html_result += "<hr>"
        
        return html_result


# {
#   "base": "AUD",
#   "date": "2023-04-13",
#   "rates": {
#     "CNY": 4.659071,
#     "GBP": 0.541584,
#     "USD": 0.678285
#   },
#   "success": true,
#   "timestamp": 1681422783
# }

