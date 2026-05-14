typecheck:
	mypy . --config-file mypy.ini

lint:
	flake8 --config=.flake8