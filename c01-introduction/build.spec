# build.spec - PyInstaller build for ansible-core with --collect-all
# Run with: pyinstaller build.spec

import os
from pathlib import Path
from PyInstaller.utils.hooks import collect_all

# Collect everything for ansible and ansible_test
datas, binaries, hiddenimports = ([], [], [])
for pkg in ["ansible", "ansible_test"]:
    d, b, h = collect_all(pkg)
    datas += d
    binaries += b
    hiddenimports += h

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

executables = []

# Generate stubs so PyInstaller knows the entry point
stub_dir = Path("pyi_stubs")
stub_dir.mkdir(exist_ok=True)

for exe_name, entry in cli_scripts.items():
    module, func = entry.split(":")
    stub_path = stub_dir / f"{exe_name}_stub.py"
    stub_path.write_text(
        f"import sys\nfrom {module} import {func} as _main\n"
        f"if __name__ == '__main__':\n"
        f"    sys.exit(_main())\n"
    )

    a = Analysis(
        [str(stub_path)],
        pathex=[os.getcwd()],
        binaries=binaries,
        datas=datas,
        hiddenimports=hiddenimports,
        hookspath=[],
        runtime_hooks=[],
        excludes=[],
        noarchive=False,
    )

    pyz = PYZ(a.pure, a.zipped_data, cipher=None)
    exe = EXE(
        pyz,
        a.scripts,
        a.binaries,
        a.zipfiles,
        a.datas,
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
