# PumpPortal Real-time Token Creation Subscriber

This Python script connects to the PumpPortal WebSocket API (`wss://pumpportal.fun/api/data`) to receive real-time updates whenever new tokens are created on the platform.

## Features

* Subscribes to the `subscribeNewToken` event to capture token creation events.
* Extracts and prints essential token details:
    * Mint address
    * Initial buy amount (SOL)
    * Market cap (SOL)
    * Raw byte data from the WebSocket message
* Handles ping/pong messages to maintain the WebSocket connection.
* Includes basic error handling.

## Installation

1. **Install dependencies:**
   ```bash
   pip install websocket-client
