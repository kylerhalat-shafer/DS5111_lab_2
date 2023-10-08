default:
	@cat makefile

env:
	@python3 -m venv env
	@. env/bin/activate && pip install -r requirements.txt

run:
	@env/bin/python bin/clockdeco_param.py

lint:
	@pylint --generate-rcfile >> pylintrc

.PHONY: tests
tests:
	pytest -vv tests
