default:
	@cat makefile

env:
	@python3 -m venv env
	@. env/bin/activate && pip install -r requirements.txt

run:
	@env/bin/python bin/clockdeco_param.py

lint:
	@echo "Linting..."
	@. env/bin/activate && pylint bin/perceptron.py.1


.PHONY: tests
tests:
	pytest -vv tests
