# Makefile for Ansible beginners
# Run playbooks, set up environment, and clean up easily

# Default target
all: help

# ---------------------------
# Help
# ---------------------------
help:
	@echo "Available targets:"
	@echo "  setup       - Install dependencies into a Python virtual environment"
	@echo "  run-web     - Run the webservers playbook"
	@echo "  run-project - Run the project playbook"
	@echo "  clean       - Remove virtual environment"
	@echo "  webservers  - Run webservers.yml directly"
	@echo "  lint        - Lint Ansible playbooks"

# ---------------------------
# Setup environment
# ---------------------------
setup:
	@echo "Creating Python virtual environment..."
	python3 -m venv ansible-runner/venv
	ansible-runner/venv/bin/pip install --upgrade pip
	ansible-runner/venv/bin/pip install -r requirements.txt
	@echo "Setup complete! Activate the environment with:"
	@echo "source ansible-runner/venv/bin/activate"

# ---------------------------
# Run playbooks
# ---------------------------
run-web:
	@echo "Running the webservers playbook..."
	ansible-runner/venv/bin/ansible-playbook -i playbooks/inventory/vagrant.ini playbooks/webservers.yml

run-project:
	@echo "Running the project playbook..."
	ansible-runner/venv/bin/ansible-playbook -i playbooks/inventory/vagrant.ini ansible-runner/playbooks/project/playbook.yml

webservers:
	@echo "Running webservers.yml directly (without virtual environment)..."
	ansible-playbook playbooks/webservers.yml

# ---------------------------
# Lint playbooks
# ---------------------------
lint:
	@echo "Linting Ansible playbooks..."
	ansible-lint playbooks/

# ---------------------------
# Clean environment
# ---------------------------
clean:
	@echo "Removing virtual environment..."
	rm -rf ansible-runner/venv
	@echo "Clean complete."
