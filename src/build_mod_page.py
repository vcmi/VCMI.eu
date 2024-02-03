import os
import base64
from io import BytesIO
from mdutils.mdutils import MdUtils
from mdutils.tools import Html

from parse_mod import ModParser

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

    mdMod.new_header(level=2, title="Submods")
    m = ModParser(mod_repo["download"])
    for item in m.get_mods():
        mdMod.new_header(level=3, title=item["data"]["name"])
        if "creatures" in item["config"]:
            mdModTable = ["Name", "Level", "Speed", "Image"]
            for k, v in item["config"]["creatures"].items():
                if not k.lower().startswith("core:") and "name" in item["config"]["creatures"][k]:
                    image = ""
                    if "iconLarge" in item["config"]["creatures"][k]["graphics"]:
                        buffered = BytesIO()
                        m.get_image(item, item["config"]["creatures"][k]["graphics"]["iconLarge"]).save(buffered, format="PNG")
                        img_str = "data:image/png;base64," + base64.b64encode(buffered.getvalue()).decode()
                        image = Html.image(path=img_str, size='50')
                    mdModTable.extend([
                        item["config"]["creatures"][k]["name"]["singular"],
                        item["config"]["creatures"][k]["level"] if "level" in item["config"]["creatures"][k] else "",
                        item["config"]["creatures"][k]["speed"],
                        image
                    ])
            if(len(mdModTable) > 4):
                mdMod.new_header(level=4, title="Creatures")
                mdMod.new_table(columns=4, rows=int(len(mdModTable)/4), text=mdModTable, text_align='center')
    mdMod.create_md_file()