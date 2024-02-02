import os
import json
import urllib.request
from mdutils.mdutils import MdUtils
from mdutils.tools import Html

def build_mod_overview(mod_repo, cb):
    os.makedirs("docs/Mod Repository", exist_ok=True)
    mdModOverview = MdUtils(file_name='docs/Mod Repository/Overview', title='Overview')
    mdModOverviewTable = ["Mod", "Description", "Version", "Language"]
    for key, value in mod_repo.items():
        mod = json.loads(urllib.request.urlopen(value["mod"].replace(" ", "%20")).read())

        mdModOverviewTable.extend([mod["name"].replace("|", "&#124;"), mod["description"].replace("\n", "<br/>").replace("|", "&#124;"), mod["version"], "test"])

        cb(value, mod)
    mdModOverview.new_table(columns=4, rows=int(len(mdModOverviewTable)/4), text=mdModOverviewTable, text_align='center')
    mdModOverview.create_md_file()