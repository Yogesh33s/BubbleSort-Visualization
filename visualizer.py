import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, send_file
import io
import os
import imageio

app = Flask(__name__)

def bubble_sort_steps(arr):
    steps = []
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            steps.append(arr.copy())

    return steps

@app.route("/")
def home():

    arr = np.random.randint(1, 100, 20)
    steps = bubble_sort_steps(arr.copy())

    frames = []

    for step in steps:
        fig, ax = plt.subplots()
        ax.bar(range(len(step)), step, color="blue")
        ax.set_title("Bubble Sort Visualization")

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)

        frames.append(imageio.v2.imread(buf))
        plt.close(fig)

    gif_bytes = io.BytesIO()
    imageio.mimsave(gif_bytes, frames, format="GIF", duration=0.2)
    gif_bytes.seek(0)

    return send_file(gif_bytes, mimetype="image/gif")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
