from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from scipy import stats
import os
# Import các mô hình từ các tệp riêng biệt
from linear import train_and_predict_linear, evaluate_model as eval_linear
from neural import train_and_predict_neural, evaluate_model as eval_neural
from lassor import train_and_predict_lassor, evaluate_model as eval_lassor

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def index():
    return render_template("indes.html")
if __name__ == "__main__":
    app.run()