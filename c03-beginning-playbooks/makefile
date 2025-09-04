
help: ## Show help for all targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

roles: ## Install required Ansible Galaxy roles
	ansible-galaxy collection install community.general
	ansible-galaxy collection install ansible.posix

lint: ## Lint Ansible playbooks
	ansible-lint playbooks/

test: ## Check playbooks syntax
	ansible-playbook playbooks/trivial.yml --syntax-check