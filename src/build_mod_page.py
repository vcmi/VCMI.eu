import os
from mdutils.mdutils import MdUtils
from mdutils.tools import Html

def build_mod_page(mod_repo, mod):
    os.makedirs("docs/Mod Repository/" + mod["modType"], exist_ok=True)
    mdMod = MdUtils(file_name='docs/Mod Repository/' + mod["modType"] + '/' + mod["name"])
    mdMod.new_header(level=1, title=mod["name"])
    mdMod.new_header(level=2, title="Description")
    mdMod.new_line(mod["description"])
    mdMod.new_header(level=2, title="Version")
    mdMod.new_line(mod["version"])
    if "screenshots" in mod_repo:
        mdMod.new_header(level=2, title="Screenshots")
        mdMod.write('<p>')
        for i, screenshot in enumerate(mod_repo["screenshots"]):
            mdMod.new_paragraph(Html.image(path=screenshot, size='100'))
        mdMod.write('</p>')
    mdMod.create_md_file()