from sharing.config.configuration import Configuration
from sharing.pipeline.pipeline import Pipeline
from sharing.exception import SharingException
from sharing.logger import logging
import os,sys

def main():
    try:
        
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        data_validation_config = Configuration().get_data_validation_config()
        print(data_validation_config)
        pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)


if __name__ == "__main__":
    main()
