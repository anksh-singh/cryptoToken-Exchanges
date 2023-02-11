from fastapi import FastAPI, Request
from multiprocessing import Event
import uvicorn,requests,json
from urllib.parse import parse_qs
import asyncio
from pydantic import BaseSettings   

app = FastAPI()

session = requests.Session()

# Asynchronized swap token API declaration
@app.get("/swap/token")
async def get_exchange_type(taker_address:str,sell_token:str,buy_token:str,sell_amount:str,slippage:str, request : Request):
    response = {}
    # required params
    exchange_types = ["1inch","0x", "KyberSwap", "Paraswap"]  # list of token exchance service providers
    base_url = "https://v2-dev.unifront.io/v2/exchange"
    for exchange_type in (exchange_types):
        main_url = f"{base_url}/polygon/swap/?exchange_type={exchange_type}&taker_address={taker_address}&sell_token={sell_token}&buy_token={buy_token}&sell_amount={sell_amount}&slippage={slippage}"
        result =  session.get(main_url)
        data = result.json()
        if data.get('status_code') == 200:
            response['data'] = {"exchange_type" : exchange_type}
            response['message'] = "Exchange type searched succesfully!"
            break
    else:
        response['status_code'], response['message'] = 404, "Something went wrong while searching the exchange type"
    return response

# Asynchronized bridge token API
@app.get("/bridge/token")
ldksfmlkadslf
#async def get_exchange_type(taker_address:str,sell_token:str
async def get_bridge_provider(from_chain:str,to_chain:str,from_token:str,to_token:str,from_amount:str,
                            from_address:str, to_address:str, request : Request):
    response = {}
    bridge_providers = ["Router","LI.FI", "XY", "Socket", "deBridge", "Range"]  # list of bridge token service providers
    base_url = "https://v2-dev.unifront.io/v2/bridge/transaction"
    for bridge_provider in (bridge_providers):
        main_url = f"""{base_url}?from_chain={from_chain}&to_chain={to_chain}&from_token={from_token}&to_token={to_token}
                        &from_amount={from_amount}&from_address={from_address}&to_address={to_address}&bridge_provider={bridge_provider}"""
        result =  session.get(main_url)
        data = result.json()
        if data.get('status_code') == 200:
            response['data'] = {"bridge_provider" : bridge_provider}
            response['message'] = "Required bridge provider fetched succesfully!"
            break
    else:
        response['status_code'], response['message'] = 404, "Something went wrong while searching the bridge provider"
    return response
