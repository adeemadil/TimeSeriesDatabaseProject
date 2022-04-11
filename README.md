# TimeSeriesDatabaseProject
A time-series database is designed to retrieve and store data records in timestamps as part of a 'time-series'. 
Such time-series data is usually continuous, for example, day-to-day stock prices and sensory measurements. 
With time-series data, changes are tracked and captured at regular intervals or even irregular intervals. 
This type of database allows us to store a large quantity of data in timestamps with quick retrieval and insertion of data encouraging complex evaluation of that data.

As a simple example, I implemented a practical application of a time-series database with TimeScaleDB, built on top of PostgreSQL. 
I attempted to use it for financial data applications and stock trading.
The sample that I will showcase is where I developed an exchange-traded fund (ETF) database, where we track a fund's holdings over time. 
Moreover, I used the arc invest funds, where I looked at the holdings in the arc invest funds and tracked how those holdings changed over time.
