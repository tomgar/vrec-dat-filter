# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=[],
             binaries=[],
             datas=[('PATH_TO_ENV/Lib/site-packages/scrapy', 'scrapy')],
             hiddenimports=[
                'email.mime.multipart',
                'email.mime.text',
                'twisted.web.client',
                'queuelib'
             ],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          name='vrec',
          debug=False,
          strip=False,
          upx=True,
          console=True )
