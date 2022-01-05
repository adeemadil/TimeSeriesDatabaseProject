from influxdb import InfluxDBClient
#client = InfluxDBClient(host='localhost', port=8086)

client = InfluxDBClient(host='mydomain.com', port=8086, username='myuser', password='mypass', ssl=True, verify_ssl=True)

client.create_database('pyexample')