import json
import os
from tomark import Tomark
from constantes import css_theme

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

def export_html(datas: dict, outfile: str, level: int = 1):
    try:
        os.makedirs(os.path.dirname(outfile), exist_ok=True)

        if level == 1:
            with open(outfile, "w", encoding="utf-8") as f:
                f.write(f"<!DOCTYPE html><html><head><title>IntegrityCheck HTML Report</title><style>{css_theme}</style></head><body>")
                f.write("<h1>IntegrityCheck HTML Report</h1>\n")

        for key, val in datas.items():
            if isinstance(val, dict):
                headerlevel = f"h{min(level+1,6)}"
                with open(outfile, "a", encoding="utf-8") as f:
                    f.write(f"<{headerlevel}>{key}</{headerlevel}>\n")

                ret = export_html(val, outfile, level+1)
                if ret[0] != 0:
                    return (1, "Unexpected error")

            else:
                if isinstance(val, list) and len(val) > 0 and isinstance(val[0], dict):
                    html = "<table border='1'><tr>"
                    for col in val[0].keys():
                        html += f"<th>{col}</th>"
                    html += "</tr>"

                    for row in val:
                        html += "<tr>"
                        for col in row.values():
                            html += f"<td>{col}</td>"
                        html += "</tr>"
                    html += "</table>\n"
                else:
                    html = f"<p><strong>{key}:</strong> {val}</p>\n"

                with open(outfile, "a", encoding="utf-8") as f:
                    f.write(html)

        if level == 1:
            with open(outfile, "a", encoding="utf-8") as f:
                f.write("<footer>IntegrityCheck</footer></body></html>")

        return (0, "OK")

    except Exception as e:
        print("Erreur export_html :", e)
        return (1, e)
