import os
from pathlib import Path


list_of_files = [
    '.github/workflows/'.gitkeep,
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py'
    'src/components/model_evaluation.py',
    'src/pipelines/__init__.py',
    'src/pipelines/training_pipeline.py',
    'src/pipelines/prediction_pipeline.py',
    'src/utils/__init__.py',
    'src/utils/utils.py',
    'src/logger/logger.py',
    'src/exception/exception',
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',
    'init_setup.py',
    'requirements.txt',
    'setup.py',
    'setup.cfg',
    'project.toml',
    'tox.ini',
    'experiment/experiments.ipynb',
]


for filepaths in list_of_files:
    Path(filepaths).touch(exist_ok=True)
    print(f"Created: {filepaths}")