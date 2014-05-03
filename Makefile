version = 0.1

sources = bkleaner/__init__.py bkleaner/errors.py bkleaner/schemes.py
sources += bkleaner/settings.py bkleaner/transform.py scripts/bkleaner

.PHONY: install uninstall clean distclean doc

dist/bkleaner-$(version).tar.gz: $(sources)
	python setup.py sdist

install: dist/bkleaner-$(version).tar.gz
	pip install $<

uninstall:
	pip uninstall -y bkleaner

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
