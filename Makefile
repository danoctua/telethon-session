PYTHON_VERSION = "3.12.7"
VENV_NAME := $(shell basename $(PWD))


compile_requirements_txt:
	pip-compile requirements.in --no-emit-index-url


_install_python_version:
	echo "\n>Install Python version in pyenv if it doesn't exist yet..."
	echo Saving "$(VENV_NAME)" in .python-version
	echo $(VENV_NAME) > .python-version
	echo "-- Checking python pyenv $ installation..."
	if pyenv versions | grep -q $(PYTHON_VERSION); then \
		echo "- python $(PYTHON_VERSION) installation was found in pyenv"; \
	else \
		echo "- python $(PYTHON_VERSION) installation was not found in pyenv, installing it..."; \
		pyenv install $(PYTHON_VERSION); \
	fi

_install_virtualenv:
	# Resets virtual env
	echo "\n>Installing virtual env..."
	echo "- Uninstalling previous venv..."
	pyenv uninstall -f $(VENV_NAME)
	echo "- Installing venv..."
	pyenv virtualenv $(PYTHON_VERSION) $(VENV_NAME)
	pip install --upgrade wheel pip

_install_packages:
	echo "Installing local packages"
	pip3 install -r requirements.txt

_install_pre_commit_hooks:
	pre-commit install

setup-venv: \
	_install_python_version \
	_install_virtualenv \
	_install_packages \
	_install_pre_commit_hooks \


setup:
	./setup.sh


build:
	docker build -t telethon-session-creator:latest .


run: build setup
	docker run --rm --env-file .env -v ./sessions:/app/sessions -it telethon-session-creator:latest


format:
	pre-commit run -a
