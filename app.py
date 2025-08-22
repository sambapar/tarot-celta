# -*- coding: utf-8 -*-
"""
Created on Sat Aug 16 13:00:12 2025

@author: samuel
"""

from flask import Flask, request, jsonify, render_template
import tarot_celta
app=Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/tirada",methods=["POST"])
def procesar_tirada():
    data=request.get_json()
    numeros=data.get("numeros",[])
    posiciones=data.get("posiciones",[])
    if not numeros or not posiciones:
        return jsonify({"error":"Faltan datos."}), 400
    if not isinstance(numeros,list) or not isinstance(posiciones,list):
        return jsonify({"error": "Los campos 'tirada' y 'orient' tienen que ser listas"}), 400
    if len(numeros)!=10 or len(posiciones)!=10:
        return jsonify({"error": "Una tirada celta tiene 10 cartas."}), 400
    try:
        numeros=[int(x) for x in numeros]
    except Exception:
        return jsonify({"error":"Todos los números deben ser enteros"}), 400
    if any(n<0 or n>21 for n in numeros):
        return jsonify({"error": "Los arcanos mayores van del 0 al 21."}),400
    if any(p not in ("d","r") for p in posiciones):
        return jsonify({"error": "Cada posión ha de ser 'd' (derecho) o 'r' (revés)"})
    resultado=tarot_celta.tarot_celta(numeros,posiciones)
    imagenes=[f"/static/img/{n}.png" for n in numeros]
    return jsonify({"resultado":resultado,"imagenes":imagenes})
if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=5000)