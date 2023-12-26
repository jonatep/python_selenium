import sys
import os
from behave.__main__ import main as behave_main

absolute_path = os.path.dirname(__file__)
results_folder = "allure-results"
full_path = absolute_path.replace('launch', results_folder)

for root, dirs, files in os.walk(full_path):
    for file in files:
        if file.endswith('.json'):
            os.remove(os.path.join(root, file))

if __name__ == "__main__":
    sys.exit(behave_main('--tags=\"@test\"'))
