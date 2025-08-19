# build.spec - PyInstaller build for ansible-core
# Run with: pyinstaller build.spec

import os
from PyInstaller.utils.hooks import collect_submodules, collect_data_files

# Collect ansible and ansible_test packages + data
hiddenimports = collect_submodules("ansible") + collect_submodules("ansible_test")
datas = collect_data_files("ansible", include_py_files=True)
datas += collect_data_files("ansible_test", include_py_files=True)

# Define entry points as executables
cli_scripts = {
    "ansible": "ansible.cli.adhoc:main",
    "ansible-config": "ansible.cli.config:main",
    "ansible-console": "ansible.cli.console:main",
    "ansible-doc": "ansible.cli.doc:main",
    "ansible-galaxy": "ansible.cli.galaxy:main",
    "ansible-inventory": "ansible.cli.inventory:main",
    "ansible-playbook": "ansible.cli.playbook:main",
    "ansible-pull": "ansible.cli.pull:main",
    "ansible-vault": "ansible.cli.vault:main",
    "ansible-test": "ansible_test._util.target.cli.ansible_test_cli_stub:main",
}

a = []
for exe_name, entry in cli_scripts.items():
    module, func = entry.split(":")
    a.append(
        Analysis(
            [f"-m{module}"],
            pathex=[os.getcwd()],
            binaries=[],
            datas=datas,
            hiddenimports=hiddenimports,
            hookspath=[],
            runtime_hooks=[],
            excludes=[],
            noarchive=False,
        )
    )

executables = []
for i, (exe_name, entry) in enumerate(cli_scripts.items()):
    module, func = entry.split(":")
    pyz = PYZ(a[i].pure, a[i].zipped_data, cipher=None)
    exe = EXE(
        pyz,
        a[i].scripts,
        a[i].binaries,
        a[i].zipfiles,
        a[i].datas,
        [],
        name=exe_name,
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=True,
    )
    executables.append(exe)

coll = COLLECT(
    *executables,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="ansible-bundle",
)
