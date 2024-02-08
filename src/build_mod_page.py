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
        create_town_screen(mdMod, item, m)
        create_puzzle_map(mdMod, item, m)
        create_spell_table(mdMod, item, m)
        create_artifact_table(mdMod, item, m)
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

def create_spell_table(md, mod, modparser):
    log.info('create spell table for ' + mod["data"]["name"])
    if "spells" in mod["config"]:
        mdModTable = ["Name", "Description", "Schools", "Image"]
        for k, v in mod["config"]["spells"].items():
            if not k.lower().startswith("core:") and "name" in mod["config"]["spells"][k]:
                try: description = mod["config"]["spells"][k]["levels"]["none"]["description"]
                except:
                    try: description = mod["config"]["spells"][k]["levels"]["basic"]["description"]
                    except: description = ""
                if "graphics" in mod["config"]["spells"][k] and "iconBook" in mod["config"]["spells"][k]["graphics"]:
                    image = Html.image(path=modparser.get_image_base64(mod, mod["config"]["spells"][k]["graphics"]["iconBook"]), size='50')
                    mdModTable.extend([
                        mod["config"]["spells"][k]["name"].replace("\r\n", "<br/>").replace("\n", "<br/>").replace("|", "&#124;"),
                        description.replace("\r\n", "<br/>").replace("\n", "<br/>").replace("|", "&#124;"),
                        ", ".join([k for k, v in mod["config"]["spells"][k]["school"].items() if v == True]),
                        image
                    ])
        if(len(mdModTable) > 4):
            md.new_header(level=4, title="Spells")
            md.new_table(columns=4, rows=int(len(mdModTable)/4), text=mdModTable, text_align='center')

def create_artifact_table(md, mod, modparser):
    log.info('create artifact table for ' + mod["data"]["name"])
    if "artifacts" in mod["config"]:
        mdModTable = ["Name", "Description", "Slot", "Image"]
        for k, v in mod["config"]["artifacts"].items():
            if not k.lower().startswith("core:") and "text" in mod["config"]["artifacts"][k]:
                if "graphics" in mod["config"]["artifacts"][k] and "image" in mod["config"]["artifacts"][k]["graphics"]:
                    image = Html.image(path=modparser.get_image_base64(mod, mod["config"]["artifacts"][k]["graphics"]["image"]), size='50')
                    mdModTable.extend([
                        mod["config"]["artifacts"][k]["text"]["name"].replace("\r\n", "<br/>").replace("\n", "<br/>").replace("|", "&#124;"),
                        mod["config"]["artifacts"][k]["text"]["description"].replace("\r\n", "<br/>").replace("\n", "<br/>").replace("|", "&#124;"),
                        mod["config"]["artifacts"][k]["slot"].lower(),
                        image
                    ])
        if(len(mdModTable) > 4):
            md.new_header(level=4, title="Artifacts")
            md.new_table(columns=4, rows=int(len(mdModTable)/4), text=mdModTable, text_align='center')

def create_town_screen(md, mod, modparser):
    log.info('create town screen for ' + mod["data"]["name"])
    if "factions" in mod["config"]:
        for k, v in mod["config"]["factions"].items():
            if not k.lower().startswith("core:") and "town" in mod["config"]["factions"][k] and "structures" in mod["config"]["factions"][k]["town"] and "townBackground" in mod["config"]["factions"][k]["town"]:
                md.new_header(level=4, title="Townscreen")
                img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
                tmp_img = modparser.get_image(mod, mod["config"]["factions"][k]["town"]["townBackground"])
                img.paste(tmp_img, (0, 0), tmp_img)
                for k2, v2 in mod["config"]["factions"][k]["town"]["structures"].items():
                    extract = modparser.get_animations(mod, v2["animation"])
                    if extract != None:
                        tmp_img = extract['sequences'][0]['frames'][0]
                        img.paste(tmp_img, (v2["x"], v2["y"]), tmp_img)
                img = img.crop(img.getbbox())
                md.new_paragraph(Html.image(path=modparser.image_convert_to_base64_html(img), size='300'))

def create_puzzle_map(md, mod, modparser):
    log.info('create puzzle map for ' + mod["data"]["name"])
    if "factions" in mod["config"]:
        for k, v in mod["config"]["factions"].items():
            if "puzzleMap" in mod["config"]["factions"][k]:
                md.new_header(level=4, title="Puzzlemap")
                img = Image.new('RGBA', (1000, 1000), (0, 0, 0, 0))
                prefix = mod["config"]["factions"][k]["puzzleMap"]["prefix"]
                for i, item in enumerate(mod["config"]["factions"][k]["puzzleMap"]["pieces"]):
                    tmp_img = modparser.get_image(mod, prefix + str(i).zfill(2))
                    if tmp_img != None:
                        img.paste(tmp_img, (item["x"], item["y"]), tmp_img)
                img = img.crop(img.getbbox())
                md.new_paragraph(Html.image(path=modparser.image_convert_to_base64_html(img), size='300'))
