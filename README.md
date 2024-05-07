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

# How to run pytests tests in paralell. The number of paralell tests to be executed should not be greated than the number of Cores of the computer
- Install pytest-xdist
    - pip install pytest-xdist

- Execute the command:
    - pytest -m login --html=reports/report.html -n=2

# How to Debug pytests
- Install pytest-vscodedebug library
    - pip install pytest-vscodedebug

- Create .vscode/launch.json file with content:
    {
    "configurations": [
      {
        "name": "Python: Remote Attach",
        "type": "python",
        "request": "attach",
        "connect": {
          "host": "localhost",
          "port": 10001,
        },
        "pathMappings": [
          {
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "."
          }
        ]
      }
    ]
  }

- Connect vscode to be able to debug running manually
    - py.test --vscodedebug test_testfile.py

- Execute debug