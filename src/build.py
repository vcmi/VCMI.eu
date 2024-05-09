import json5
import urllib.request
import shutil
from mdutils.mdutils import MdUtils
import logging
import sys

from build_extract_main_repo import build_extract_main_repo
from build_mod_overview import build_mod_overview
from build_mod_page import build_mod_page

logging.basicConfig(
    level=logging.DEBUG, 
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler(stream=sys.stdout)]
)
log = logging.getLogger('VCMI')
log.info('started')

shutil.rmtree("docs", ignore_errors=True)

vcmi_url = "https://github.com/vcmi/vcmi/archive/refs/heads/develop.zip"
settings_schema = json5.loads(urllib.request.urlopen("https://raw.githubusercontent.com/vcmi/vcmi/develop/config/schemas/settings.json").read())
vcmi_mod_url = settings_schema["properties"]["launcher"]["properties"]["defaultRepositoryURL"]["default"]
#vcmi_mod_url = "https://pastebin.com/raw/MUYS7dbJ" #test

log.info('Download mod repo')
repo = urllib.request.urlopen(vcmi_url).read()
repo_mod = json5.loads(urllib.request.urlopen(vcmi_mod_url).read())

log.info('Create main page')
build_extract_main_repo(repo)
log.info('Create mod pages')
build_mod_overview(repo_mod, cb=build_mod_page)
log.info('finished')

#mkdocs serve