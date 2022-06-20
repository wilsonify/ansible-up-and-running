# Chapter 8

Install python dependencies listen in the `requirements.txt` file:

```
python3 -mvenv py3
source py3/bin/activate
pip3 install --upgrade pip
pip3 install wheel
pip3 install -r playbooks/requirements.txt
cd playbooks
```

Just run the playbook.yml, the vault file is encrypted. The password is `password`
