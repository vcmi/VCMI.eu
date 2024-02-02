import os
import io
import json5
import tempfile
import zipfile
import urllib.request
from mdutils.mdutils import MdUtils
from mdutils.tools import Html

def get_creature_data(mod_repo):
    tmp = []
    mod_data = urllib.request.urlopen(mod_repo["download"]).read()
    with tempfile.TemporaryDirectory() as tempdirname:
        with zipfile.ZipFile(io.BytesIO(mod_data), "r") as z:
            z.extractall(tempdirname)
        for subdir, dirs, files in os.walk(tempdirname):
            for file in files:
                if file.lower().endswith(".json"):
                    jdata = json5.loads(open(os.path.join(subdir, file), "r").read())
                    if "creatures" in jdata:
                        for creature in jdata["creatures"]:
                            creature = creature.rstrip("/")
                            creature = creature if creature.endswith(".json") else creature + ".json"
                            jdata_creatures = json5.loads(open(os.path.join(subdir, [x for x in os.listdir(subdir) if x.lower() == "content"][0], creature), "r").read())
                            for key, jdata_creature in jdata_creatures.items():
                                tmp.append(jdata_creature)
    return tmp

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
    if(mod["modType"] in ["Creatures"]):
        tmp = get_creature_data(mod_repo)
        if len(tmp) > 0:
            mdMod.new_header(level=2, title="New Units")
            mdModTable = ["Name", "Level", "Speed", "Image"]
            for item in tmp:
                mdModTable.extend([item["name"]["singular"], item["level"], item["speed"], item["graphics"]["iconLarge"]])
            mdMod.new_table(columns=4, rows=int(len(mdModTable)/4), text=mdModTable, text_align='center')
            
    mdMod.create_md_file()