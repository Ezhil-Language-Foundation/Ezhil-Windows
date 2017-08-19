# -*- mode: python -*-

block_cipher = None


a = Analysis(['ezhuthi.py'],
             pathex=['c:\\Users\\muthu\\devel\\Ezhil-Windows\\'],
             binaries=[],
             datas=[('res/editor.glade', 'res'), ('res/helper.glade', 'res'), ('res/img/ezhil_square_2015_128px.png', 'res/img'), ('res/img/small-ezhil-splash-5.png', 'res/img')],
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
          name='ezhuthi',
          debug=False,
          strip=False,
          upx=True,
          console=False , icon='ezhil16.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='ezhuthi')
