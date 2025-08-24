# Ansible + Vagrant Integration

This project demonstrates how to integrate **Vagrant** with **Ansible** using a `Makefile` for automation.  
The setup is based on the `ansible-up-and-running` examples and extended to use a `Vagrantfile` with JSON-based
configuration.

---

## Prerequisites

Before running, make sure you have installed:

- [Vagrant](https://www.vagrantup.com/downloads) (>= 2.0.0)
- [VirtualBox](https://www.virtualbox.org/wiki/Downloads) (or another supported provider)
- [Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- Required Vagrant plugins:
  ```bash
  vagrant plugin install vagrant-hostmanager vagrant-vbguest
  ```

---

## File Structure

```
.
├── Vagrantfile
├── config.json
├── playbook.yml
├── roles/
│   └── requirements.yml
├── playbooks/
│   └── install-vagrant.yml
└── makefile
```

- **Vagrantfile** — defines VMs dynamically from `config.json` and provisions them with Ansible.
- **config.json** — defines VM attributes (name, box, IP, CPUs, RAM, etc).
- **playbook.yml** — the main Ansible playbook applied inside VMs.
- **roles/** — Ansible roles, installed via Galaxy (`requirements.yml`).
- **playbooks/install-vagrant.yml** — optional bootstrap playbook for local machine setup.
- **makefile** — automates common tasks.

---

## Example `config.json`

```json
{
  "servers": [
    {
      "name": "web1",
      "box": "bento/ubuntu-20.04",
      "ip": "192.168.56.10",
      "cpus": 2,
      "memory": 2048
    },
    {
      "name": "db1",
      "box": "bento/ubuntu-20.04",
      "ip": "192.168.56.11",
      "cpus": 1,
      "memory": 1024
    }
  ]
}
```

---

## Makefile Usage

```bash
make vagrant      # Runs the Vagrant install playbook
make up           # Starts and provisions VMs via Vagrant + Ansible
make halt         # Stops all Vagrant VMs
make destroy      # Destroys all Vagrant VMs
make clean        # Cleans up generated files and resets state
```

---

## Workflow

1. Edit `config.json` to define your VMs.
2. Run:
   ```bash
   make up
   ```
3. Access VMs:
   ```bash
   vagrant ssh web1
   vagrant ssh db1
   ```
4. Destroy when done:
   ```bash
   make destroy
   ```

---

## Notes

- Ensure your user can run Ansible with privilege escalation (passwordless `sudo` or `--ask-become-pass`).
- Adjust the `playbook.yml` to define roles and tasks for provisioning.
- Extend `roles/requirements.yml` for Galaxy role dependencies.