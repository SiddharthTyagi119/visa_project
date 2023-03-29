from collections import namedtuple
from datetime import datetime
from collections import namedtuple
from datetime import datetime
import uuid
from visa.config.configuration import Configuartion
from visa.logger import logging
from visa.exception import CustomException
from threading import Thread
from typing import List
import os, sys
from collections import namedtuple
from datetime import datetime
import pandas as pd
from multiprocessing import Process
from visa.entity.artifact_entity import DataIngestionArtifact
from visa.components.data_ingestion import DataIngestion



class Pipeline():
#caling configuration class 
    def __init__(self, config: Configuartion = Configuartion()) -> None:
        try:
            self.config = config
        except Exception as e:
            raise CustomException(e, sys) from e

#initiate our data ingestion, this fn will return data ingestion artifact
    def start_data_ingestion(self) -> DataIngestionArtifact:
        try:
            #passing the variables under data ingestion class and then initiating it
            data_ingestion = DataIngestion(data_ingestion_config=self.config.get_data_ingestion_config())
            return data_ingestion.initiate_data_ingestion()
        except Exception as e:
            raise CustomException(e, sys) from e

#calling the pipeline
    def run_pipeline(self):
        try:
             #data ingestion

            data_ingestion_artifact = self.start_data_ingestion()
           
        except Exception as e:
            raise CustomException(e, sys) from e

