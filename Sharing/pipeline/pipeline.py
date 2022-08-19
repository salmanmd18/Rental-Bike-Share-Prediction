import os, sys
import uuid
import pandas as pd
from threading import Thread
from sharing.constant import *
from sharing.logger import logging
from sharing.exception import SharingException
from sharing.config.configuration import Configuration
from sharing.entity.config_entity import *
from sharing.entity.artifact_entity import *
from sharing.component.data_ingestion import DataIngestion
# from sharing.component.data_validation import DataValidation
# from sharing.component.data_transformation import DataTransformation
# from sharing.component.model_trainer import ModelTrainer
# from sharing.component.model_evaluation import ModelEvaluation
# from sharing.component.model_pusher import ModelPusher


class Pipeline:
    def __init__(self,config:Configuration) -> None:
        try:
            self.config = config

        except Exception as e:
            raise SharingException(e,sys) from e
    
    def start_data_ingestion(self)-> DataIngestionArtifact:
        try:
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise SharingException(e,sys) from e

    def start_data_validation(self):
        pass

    def start_data_transformation(self):
        pass

    def start_model_trainer(self):
        pass

    def start_model_evaluation(self):
        pass

    def start_model_pusher(self):
        pass


    def run_pipeline(self):
        try:

            data_ingestion_artifact = self.start_data_ingestion()


        except Exception as e:
            raise SharingException(e,sys) from e

