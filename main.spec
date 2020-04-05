# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['app\\main.py'],
             pathex=['D:\\ITR\\Projects\\Python\\Temporary\\learn-words'],
             binaries=[],
             datas=[('./app/store/logo.ico', 'store'), ('./VLC/libvlc.dll', '.'), ('./VLC/axvlc.dll', '.'), ('./VLC/libvlccore.dll', '.'), ('./VLC/npvlc.dll', '.')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
a.datas += Tree('./VLC/plugins', prefix='plugins')
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False , icon='app\\store\\logo.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
