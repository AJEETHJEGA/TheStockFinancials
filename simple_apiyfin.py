from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
import yfinance as yf
from datetime import datetime, timedelta

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        if parsed_path.path == '/nifty50':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            nifty50_current_data = yf.download('^NSEI', period="1s")
            nifty50_previous_close = self.fetch_previous_close('^NSEI')

            response = {
                "current_data": json.loads(nifty50_current_data.to_json()),
              "previous_close": nifty50_previous_close
            }

            self.wfile.write(json.dumps(response).encode())
        elif parsed_path.path == '/sensex':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            sensex_current_data = yf.download('^BSESN', period="1s")
            sensex_previous_close = self.fetch_previous_close('^BSESN')

            response = {
                "current_data": json.loads(sensex_current_data.to_json()),
                "previous_close": sensex_previous_close
            }

            self.wfile.write(json.dumps(response).encode())
        elif parsed_path.path == '/banknifty':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            banknifty_current_data = yf.download('^NSEBANK', period="1s")
            banknifty_previous_close = self.fetch_previous_close('^NSEBANK')

            response = {
                "current_data": json.loads(banknifty_current_data.to_json()),
                "previous_close": banknifty_previous_close
            }

            self.wfile.write(json.dumps(response).encode())
        elif parsed_path.path == '/niftyit':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftymidcap_current_data = yf.download('^CNXIT', period="1s")
            niftymidcap_previous_close = self.fetch_previous_close('^CNXIT')

            response = {
                "current_data": json.loads(niftymidcap_current_data.to_json()),
                "previous_close": niftymidcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())
        elif parsed_path.path == '/niftyauto':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('^CNXAUTO', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('^CNXAUTO')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())
        elif parsed_path.path == '/s&p500':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('^GSPC', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('^GSPC')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())
        elif parsed_path.path == '/nasdaq':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('^IXIC', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('^IXIC')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())   
        elif parsed_path.path == '/dowjones':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('^DJI', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('^DJI')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())   
        elif parsed_path.path == '/nikkei':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('^N225', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('^N225')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())   
        elif parsed_path.path == '/ftse':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('^FTSE', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('^FTSE')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())   
        elif parsed_path.path == '/cac':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('^FCHI', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('^FCHI')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())   
        elif parsed_path.path == '/dax':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('^GDAXI', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('^GDAXI')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())   
        elif parsed_path.path == '/gold':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('GC=F', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('GC=F')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())   
        elif parsed_path.path == '/silver':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('SI=F', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('SI=F')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())   
        elif parsed_path.path == '/crude':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('CL=F', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('CL=F')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())   
        elif parsed_path.path == '/brent':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('BZ=F', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('BZ=F')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())   
        elif parsed_path.path == '/dollarindex':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('DX-Y.NYB', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('DX-Y.NYB')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())  
        elif parsed_path.path == '/usdinr':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('USDINR=X', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('USDINR=X')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())  
        elif parsed_path.path == '/eurusd':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('EURUSD=X', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('EURUSD=X')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())  
        elif parsed_path.path == '/gbpinr':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('GBPINR=X', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('GBPINR=X')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())  
        elif parsed_path.path == '/eurinr':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            niftysmallcap_current_data = yf.download('EURINR=X', period="1s")
            niftysmallcap_previous_close = self.fetch_previous_close('EURINR=X')

            response = {
                "current_data": json.loads(niftysmallcap_current_data.to_json()),
                "previous_close": niftysmallcap_previous_close
            }

            self.wfile.write(json.dumps(response).encode())  
        elif parsed_path.path == '/niftyhistory':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            nifty50_data = yf.download('^NSEI', period="300d")
            
            json_data = []
            for index, row in nifty50_data.iterrows():
                data_point = {
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume']
                }
                json_data.append(data_point)

            self.wfile.write(json.dumps(json_data).encode()) 
        elif parsed_path.path == '/sensexhistory':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            nifty50_data = yf.download('^BSESN', period="300d")
            
            json_data = []
            for index, row in nifty50_data.iterrows():
                data_point = {
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume']
                }
                json_data.append(data_point)

            self.wfile.write(json.dumps(json_data).encode()) 
        elif parsed_path.path == '/RELIANCE':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            
            all_data = {}
            #for symbol in symbols:
                # Fetch historical data for the previous day (1-day period)
            stock_data = yf.download('RELIANCE.NS', period="2d")
                
                # Extract the previous day's closing price
               
            stock_json = []
            for index, row in stock_data.iterrows():
                    data_point = {
                        "Symbol": 'RELIANCE.NS',
                        "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                        "Open": row['Open'],
                        "High": row['High'],
                        "Low": row['Low'],
                        "Close": row['Close'],
                        "Adj Close": row['Adj Close'],
                        "Volume": row['Volume'],
                        
                    }
                    stock_json.append(data_point)
            all_data['RELIANCE.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())
        elif parsed_path.path == '/TCS':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('TCS.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'TCS.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['TCS.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())
        elif parsed_path.path == '/HDFC':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('HDFC.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'HDFC.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['HDFC.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/INFY':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('INFY.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'INFY.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['INFY.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())
        elif parsed_path.path == '/HDFCBANK':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('HDFCBANK.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'HDFCBANK.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['HDFCBANK.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/ICICIBANK':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('ICICIBANK.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'ICICIBANK.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['ICICIBANK.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/HINDUNILVR':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('HINDUNILVR.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'HINDUNILVR.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['HINDUNILVR.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/BHARTIARTL':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('BHARTIARTL.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'BHARTIARTL.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['BHARTIARTL.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like KOTAKBANK, ITC, etc.

        elif parsed_path.path == '/KOTAKBANK':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('KOTAKBANK.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'KOTAKBANK.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['KOTAKBANK.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/ITC':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('ITC.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'ITC.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['ITC.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like LT, AXISBANK, etc.
        elif parsed_path.path == '/LT':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('LT.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'LT.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['LT.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/AXISBANK':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('AXISBANK.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'AXISBANK.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['AXISBANK.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like SBIN, MARUTI, etc.
        elif parsed_path.path == '/SBIN':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('SBIN.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'SBIN.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['SBIN.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/MARUTI':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('MARUTI.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'MARUTI.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['MARUTI.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like TECHM, BAJFINANCE, etc.
        elif parsed_path.path == '/TECHM':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('TECHM.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'TECHM.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['TECHM.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/BAJFINANCE':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('BAJFINANCE.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'BAJFINANCE.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['BAJFINANCE.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like ULTRACEMCO, POWERGRID, etc.
        elif parsed_path.path == '/ULTRACEMCO':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('ULTRACEMCO.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'ULTRACEMCO.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['ULTRACEMCO.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/POWERGRID':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('POWERGRID.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'POWERGRID.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['POWERGRID.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like ASIANPAINT, INDUSINDBK, etc.
        elif parsed_path.path == '/ASIANPAINT':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('ASIANPAINT.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'ASIANPAINT.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['ASIANPAINT.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/INDUSINDBK':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('INDUSINDBK.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'INDUSINDBK.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['INDUSINDBK.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like HCLTECH, BAJAJFINSV, etc.
        elif parsed_path.path == '/HCLTECH':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('HCLTECH.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'HCLTECH.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['HCLTECH.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/BAJAJFINSV':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('BAJAJFINSV.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'BAJAJFINSV.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['BAJAJFINSV.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like TATASTEEL, BRITANNIA, etc.
        elif parsed_path.path == '/TATASTEEL':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('TATASTEEL.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'TATASTEEL.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['TATASTEEL.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/BRITANNIA':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('BRITANNIA.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'BRITANNIA.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['BRITANNIA.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like COALINDIA, SBILIFE, etc.
        elif parsed_path.path == '/COALINDIA':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('COALINDIA.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'COALINDIA.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['COALINDIA.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/SBILIFE':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('SBILIFE.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'SBILIFE.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['SBILIFE.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like NESTLEIND, ONGC, etc.
        elif parsed_path.path == '/NESTLEIND':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('NESTLEIND.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'NESTLEIND.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['NESTLEIND.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/ONGC':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('ONGC.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'ONGC.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['ONGC.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like TITAN, DIVISLAB, etc.
        elif parsed_path.path == '/TITAN':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('TITAN.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'TITAN.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['TITAN.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/DIVISLAB':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('DIVISLAB.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'DIVISLAB.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['DIVISLAB.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like UPL, WIPRO, etc.
        elif parsed_path.path == '/UPL':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('UPL.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'UPL.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['UPL.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/WIPRO':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('WIPRO.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'WIPRO.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['WIPRO.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like SHREECEM, GRASIM, etc.
        elif parsed_path.path == '/SHREECEM':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('SHREECEM.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'SHREECEM.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['SHREECEM.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/GRASIM':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('GRASIM.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'GRASIM.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['GRASIM.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like IOC, NTPC, etc.
        elif parsed_path.path == '/IOC':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('IOC.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'IOC.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['IOC.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/NTPC':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('NTPC.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'NTPC.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['NTPC.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like HDFCLIFE, CIPLA, etc.
        elif parsed_path.path == '/HDFCLIFE':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('HDFCLIFE.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'HDFCLIFE.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['HDFCLIFE.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/CIPLA':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('CIPLA.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'CIPLA.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['CIPLA.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like DRREDDY, SUNPHARMA, etc.
        elif parsed_path.path == '/DRREDDY':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('DRREDDY.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'DRREDDY.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['DRREDDY.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/SUNPHARMA':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('SUNPHARMA.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'SUNPHARMA.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['SUNPHARMA.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like BAJAJ-AUTO, HINDALCO, etc.
        elif parsed_path.path == '/BAJAJ-AUTO':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('BAJAJ-AUTO.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'BAJAJ-AUTO.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['BAJAJ-AUTO.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/HINDALCO':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('HINDALCO.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'HINDALCO.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['HINDALCO.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like ADANIPORTS, EICHERMOT, etc.
        elif parsed_path.path == '/ADANIPORTS':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('ADANIPORTS.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'ADANIPORTS.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['ADANIPORTS.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/EICHERMOT':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('EICHERMOT.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'EICHERMOT.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['EICHERMOT.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like JSWSTEEL, LTTS, etc.
        elif parsed_path.path == '/JSWSTEEL':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('JSWSTEEL.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'JSWSTEEL.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['JSWSTEEL.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/LTTS':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('LTTS.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'LTTS.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['LTTS.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like ADANIENT, APOLLOHOSP, etc.
        elif parsed_path.path == '/ADANIENT':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('ADANIENT.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'ADANIENT.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['ADANIENT.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        elif parsed_path.path == '/APOLLOHOSP':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            all_data = {}
            stock_data = yf.download('APOLLOHOSP.NS', period="2d")
            stock_json = []
            for index, row in stock_data.iterrows():
                data_point = {
                    "Symbol": 'APOLLOHOSP.NS',
                    "Date": int(index.timestamp()) * 1000,  # Convert to milliseconds
                    "Open": row['Open'],
                    "High": row['High'],
                    "Low": row['Low'],
                    "Close": row['Close'],
                    "Adj Close": row['Adj Close'],
                    "Volume": row['Volume'],
                }
                stock_json.append(data_point)
            all_data['APOLLOHOSP.NS'] = stock_json

            self.wfile.write(json.dumps(all_data).encode())

        # Repeat similar blocks for other symbols like RELIANCE, TCS, etc.

        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'404 Not Found')

    def fetch_previous_close(self, symbol):
        end_date = datetime.now().strftime('%Y-%m-%d')
        start_date = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')
        previous_close_data = yf.download(symbol, start=start_date, end=end_date)
        return previous_close_data['Close'].iloc[0]

def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
