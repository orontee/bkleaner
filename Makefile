PYTHON = python

version = 0.1

sources = bkleaner/__init__.py bkleaner/errors.py bkleaner/schemes.py
sources += bkleaner/settings.py bkleaner/transform.py scripts/bkleaner

build: dist/bkleaner-$(version).tar.gz

help:
	@echo "The main targets are:"
	@echo "  build      Build the package"
	@echo "  install    Install the package"
	@echo "  uninstall  Uninstall the package"
	@echo "  test       Run tests"

.PHONY: build help clean install uninstall distclean doc test

install: build
	pip install dist/bkleaner-$(version).tar.gz

uninstall:
	pip uninstall -y bkleaner

dist/bkleaner-$(version).tar.gz: $(sources)
	python setup.py sdist

clean:
	-rm -f MANIFEST
	-rm -rf bkleaner.egg-info/
	-rm -rf bkleaner/__pycache__/
	-rm -f bkleaner/*.pyc
	cd doc; $(MAKE) $@

distclean: clean
	-rm -rf dist

doc:
	cd doc; $(MAKE) html

test:
	PYTHONPATH=. $(PYTHON) bkleaner/tests/test_transform.py
