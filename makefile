#Note you must have a Virtualenv ‘env’ (default) created before
#running these commands

ENVIRONMENT = env

lint:
	#Just Pylint with config
	$(ENVIRONMENT)/bin/pylint src/ -rn --rcfile=pylint_config.txt
	$(ENVIRONMENT)/bin/pylint test/ -rn --rcfile=pylint_config.txt

run:
	#Run the program
	$(ENVIRONMENT)/bin/python main.py

status: tests lint
	#Overall project status with lint and tests

tests:
	#Just run unit tests and display code coverage result
	$(ENVIRONMENT)/bin/coverage run test/run_tests.py --include src/*,test/*
	$(ENVIRONMENT)/bin/coverage report -m --skip-covered --include src/*,test/*
