import matplotlib
matplotlib.use('Agg')  # important for servers

import matplotlib.pyplot as plt
import numpy as np
from flask import Flask, send_file
import io

app = Flask(__name__)

def bubble_sort(arr):
    n = len(arr)
    steps = []

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
            steps.append(arr.copy())

    return steps

def create_plot():
    arr = np.random.randint(1, 100, 20)
    steps = bubble_sort(arr.copy())

    fig, ax = plt.subplots()

    for step in steps:
        ax.clear()
        ax.bar(range(len(step)), step, color='blue')

    ax.set_title("Bubble Sort Visualization")

    img = io.BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)

    return img

@app.route("/")
def home():
    img = create_plot()
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
