import os
from pathlib import Path


list_of_files = [
    '.github/workflows/.gitkeep',
    'src/__init__.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_evaluation.py',
    # 'src/components/trainer.py'
    'src/pipelines/__init__.py',
    'src/pipelines/training_pipeline.py',
    'src/pipelines/prediction_pipeline.py',
    'src/utils/__init__.py',
    'src/utils/utils.py',
    'src/logger/logger.py',
    'src/exception/exception.py',
    'tests/unit/__init__.py',
    'tests/integration/__init__.py',
    'init_setup.sh',
    'requirements.txt',
    'setup.py',
    'setup.cfg',
    'project.toml',
    'tox.ini',
    'experiment/experiments.ipynb',
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !='':
        os.makedirs(filedir, exist_ok=True)

    if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass