import tempfile
import zipfile
import io
import shutil
import os
import json
import urllib.request
from mdutils.mdutils import MdUtils
from mdutils.tools import Html

vcmi_url = "https://github.com/vcmi/vcmi/archive/refs/heads/develop.zip"
vcmi_mod_url = "https://raw.githubusercontent.com/vcmi/vcmi-mods-repository/develop/vcmi-1.4.json"

shutil.rmtree("docs", ignore_errors=True)

with tempfile.TemporaryDirectory() as tempdirname:
    response = urllib.request.urlopen(vcmi_url)
    data = response.read()
    with zipfile.ZipFile(io.BytesIO(data), "r") as z:
        z.extractall(tempdirname)

    shutil.move(os.path.join(tempdirname, 'vcmi-develop/docs'), 'docs')
    shutil.copytree('additional/docs', 'docs', dirs_exist_ok=True)

    # TODO replace all Readme.md in to index in all files from repo

    os.makedirs("docs/assets", exist_ok=True)
    shutil.copy(os.path.join(tempdirname, 'vcmi-develop/client/icons/vcmiclient.svg'), 'docs/assets/logo.svg')
    shutil.copy(os.path.join(tempdirname, 'vcmi-develop/client/icons/vcmiclient.16x16.png'), 'docs/assets/favicon.png')

    repo = json.loads(urllib.request.urlopen(vcmi_mod_url).read())
    os.makedirs("docs/Mod Repository", exist_ok=True)
    mdModOverview = MdUtils(file_name='docs/Mod Repository/Overview', title='Overview')
    mdModOverviewTable = ["Mod", "Description", "Version", "Language"]
    for key, value in repo.items():
        mod = json.loads(urllib.request.urlopen(value["mod"].replace(" ", "%20")).read())

        #mdModOverview.new_header(level=1, title=key)
        #mdModOverview.new_line('Link: ' + mdModOverview.new_inline_link(link='../' + mod["modType"] + '/' + mod["name"], text=mod["name"]))
        mdModOverviewTable.extend([mod["name"].replace("|", "&#124;"), mod["description"].replace("\n", "<br/>").replace("|", "&#124;"), mod["version"], "test"])

        os.makedirs("docs/Mod Repository/" + mod["modType"], exist_ok=True)
        mdMod = MdUtils(file_name='docs/Mod Repository/' + mod["modType"] + '/' + mod["name"])
        mdMod.new_header(level=1, title=mod["name"])
        mdMod.new_header(level=2, title="Description")
        mdMod.new_line(mod["description"])
        mdMod.new_header(level=2, title="Version")
        mdMod.new_line(mod["version"])
        if "screenshots" in value:
            mdMod.new_header(level=2, title="Screenshots")
            for i, screenshot in enumerate(value["screenshots"]):
                #mdMod.new_line(mdMod.new_inline_image(text='screenshot-' + str(i).zfill(3), path=screenshot))
                #mdMod.new_paragraph(mdModOverview.new_inline_link(link=screenshot, text=Html.image(path=screenshot, size='200')))
                mdMod.new_paragraph(Html.image(path=screenshot, size='200'))
        mdMod.create_md_file()
    mdModOverview.new_table(columns=4, rows=int(len(mdModOverviewTable)/4), text=mdModOverviewTable, text_align='center')
    mdModOverview.create_md_file()

#mkdocs serve