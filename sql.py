import psycopg2

connection = psycopg2.connect(host="localhost", port="5432", database="chinook")
cursor = connection.cursor()

# cursor.execute('select "Name" from "Artist"')
cursor.execute('select * from "Track" where "Composer" = %s',["Queen"])

results = cursor.fetchone()
connection.close()

for result in results:
    print(result)


