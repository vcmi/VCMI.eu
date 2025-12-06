# patch_retry/plugin.py
from mkdocs.plugins import BasePlugin
import time
import material.plugins.privacy.plugin as privacy

_original_fetch = privacy.PrivacyPlugin._fetch

def _fetch_with_retry(self, file, config, retries=5, delay=10.0):
    attempt = 0
    while True:
        result = _original_fetch(self, file, config)
        if result:
            return True
        attempt += 1
        if attempt >= retries:
            print(f"[patch-retry] Giving up on {file}")
            return False
        print(f"[patch-retry] Fetch failed for {file} (attempt {attempt}), retrying in {delay}s…")
        time.sleep(delay)

privacy.PrivacyPlugin._fetch = _fetch_with_retry

class PatchRetryPlugin(BasePlugin):
    """Empty plugin — patch runs on import."""
    pass
