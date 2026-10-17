# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('Background.png', '.'), ('PlayerFrame1.png', '.'), ('PlayerFrame2.png', '.'), ('ClockFrame1.png', '.'), ('ClockFrame2.png', '.'), ('Kitty1.png', '.'), ('Kitty2.png', '.'), ('Kitty3.png', '.'), ('Doggy1.png', '.'), ('Doggy2.png', '.'), ('Doggy3.png', '.'), ('LifeCardFrame1.png', '.'), ('LifeCardFrame2.png', '.'), ('Trollface.png', '.'), ('meow.mp3', '.'), ('bark.mp3', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
