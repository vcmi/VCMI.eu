import json
import urllib.request
import shutil
from mdutils.mdutils import MdUtils

from build_extract_main_repo import build_extract_main_repo
from build_mod_overview import build_mod_overview
from build_mod_page import build_mod_page

shutil.rmtree("docs", ignore_errors=True)

vcmi_url = "https://github.com/vcmi/vcmi/archive/refs/heads/develop.zip"
vcmi_mod_url = "https://raw.githubusercontent.com/vcmi/vcmi-mods-repository/develop/vcmi-1.4.json"
#vcmi_mod_url = "https://pastebin.com/raw/4TePvU6F" #test
repo = urllib.request.urlopen(vcmi_url).read()
repo_mod = json.loads(urllib.request.urlopen(vcmi_mod_url).read())

build_extract_main_repo(repo)
build_mod_overview(repo_mod, cb=build_mod_page)

#mkdocs serve