import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, send_file
import io
import os

app = Flask(__name__)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

@app.route("/")
def home():

    arr = np.random.randint(1, 100, 20)
    sorted_arr = bubble_sort(arr.copy())

    fig, ax = plt.subplots()

    ax.bar(range(len(sorted_arr)), sorted_arr, color="green")
    ax.set_title("Bubble Sort Result")

    img = io.BytesIO()
    plt.savefig(img, format="png")
    img.seek(0)

    return send_file(img, mimetype="image/png")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
