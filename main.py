from TextSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from TextSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
from TextSummarizer.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from TextSummarizer.pipeline.stage_04_model_trainer import ModelTrainerPipeline
from TextSummarizer.logging import logger

STAGE_NAME = "Data Ingestion stage"

try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   data_ingestion = DataIngestionTrainingPipeline()
   data_ingestion.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Validation stage"

try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   data_validation = DataValidationTrainingPipeline()
   data_validation.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Data Transformation stage"

try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   data_transformation = DataTransformationTrainingPipeline()
   data_transformation.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e

STAGE_NAME = "Model Trainer stage"

try:
   logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
   model_trainer = ModelTrainerPipeline()
   model_trainer.main()
   logger.info(f">>>>>> {STAGE_NAME} completed <<<<<<\n\nx==========x")

except Exception as e:
        logger.exception(e)
        raise e