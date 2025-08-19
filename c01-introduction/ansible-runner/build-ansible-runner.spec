# build-ansible-runner.spec
# Usage: pyinstaller build-ansible-runner.spec
#
# Produces: dist/ansible-runner/ansible-runner  (or .exe on Windows)

import os
from pathlib import Path
from PyInstaller.utils.hooks import collect_all

# 1) Collect everything from ansible_runner (modules + package data)
datas, binaries, hiddenimports = ([], [], [])
d, b, h = collect_all("ansible_runner")
datas += d
binaries += b
hiddenimports += h

# 2) Generate a small, robust entry-point stub
#    ansible-runner has historically used __main__.main; keep a fallback.
stub_dir = Path("pyi_stubs")
stub_dir.mkdir(exist_ok=True)
stub_path = stub_dir / "ansible_runner_stub.py"
stub_path.write_text(
    "import sys\n"
    "try:\n"
    "    from ansible_runner.__main__ import main\n"
    "except Exception:\n"
    "    # Fallback for older layouts\n"
    "    from ansible_runner.interface import main\n"
    "if __name__ == '__main__':\n"
    "    sys.exit(main())\n"
)

# 3) Standard PyInstaller pipeline
a = Analysis(
    [str(stub_path)],
    pathex=[os.getcwd()],
    binaries=binaries,
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=[],         # add custom hooks here if you create any
    runtime_hooks=[],
    excludes=[],          # add excludes if you need to slim the build
    noarchive=False,      # keep archive for smaller dist; set True to unpack
)

pyz = PYZ(a.pure, a.zipped_data, cipher=None)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name="ansible-runner",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,             # UPX is fine; PyInstaller disables on some linux automatically
    console=True,         # CLI tool -> console
)

coll = COLLECT(
    exe,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="ansible-runner",
)
