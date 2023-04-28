
import os

# Define the directory structure
project_dir = 'Data_Engineering_Project'
data_dir = os.path.join(project_dir, 'data')
code_dir = os.path.join(project_dir, 'code')
docs_dir = os.path.join(project_dir, 'docs')

# Create the main project directory if it doesn't exist
if not os.path.exists(project_dir):
    os.mkdir(project_dir)

# Create the subdirectories
os.mkdir(data_dir)
os.mkdir(code_dir)
os.mkdir(docs_dir)

# Create empty files in each folder
open(os.path.join(data_dir, 'data.csv'), 'a').close()
open(os.path.join(code_dir, 'main.py'), 'a').close()
open(os.path.join(docs_dir, 'README.md'), 'a').close()

