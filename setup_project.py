import os
folders = [
    'app/routes', 'app/models', 'app/services', 'app/templates',
    'app/static', 'ml', 'tests'
]
files = [
    'app/__init__.py', 'app/routes/main.py', 'app/models/stock_model.py',
    'app/services/data_service.py', 'app/templates/index.html',
    'app/static/styles.css', 'app/extensions.py', 'ml/train.py',
    'ml/preprocess.py', 'ml/model.pkl', 'ml/utils.py', 'config.py',
    'run.py', 'requirements.txt', 'README.md', 'tests/test_app.py'
]
for folder in folders:
    os.makedirs(folder, exist_ok=True)
for file in files:
    with open(file, 'w') as f:
        pass
