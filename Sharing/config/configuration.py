import os,sys
from sharing.entity.config_entity import *
from sharing.exception import SharingException
from sharing.util.util import read_yaml_file
from sharing.constant import *
from sharing.logger import logging

class Configuration:
    def __init__(self,
        config_file_path:str = CONFIG_FILE_PATH,
        current_time_stamp = CURRENT_TIME_STAMP
        ) -> None:
        try:
            self.config_info = read_yaml_file(file_path=config_file_path)
            self.training_pipeline_config = self.get_training_pipeline_config()
            self.time_stamp = current_time_stamp
        except Exception as e:
            raise SharingException(e,sys) from e

    def get_data_ingestion_config(self) ->DataIngestionConfig:
        pass

    def get_data_validation_config(self) ->DataValidationConfig:
        pass

    def get_data_transformation_config(self) ->DataTransformationConfig:
        pass

    def _get_model_trainer_config(self) ->ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self) ->ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self) ->ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        try:
            training_pipeline_config = self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir = os.path.join(ROOT_DIR,
            training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
            training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY]
            )
            training_pipeline_config = TrainingPipelineConfig(artifact_dir=artifact_dir)
            logging.info(f"Training pipleine config: {training_pipeline_config}")
            return training_pipeline_config
        except Exception as e:
            raise SharingException(e,sys) from e