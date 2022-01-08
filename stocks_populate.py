import timescaledb
import alpaca_trade_api as tradeapi
import psycopg2
import psycopg2.extras

connection = psycopg2.connect( host=timescaledb.DB_HOST, database=timescaledb.DB_NAME, 
                            user=timescaledb.DB_USER, password=timescaledb.DB_PASS)

cursor = connection.cursor( cursor_factory=psycopg2.extras.DictCursor)

api = tradeapi.REST(timescaledb.API_KEY, timescaledb.API_SECRET, base_url=timescaledb.API_URL)

assets = api.list_assets()

for asset in assets:
    print(f"Inserting a stock {asset.name} {asset.symbol}")
    cursor.execute("""
        INSERT INTO stock (name, symbol, exchange, is_etf)
        VALUES (%s, %s, %s, %s)
    """, (asset.name, asset.symbol, asset.exchange, False))

connection.commit()