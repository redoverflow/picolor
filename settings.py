#settings (most likely dark mode only)

import simplejson as json

def getsettings():
    return json.loads(open("settings.json").read())

def setsettings(darkmode = 1):
    with open("settings.json", "r+") as f:
        parsed = json.load(f)
        f.seek(0)
        parsed["darkmode"] = darkmode
        f.write(json.dumps(parsed))
        f.truncate()

if __name__=="__main__":
    setsettings(1)