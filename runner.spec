# -*- mode: python ; coding: utf-8 -*-
import sys
import os.path as osp
sys.setrecursionlimit(5000)
 
block_cipher = None
 
 




a = Analysis(['runner.py',
'global_environment.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_00_dmp_product.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_03_function_model.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_04_category.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_05_dmp_device.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_06_device_shadow.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_07_group.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_08_label.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_09_check_statistic.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_10_data_check.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_11_data_parse.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_12_router_destination.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_13_router.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_15_rules.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_16_mail_config.py',
'E:\\work_code\\openapi\\openapi_python\\case\\dmp\\test_17_delete.py',
'E:\\work_code\\openapi\\openapi_python\\assist\\get_color.py',
'E:\\work_code\\openapi\\openapi_python\\assist\\getSignature.py'
],
             pathex=['E:\\work_code\\openapi\\openapi_python'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='runner',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='runner')
