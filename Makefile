
default: requirements.txt
	pip install -r requirements.txt

requirements.txt:
	pip-compile -v requirements.in

