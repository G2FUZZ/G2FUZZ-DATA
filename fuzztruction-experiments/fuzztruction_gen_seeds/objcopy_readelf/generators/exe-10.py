import os

# Step 1: Generate a simple Python script
hello_world_script = """
def main():
    print("Hello, World!")

if __name__ == "__main__":
    main()
"""

# Save the Python script to ./tmp/hello_world.py
os.makedirs('./tmp', exist_ok=True)
with open('./tmp/hello_world.py', 'w') as file:
    file.write(hello_world_script)

# Step 2: Create a PyInstaller spec file with basic obfuscation settings
spec_content = """
# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['./tmp/hello_world.py'],
             pathex=['.'],
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
          name='hello_world',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
app = BUNDLE(exe,
             name='hello_world.app',
             icon=None,
             bundle_identifier=None)
"""

# Save the spec file to ./tmp/hello_world.spec
with open('./tmp/hello_world.spec', 'w') as file:
    file.write(spec_content)

# Step 3: Use PyInstaller to generate the executable
# Note: This step assumes that PyInstaller is installed and available in your environment
os.system('pyinstaller --onefile ./tmp/hello_world.spec --distpath ./tmp/ --workpath ./tmp/build/')

print("Executable has been generated and is located in the ./tmp/ directory.")