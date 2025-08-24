# Install Vagrant on the host (via Ansible playbook)
bootstrap:
	ansible-playbook playbooks/install-vagrant.yml --ask-become-pass

# Bring up all VMs defined in Vagrantfile/config.json
up:
	vagrant up

# Re-run Ansible provisioners inside VMs
provision:
	vagrant provision

# Check VM status
status:
	vagrant status

# SSH into a VM: make ssh VM=bionic
ssh:
	vagrant ssh $(VM)

# Reload VM configs (useful after changing Vagrantfile)
reload:
	vagrant reload

# Halt all VMs
halt:
	vagrant halt

# Destroy all VMs (CAREFUL!)
destroy:
	vagrant destroy -f

# Install required Ansible Galaxy roles
roles:
	ansible-galaxy install -r playbooks/requirements.yml -p playbooks/roles
