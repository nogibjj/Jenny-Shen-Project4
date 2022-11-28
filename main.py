from fastapi import FastAPI
import uvicorn
from mylib.logic import sector as tickersector
from mylib.logic import financials as tickerfinancials

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "yfinance API. Call /sector or /financials"}

@app.get("/sector/{name}")
async def sector(name: str):
    """Retrieve sector of a specific ticker"""

    result = tickersector(name)
    return {"result": result}


@app.get("/financials/{name}")
async def financials(name: str):
    """Retrieve finanicials data of a specific ticker"""

    result = tickerfinancials(name)
    return {"result": result}


if __name__ == '__main__':
    uvicorn.run(app, port=8000, host='0.0.0.0')
