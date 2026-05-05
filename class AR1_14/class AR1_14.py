import numpy as np
from flask import Flask, request, jsonify
class AR1_14:
    def __init__(self, T):
        self.T = T
        self.app = Flask(__name__)
        self.route()

    def generate_ar1(self, a, T):
        eps = np.random.normal(0, 1, T)
        x = np.zeros(T)

        for t in range(1, T):
            x[t] = a * x[t-1] + eps[t]

        return x

    def route(self):
        @self.app.route("/helo")
        def api_generate():
            a = float(request.args.get('a', 0.5))
            T = int(request.args.get('T', self.T))

            x = self.generate_ar1(a, T)

            print("API CALLED")
            return jsonify(x.tolist())
    def run(self):
        print(f"API: http://127.0.0.1:5000/helo?a=0.5&T={self.T}")
        self.app.run(debug=True)
app = AR1_14(T=100)
app.run()