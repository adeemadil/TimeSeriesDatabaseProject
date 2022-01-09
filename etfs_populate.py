from os import read
import timescaledb
import csv
import psycopg2
import psycopg2.extras

connection = psycopg2.connect( host=timescaledb.DB_HOST, database=timescaledb.DB_NAME, 
                            user=timescaledb.DB_USER, password=timescaledb.DB_PASS)

cursor = connection.cursor( cursor_factory=psycopg2.extras.DictCursor)

cursor.execute("select * from stock where is_etf = TRUE")

etfs = cursor.fetchall()

dates = ['2022-01-07']
for current_date in dates:
    for etf in etfs:
        print(etf['symbol'])
        with open(f"data/{current_date}/{etf['symbol']}.csv") as f:
            reader = csv.reader(f)
            next(reader)

            for row in reader:
                try:
                    ticker = row[3]
                except Exception as e:
                    print(row)
                
                ticker = row[3]
                #print(ticker)

                if ticker:
                    shares = row[5]
                    weight = row[7]

                    cursor.execute("""
                        SELECT * FROM stock WHERE symbol = %s
                    """, (ticker, ))
                    stock = cursor.fetchone()
                    if stock:
                        cursor.execute("""
                            INSERT INTO etf_holding (etf_id, holding_id, dt, shares, weight)
                            VALUES (%s, %s, %s, %s, %s)
                        """, (etf['id'], stock['id'], current_date, shares.replace(',',''), weight.replace('%','')))

connection.commit()