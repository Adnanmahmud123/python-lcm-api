from flask import Flask, request, Response
from math import gcd
import re

app = Flask(__name__)

@app.route("/mail_adnanmahin_gmail_com", methods=["GET"])
def calculate_lcm():
    x = request.args.get("x", "")
    y = request.args.get("y", "")

    if not re.fullmatch(r"[0-9]+", x) or not re.fullmatch(r"[0-9]+", y):
        return Response("NaN", mimetype="text/plain")

    x = int(x)
    y = int(y)

    if x == 0 or y == 0:
        result = 0
    else:
        result = abs(x * y) // gcd(x, y)

    return Response(str(result), mimetype="text/plain")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)