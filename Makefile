PYTHON := python3
PYTHON2 := python2
PYFLAKES := pyflakes

default: test #lint

test:
	$(PYTHON) setup.py test

check: test

dist:
	rm -rf dist/*
	WHEEL_TOOL=$(shell which wheel) $(PYTHON2) setup.py sdist bdist_wheel

publish: dist
	find dist -type f -exec gpg2 --detach-sign -a {} \;
	twine upload dist/*

setup-pypi-test:
	$(PYTHON) setup.py register -r pypitest
	$(PYTHON) setup.py sdist upload -r pypitest

setup-pypi-publish:
	$(PYTHON) setup.py register -r pypi
	$(PYTHON) setup.py sdist upload --sign -r pypi

lint:
	$(PYFLAKES) vev/*.py tests/*.py || exit 0

clean:
	find . -name '*.pyc' -exec rm -f {} \;
	find . -name __pycache__ -type d | xargs rm -rf
	rm -rf vev.egg-info .eggs build dist .tox
