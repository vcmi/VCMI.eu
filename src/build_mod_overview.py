import os
import urllib.request
from mdutils.mdutils import MdUtils
from mdutils.tools import Html
from mdutils.tools.Link import Inline
import re
import textwrap

from helper import load_vcmi_json

def build_mod_overview(mod_repo, cb):
    os.makedirs("docs/Mod Repository", exist_ok=True)
    mdModOverview = MdUtils(file_name='docs/Mod Repository/Overview', title='Overview')
    mdModOverviewTable = ["Mod", "Type", "Description", "Version", "Translations"]
    for key, value in mod_repo.items():
        mod = load_vcmi_json(urllib.request.urlopen(value["mod"].replace(" ", "%20")).read().decode())

        translations = [k for k, v in mod.items() if isinstance(v, dict) and "translations" in v]

        description = mod["description"].replace("<br>", "\n").replace("<br/>", "\n").replace("<br />", "\n").replace("<p", "\n<p")
        description = re.sub(r"<[^>]*>", "", description)
        w = textwrap.TextWrapper(width=300,break_long_words=False,replace_whitespace=False)
        description_short = w.wrap(description)
        if len(description) != len(description_short[0]):
            description = description_short[0] + " [...]"
        else:
            description = description_short[0]
        description = description.replace("\r\n", "<br/>").replace("\n", "<br/>").replace("|", "&#124;")

        mdModOverviewTable.extend([
            Inline.new_link('../' + mod["modType"] + '/' + mod["name"].replace("|", "&#124;"), text=mod["name"].replace("|", "&#124;")),
            mod["modType"],
            description,
            mod["version"],
            ", ".join(translations)
        ])

        cb(value, mod)
    mdModOverview.new_table(columns=5, rows=int(len(mdModOverviewTable)/5), text=mdModOverviewTable, text_align='center')
    mdModOverview.create_md_file()