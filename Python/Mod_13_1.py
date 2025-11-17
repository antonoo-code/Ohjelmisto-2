from flask import Flask, request

app = Flask(__name__)
@app.route('/alkuluku/<int:luku>')
def alkuluku(luku):
    alkuluku = True
    for i in range(2,luku):
        if luku % i == 0:
            alkuluku = False
    

    vastaus = {
       "Number":luku,
       "isPrime":alkuluku
    }

    return vastaus

app.run(use_reloader=True, host='127.0.0.1', port=3000)



