import mysql.connector
from flask import Flask, request


connection = mysql.connector.connect(
    port=3306, #oletusarvo ei pakollinen.
    host="127.0.0.1", #oletusarvo ei pakollinen.
    database = 'esim_peli', 
    user='root',
    password='Rekolammas123',
    autocommit=True)



app = Flask(__name__)
@app.route('/kentta/<icao>')
def kentta (icao):
    airport_data = (f'SELECT ident , name, municipality  FROM airport WHERE ident = "{icao}"')
    cursor = connection.cursor()
    cursor.execute(airport_data)
    result = cursor.fetchall()
    

    ret = {
        "ICAO": result[0][0],
        "Name": result[0][1],
        "Municipality": result[0][2]
            }
    


    return ret


app.run(use_reloader=True, host='127.0.0.1', port=3000)

