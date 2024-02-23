# Project Command Pattern and Plugins

In this project, you will be learning a few differencing concepts:

1. Read, Evaluate, Print, Loop (REPL)
2. The object oriented design pattern: Command

### Command Assignment Readings
* https://refactoring.guru/design-patterns/command

### Command Pattern Lecture - Instructor Required - [here](https://youtu.be/3DVUN091T5g)

3. Knowing when to use If statements and Exceptions by following Easier to ask for forgiveness than permission(EAFP), or Look Before You Leap LBYL.

4. Adding Plugins with Using ChatGPT - Gets rid of the manual loading of commands

### Plugins Lecture - Instructor Required - [here](https://youtu.be/c2PmjazGW2w)


## Setup Instructions
1. Clone the repo
2. CD into the project folder
3. Create the virtual environment 
4. Activate the virtual environment (VE)
5. Install Requirements

## Test Commands
1. pytest run all tests
2. pytest tests/test_main.py <- Run just the tests in this file
3. pytest --pylint --cov <- Run Pylint and Coverage (Can be run independently)

## Current Libraries Installed
1. [Pytest - Testing Framework](https://docs.pytest.org/en/8.0.x/)
2. [Faker - Fake Data Creation](https://faker.readthedocs.io/en/master/)
3. [Pytest Coverage](https://pytest-cov.readthedocs.io/en/latest/readme.html)
4. [Pytest Pylint](https://pylint.readthedocs.io/en/stable/development_guide/contributor_guide/tests/launching_test.html)

## Adding Library
1.  Make sure you are in the correct VE, if not sure run "deactivate"
2.  Activate the VE
3.  Run pip freeze > requirements.txt