import os

from mdutils.mdutils import MdUtils
from mdutils.tools import Html
from PIL import Image
import logging
log = logging.getLogger('LOGGER_NAME')

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
        create_creature_table(mdMod, item, m)
        create_puzzle_map(mdMod, item, m)
    mdMod.create_md_file()

def create_creature_table(md, mod, modparser):
    log.info('create creature table for ' + mod["data"]["name"])
    if "creatures" in mod["config"]:
        mdModTable = ["Name", "Level", "Speed", "Image"]
        for k, v in mod["config"]["creatures"].items():
            if not k.lower().startswith("core:") and "name" in mod["config"]["creatures"][k]:
                image = ""
                if "iconLarge" in mod["config"]["creatures"][k]["graphics"]:
                    image = Html.image(path=modparser.get_image_base64(mod, mod["config"]["creatures"][k]["graphics"]["iconLarge"]), size='50')
                mdModTable.extend([
                    mod["config"]["creatures"][k]["name"]["singular"],
                    mod["config"]["creatures"][k]["level"] if "level" in mod["config"]["creatures"][k] else "",
                    mod["config"]["creatures"][k]["speed"],
                    image
                ])
        if(len(mdModTable) > 4):
            md.new_header(level=4, title="Creatures")
            md.new_table(columns=4, rows=int(len(mdModTable)/4), text=mdModTable, text_align='center')

def create_puzzle_map(md, mod, modparser):
    log.info('create puzzle map for ' + mod["data"]["name"])
    if "factions" in mod["config"]:
        for k, v in mod["config"]["factions"].items():
            md.new_header(level=4, title="Puzzlemap")
            if "puzzleMap" in mod["config"]["factions"][k]:
                img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
                prefix = mod["config"]["factions"][k]["puzzleMap"]["prefix"]
                for i, item in enumerate(mod["config"]["factions"][k]["puzzleMap"]["pieces"]):
                    tmp_img = modparser.get_image(mod, prefix + str(i).zfill(2))
                    if tmp_img != None:
                        img.paste(tmp_img, (item["x"], item["y"]), tmp_img)
                img = img.crop(img.getbbox())
                md.new_paragraph(Html.image(path=modparser.image_convert_to_base64_html(img), size='300'))
