import json
import os
from tomark import Tomark

def export_json(datas: dict, outfile: str) -> int:
    try:
        os.makedirs(os.path.dirname(outfile), exist_ok=True)

        with open(outfile, "w", encoding="utf-8") as f:
            json.dump(datas, f, indent=4, ensure_ascii=False)

        return (0,"OK")

    except Exception as e:
        print("Export error:", e)
        return (1,e)

def export_md(datas: dict, outfile: str, level: int = 1):
    try:
        os.makedirs(os.path.dirname(outfile), exist_ok=True)

        if level == 1:
            with open(outfile, "w", encoding="utf-8") as f:
                f.write("# IntegrityCheck MD Report\n\n")

        for key, val in datas.items():
            if isinstance(val, dict):
                level
                hashtags = "#"+"#" * level
                with open(outfile, "a", encoding="utf-8") as f:
                    f.write(f"{hashtags} {key}\n\n")

                ret = export_md(val, outfile, level+1)
                if ret[0] != 0:
                    return (1,"Unexpected error")

            else:
                if isinstance(val, list) and len(val) > 0 and isinstance(val[0], dict):
                    markdown = Tomark.table(val) + "\n"
                else:
                    markdown = f"**{key}**: {val}\n\n"

                with open(outfile, "a", encoding="utf-8") as f:
                    f.write(markdown)

        return (0,"OK")

    except Exception as e:
        print("Erreur export_md :", e)
        return (1,e)
