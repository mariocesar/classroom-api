
default: requirements.txt
	pip install -r requirements.txt
	pip install -e .

requirements.txt:
	pip-compile -v requirements.in
