python
import os

# Define the directory for the README file
docs_dir = 'Data_Engineering_Project/docs'
readme_path = os.path.join(docs_dir, 'README.md')

# Prompt the user for the contents of the README file
readme_contents = input('Enter the contents of the README file: ')

# Write the contents to the file
with open(readme_path, 'w') as readme_file:
    readme_file.write(readme_contents)

# Verify that the file was written successfully
if os.path.isfile(readme_path):
    print('README file was created successfully!')
else:
    print('README was not created.')
