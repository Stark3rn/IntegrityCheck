import os
import yara

def scan_file_with_yara(file_path: str, rules_dir: str = "./rules") -> dict:
    matches_dict = {}
    for root, _, files in os.walk(rules_dir):
        for rule_file in files:
            if rule_file.endswith((".yar", ".yara")):
                rule_path = os.path.join(root, rule_file)
                try:
                    rules = yara.compile(filepath=rule_path)
                    matches = rules.match(file_path)
                    if matches:
                        matches_dict[rule_path] = [m.rule for m in matches]
                except yara.SyntaxError as e:
                    print(f"Syntax error in rule {rule_path}: {e}")
                except Exception as e:
                    print(f"Error scanning with {rule_path}: {e}")

    return matches_dict