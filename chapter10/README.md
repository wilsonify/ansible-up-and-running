# Chapter 8

Install python dependencies listed in the `requirements.txt` fil into a Python 3 virtualenv.

```
python3 -mvenv py3
source py3/bin/activate
pip3 install --upgrade pip
pip3 install wheel
pip3 install -r playbooks/requirements.txt
cd playbooks
```

Then just run the playbook.yml, the vault file is encrypted. The password is `password`
