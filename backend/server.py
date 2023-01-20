from fastapi import FastAPI, Request
from fastapi_utils.tasks import repeat_every
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import json 
from datetime import datetime
from constants import CORS_URLS
from bitcoin_timestamp import BitcoinTimestamp
from custom_util import get_live_bitcoin_price, convert_date_to_text
from database_connection import DatabaseConnection

# TODO (3.1): define FastAPI app
app = FastAPI()
# TODO (5.4.1): define database connection
dbConnection = DatabaseConnection()

# TODO (3.2): add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=CORS_URLS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# TODO (3.1)
"""
a index function to test if server is running
"""
@app.get("/")
async def root():
    content = {"message": "Hello world! This is a bitcoin monitoring service!"}
    return json.dumps(content)

# TODO (5.4.2)
"""
repeated task to update bitcoin prices periodically
"""
@app.on_event("startup")
@repeat_every(seconds=15)
def update_bitcoin_price():
    price = get_live_bitcoin_price()
    if price != -1:
        dbConnection.insert_timestamp(BitcoinTimestamp(convert_date_to_text(datetime.now()), price))

# TODO (5.4.3)
"""
API endpoint to get bitcoin prices

:return:
    a list of bitcoinstamps
:rtype:
    json
"""
@app.get("/get_bitcoin_prices")
def get_bitcoin_prices():
    timestampes = dbConnection.get_all_timestampes()
    data = timestampes.__dict__
    return json.dumps(data)

# main function to run the server
if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)