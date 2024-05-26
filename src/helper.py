import re
import json_repair

def get_value_if_exists(elem, val):
    return elem[val] if val in elem else ""

# https://stackoverflow.com/a/18381470 (Onur Yıldırım, CC BY-SA 4.0)
def remove_comments(string):
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    # first group captures quoted strings (double or single)
    # second group captures comments (//single-line or /* multi-line */)
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    def _replacer(match):
        # if the 2nd group (capturing comments) is not None,
        # it means we have captured a non-quoted (real) comment string.
        if match.group(2) is not None:
            return "" # so we will return empty to remove the comment
        else: # otherwise, we will return the 1st group
            return match.group(1) # captured quoted-string
    return regex.sub(_replacer, string)

def load_vcmi_json(string):
    tmp = remove_comments(string)
    return json_repair.loads(tmp)