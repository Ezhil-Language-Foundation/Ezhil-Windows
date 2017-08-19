# -*- mode: python -*-

block_cipher = None


a = Analysis(['ezhili.py'],
             pathex=['c:\\Users\\muthu\\devel\\ezhil-windows\\cli'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ezhili',
          debug=False,
          strip=False,
          upx=True,
          console=True , icon='ezhil.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='ezhili')
