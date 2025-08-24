
help: # Show help for all targets
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m %s\n", $$1, $$2}'

bootstrap: # Install Vagrant on the host (via Ansible playbook)
	ansible-playbook playbooks/install-vagrant.yml --ask-become-pass
	ansible-playbook playbooks/install-ansible-lint.yml --ask-become-pass

up: # Bring up all VMs defined in Vagrantfile/config.json
	vagrant up

provision: # Re-run Ansible provisioners inside VMs
	vagrant provision

status: # Check VM status
	vagrant status

ssh: # SSH into a VM: make ssh VM=bionic
	vagrant ssh $(VM)

reload: # Reload VM configs (useful after changing Vagrantfile)
	vagrant reload

halt: # Halt all VMs
	vagrant halt

destroy: # Destroy all VMs (CAREFUL!)
	vagrant destroy -f

roles: # Install required Ansible Galaxy roles
	ansible-galaxy install -r playbooks/requirements.yml -p playbooks/roles

lint: ## Lint Ansible playbooks
	ansible-lint playbooks/

test: ## Check playbooks syntax
	ansible-playbook playbooks/trivial.yml --syntax-check