PROG = hsltimes
DOCS = docs
PREFIX = $(HOME)/.local
MAN_SRC = $(shell pwd)/$(DOCS)/$(PROG).1
MAN_DST = $(PREFIX)/man/man1/
PYTHON = python3

.PHONY: build
build:
	@echo "Building distribution packages..."
	rm -rf dist/
	$(PYTHON) -m build

.PHONY: clean
clean:
	@echo "Cleaning distribution packages..."
	rm -rf dist/

.PHONY: man
man:
	pandoc $(DOCS)/$(PROG).1.md -s -t man -o $(DOCS)/$(PROG).1

.PHONY: install
install:
	@echo "Installing $(PROG)..."
	$(PYTHON) -m pip uninstall -qq --yes $(PROG)
	$(PYTHON) -m pip install -qq .
	@echo "Install successful."

.PHONY: install-editable
install-editable:
	@echo "Installing $(PROG)..."
	$(PYTHON) -m pip uninstall -qq --yes $(PROG)
	$(PYTHON) -m pip install -qq -e .
	@echo "Install successful."

.PHONY: uninstall
uninstall:
	@echo "Uninstalling $(PROG)..."
	$(PYTHON) -m pip uninstall -qq --yes $(PROG)
	@echo "Uninstall successful."

.PHONY: tests
tests:
	@echo "Running tests..."
	$(PYTHON) -m unittest -v