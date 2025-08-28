from flask import Flask, jsonify, request
from rivescript import RiveScript
import mysql.connector
from heyoo import WhatsApp

app = Flask(__name__)

@app.route("/webhook/", methods=["POST", "GET"])
def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == "DiegusToken4321":
            return request.args.get("hub.challenge")
        else:
            return "Auth error."

    datos = request.get_json()
    numero = datos['entry'][0]['changes'][0]['value']['messages'][0]['from']
    texto = datos['entry'][0]['changes'][0]['value']['messages'][0]['text']['body']
    id_msg = datos['entry'][0]['changes'][0]['value']['messages'][0]['id']
    tiempo = datos['entry'][0]['changes'][0]['value']['messages'][0]['timestamp']

    if texto is not None:
        bot = RiveScript()
        bot.load_file("chatbot.rive")
        bot.sort_replies()

        salida = bot.reply("localuser", texto)
        salida = salida.replace("\\n", "\\\n")
        salida = salida.replace("\\", "")

        conn = mysql.connector.connect(
            host="mysql-diegu.alwaysdata.net",
            user="diegu",
            password="6*M*n5cAXiM_qJS",
            database="diegu_chat"
        )
        consulta = conn.cursor()
        consulta.execute("SELECT count(id) FROM registro WHERE id_wa='" + id_msg + "';")
        cantidad, = consulta.fetchone()
        cantidad = int(cantidad)

        if cantidad == 0:
            query = (
                "INSERT INTO registro "
                "(mensaje_recibido, mensaje_enviado, id_wa, timestamp_wa, telefono_wa) VALUES "
                "('" + texto + "','" + salida + "','" + id_msg + "','" + tiempo + "','" + numero + "');"
            )
            consulta.execute(query)
            conn.commit()
            enviar_msg(numero, salida)
            return jsonify({"status": "success"}, 200)

def enviar_msg(destino, salida):
    token = "EAA0eSQMe93YBPFFsbBZAXdRH2NE3LtPMwaPOLAOOKeStEV8uksBLWi7mCDPZCYZC8hVCnNiNzLwGQ7bkwleZBTStiiSvoFcrC67ZB6lgkvgAqmBmYq5BAhJzhDOwF70b8XXgRiA5jKRIZAUL8nb9MivVWXcDIuwcUlPWQfLN5rIxPDEmMQ2qJld9g3nYpH8NTDdUEB4CGstbcI35FW8DcXS9Mgrj38EfoBOZBD77Cqen5ZAONLTMgwZDZD"
    id_numero = "687569721116449"
    cliente = WhatsApp(token, id_numero)
    destino = destino.replace("521", "52")
    cliente.send_message(salida, destino)

if __name__ == "__main__":
    app.run(debug=True)
