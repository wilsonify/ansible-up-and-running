# type 'make' for help with this Makefile

.PHONY: help
help:
	@echo "'make clean' to destroy virtual machines"
	@echo "'make check' to validate content"
	@echo "'make update' vagrant box update"
	@echo "'make provision' to run playbook"
	@echo "'make test' validate result"


secrets.yml:
	@echo 'copy secrets.yml.example to secrets.yml and change the values'
	@exit 1

.PHONY: check
check: secrets.yml
	ansible-inventory --graph -i inventory
	ansible-playbook --syntax-check mezzanine-across-hosts.yml
	ansible-lint mezzanine-across-hosts.yml
	vagrant validate
	git ls-files *.yml | xargs yamllint

update:
	vagrant box update

noprovision:
	vagrant up --no-provision

provision: noprovision check
	vagrant up

.PHONY: clean
clean:
	vagrant destroy -f
	@rm -rf .vagrant/

.PHONY: test
test:
	@echo 'make test should display this line twice:'
	@echo '<h2>Congratulations!</h2>'
	@curl -s -k https://www.192.168.33.10.nip.io/ | grep h2

all: clean update provision test
