
help: ## Show help for all targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

bootstrap: ## Generate a self-signed certificate
	openssl req -x509 -nodes -newkey rsa:2048 -subj /CN=localhost -keyout playbooks/files/nginx.key -out playbooks/files/nginx.crt

up: ## Bring up all VMs defined in Vagrantfile/config.json
	vagrant up

halt: ## Halt all VMs
	vagrant halt

down: ## Destroy all VMs
	vagrant destroy -f

provision: ## Re-run Ansible provisioners inside VMs
	vagrant provision

status: ## Check VM status
	vagrant status

ssh: ## SSH into a VM: make ssh VM=bionic
	vagrant ssh $(VM)

reload: ## Reload VM configs (useful after changing Vagrantfile)
	vagrant reload

lint: ## Lint Ansible playbooks
	ansible-lint playbooks/

test: ## Check playbooks syntax
	ansible-playbook playbooks/trivial.yml --syntax-check