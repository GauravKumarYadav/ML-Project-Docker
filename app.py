import numpy as np
import pandas as pd

from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler
from src.pipeline.predict_pipeline import CustomData, PredictPipeline
from src.logger import logging

application = Flask(__name__)
app = application

# route for home page


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictDataPoint', methods=['GET', 'POST'])
def predictDataPoint():
    if request.method == "GET":
        return render_template('home.html')
    else:
        data = CustomData(
            gender=request.form.get('gender'),  # type: ignore
            race_ethnicity=request.form.get('ethnicity'),  # type: ignore
            parental_level_of_education=request.form.get(
                'parental_level_of_education'),  # type: ignore
            lunch=request.form.get('lunch'),  # type: ignore
            test_preparation_course=request.form.get(
                'test_preparation_course'),  # type: ignore
            reading_score=float(request.form.get(
                'writing_score')),  # type: ignore
            writing_score=float(request.form.get(
                'reading_score'))  # type: ignore
        )
        predict_data = data.get_data_as_dataframe()
        logging.info(f'data input : {predict_data}')
        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(predict_data)

        logging.info(f'predicted data : {results}')

        return render_template('home.html', results=results[0])


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True,port=5000)