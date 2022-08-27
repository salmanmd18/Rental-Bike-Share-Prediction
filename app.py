import sys,pip,os,json
import pandas as pd
#from matplotlib.style import context
from flask import Flask,send_file, abort, render_template, request,url_for
#from sharing.logger import logging
from sharing.exception import SharingException
from sharing.config.configuration import Configuration
from sharing.constant import CONFIG_DIR, get_current_time_stamp
from sharing.pipeline.pipeline import Pipeline
from sharing.util.util import read_yaml_file, write_yaml_file
from sharing.logger import get_log_dataframe
from sharing.entity.sharing_predictor import SharingPredictor, SharingData
from sharing.config.configuration import *
from sharing.component.data_ingestion import DataIngestion

app = Flask(__name__)


ROOT_DIR = os.getcwd()
SAVED_MODELS_DIR_NAME = "saved_models"
MODEL_DIR = os.path.join(ROOT_DIR, SAVED_MODELS_DIR_NAME)

SHARING_DATA_KEY = "sharing_data"
MEDIAN_SHARING_VALUE_KEY = "median_share_value"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    try:
       
        context = {
        SHARING_DATA_KEY: None,
        MEDIAN_SHARING_VALUE_KEY: None
    }

        if request.method == 'POST':
            season = int(request.form['season'])
            year = int(request.form['year'])
            month = int(request.form['month'])
            hour = int(request.form['hour'])
            holiday = int(request.form['holiday'])
            weekday = int(request.form['weekday'])
            workingday = int(request.form['workingday'])
            weather = int(request.form['weather'])
            temp = float(request.form['temp'])
            humidity = float(request.form['humidity'])
            windspeed = float(request.form['windspeed'])
            print(season,year,month,hour,holiday,weekday,workingday, weather, temp, humidity,windspeed)
            sharing_data = SharingData(season=season,
            year = year,month= month,hour = hour, holiday=holiday, weekday = weekday, workingday=workingday, weather=weather, temp = temp,
            humidity=humidity, windspeed=windspeed)
            sharing_df = sharing_data.get_sharing_input_data_frame()
            sharing_predictor = SharingPredictor(model_dir=MODEL_DIR)
            median_sharing_value = sharing_predictor.predict(X=sharing_df)
            context = {
            SHARING_DATA_KEY: sharing_data.get_sharing_data_as_dict(),
            MEDIAN_SHARING_VALUE_KEY: int(median_sharing_value),
            }
            return render_template('predict.html', context=context)
        return render_template("predict.html", context=context)
    
    except Exception as e:
            raise SharingException(e, sys) from e



if  __name__=="__main__":
    app.run(debug=True)