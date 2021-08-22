run:
	FLASK_DEBUG=1 python3 -m flask run

run_with_pipenv:
	python3 -m pipenv install
	FLASK_DEBUG=1 python3 -m pipenv run flask run
