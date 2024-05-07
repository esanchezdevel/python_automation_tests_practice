# How to create requirements.txt file
- Install pipreqs
    `pip install pipreqs`

- Execute pipreqs
    - `pipreqs . --ignore ".venv"`

# How to run pytests indicating one specific Mark
- pytest -m login

# How to run pytests generating an HTML report
- Install the html library:
    - pip install pytest-html

- Execute the command:
    - pytest -m login --html=reports/report.html