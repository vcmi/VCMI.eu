import os
import json5
import urllib.request
from mdutils.mdutils import MdUtils
from mdutils.tools import Html
from mdutils.tools.Link import Inline

def build_mod_overview(mod_repo, cb):
    os.makedirs("docs/Mod Repository", exist_ok=True)
    mdModOverview = MdUtils(file_name='docs/Mod Repository/Overview', title='Overview')
    mdModOverviewTable = ["Mod", "Type", "Description", "Version", "Translations"]
    for key, value in mod_repo.items():
        mod = json5.loads(urllib.request.urlopen(value["mod"].replace(" ", "%20")).read())

        translations = [k for k, v in mod.items() if isinstance(v, dict) and "translations" in v]

        mdModOverviewTable.extend([
            Inline.new_link('../' + mod["modType"] + '/' + mod["name"].replace("|", "&#124;"), text=mod["name"].replace("|", "&#124;")),
            mod["modType"],
            mod["description"].replace("\r\n", "<br/>").replace("\n", "<br/>").replace("|", "&#124;"),
            mod["version"],
            ", ".join(translations)
        ])

        cb(value, mod)
    mdModOverview.new_table(columns=5, rows=int(len(mdModOverviewTable)/5), text=mdModOverviewTable, text_align='center')
    mdModOverview.create_md_file()