SRCDIR = fasseh
PYTHON2_7 = $(shell python --version 2>&1 | grep 2.7)
PYTHON = python2.7

.PHONY: requirements
requirements:
ifneq ($(PYTHON2_7), )
	pip install -r requirements
else
	$(error Bad python version, please install version 2.7)
endif

.PHONY: clean
clean:
	sudo rm -rf build dist fasseh.egg-info logs
	find . -name '*.pyc' -delete

.PHONY: run
run:
	$(PYTHON) $(SRCDIR)/fasseh.py

.PHONY: install
install: requirements
	sudo $(PYTHON) setup.py install

.PHONY: build
build: requirements
	sudo $(PYTHON) setup.py develop


.PHONY: test
test: install
	$(PYTHON) -m unittest discover

.PHONY: testConvention
testConvention:
	$(PYTHON) -m pep8 fasseh
