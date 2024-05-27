import websocket
import json

def on_message(ws, message):
    # Check for ping/pong messages
    if message == b'\x89\x00':
        ws.send(b'\x8a\x80\xcc\xb4\x0c\x19')  # Respond to pings
        return  # Skip further processing

    try:
        # Extract the JSON part (remove initial bytes)
        json_string = message.split(b'\x01\xc3')[1]  # Split but keep as bytes
        data = json.loads(json_string.decode('utf-8'))  # Decode to string before loading

        # Now you have a clean Python dictionary containing the token data
        print("Token Creation Event:")
        print(f"  Mint: {data['mint']}")
        print(f"  Initial Buy: {data['initialBuy']} SOL")
        print(f"  Market Cap (SOL): {data['marketCapSol']}")
        print("Raw data (bytes):", json_string)  # Print the raw bytes here
        # ... extract and process other fields as needed

    except (IndexError, json.JSONDecodeError) as e:
        print("Error parsing message:", e)

def on_error(ws, error):
    print(error)

def on_close(ws, close_status_code, close_msg):
    print("### Amon This was closed ###")

def on_open(ws):
    # Subscribe to token creation events
    ws.send(json.dumps({"method": "subscribeNewToken"}))

    # Subscribe to trades made by accounts
    ws.send(json.dumps({
        "method": "subscribeAccountTrade",
        "keys": ["AArPXm8JatJiuyEffuC1un2Sc835SULa4uQqDcaGpAjV"]
    }))

    # Subscribe to trades on tokens
    ws.send(json.dumps({
        "method": "subscribeTokenTrade",
        "keys": ["91WNez8D22NwBssQbkzjy4s2ipFrzpmn5hfvWVe2aY5p"]
    }))

if __name__ == "__main__":
    websocket.enableTrace(True)  # Optional: Enable debug logging
    ws = websocket.WebSocketApp(
        "wss://pumpportal.fun/api/data",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()  
