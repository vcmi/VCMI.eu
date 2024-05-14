import tempfile
import zipfile
import io
import os
import shutil
import re

def build_extract_main_repo(data):
    with tempfile.TemporaryDirectory() as tempdirname:
        with zipfile.ZipFile(io.BytesIO(data), "r") as z:
            z.extractall(tempdirname)

        shutil.move(os.path.join(tempdirname, 'vcmi-develop/docs'), 'docs')
        shutil.copytree('additional/docs', 'docs', dirs_exist_ok=True)

        os.makedirs("docs/assets", exist_ok=True)
        shutil.copy(os.path.join(tempdirname, 'vcmi-develop/client/icons/vcmiclient.svg'), 'docs/assets/logo.svg')
        shutil.copy(os.path.join(tempdirname, 'vcmi-develop/client/icons/vcmiclient.svg'), 'docs/assets/logo2.svg')
        shutil.copy(os.path.join(tempdirname, 'vcmi-develop/client/icons/vcmiclient.16x16.png'), 'docs/assets/favicon.png')

        shutil.copy(os.path.join(tempdirname, 'vcmi-develop/ChangeLog.md'), 'docs/ChangeLog.md')
        with open('docs/ChangeLog.md', "r") as file:
            tmp = file.read()
        tmp = re.sub(r"(# [\d])", r"#\1", tmp)
        with open('docs/ChangeLog.md', "w") as file:
            file.write("---\nhide:\n  - navigation\n---\n\n# Changelog\n" + tmp)

        shutil.copytree('static', 'docs', dirs_exist_ok=True)