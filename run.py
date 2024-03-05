import osquery
from flask import Flask, request

app = Flask(__name__)


@app.get("/exec")
def get():
    instance = osquery.SpawnInstance()
    instance.open()
    query = request.args.get("query", default="", type=str)
    print("Richiesta GET:", query)
    query_result = instance.client.query(query)
    print("Risposta:", query_result.response)
    return query_result.response, 200


@app.post("/exec")
def post():
    instance = osquery.SpawnInstance()
    instance.open()
    query = str(request.data, "utf-8")
    print("Richiesta POST:", query)
    query_result = instance.client.query(query)
    print("Risposta:", query_result.response)
    return query_result.response, 200


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)
