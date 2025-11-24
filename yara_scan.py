import os
import yara

def scan_file_with_yara(file_path: str, rules_dir: str = "./rules") -> dict:
    matches_dict = {}

    for rule_file in os.listdir(rules_dir):
        if rule_file.endswith((".yar", ".yara")):
            rule_path = os.path.join(rules_dir, rule_file)
            try:
                rules = yara.compile(filepath=rule_path)
                matches = rules.match(file_path)
                if matches:
                    matches_dict[rule_file] = [m.rule for m in matches]
            except yara.SyntaxError as e:
                print(f"Erreur syntaxe dans la règle {rule_file}: {e}")
            except Exception as e:
                print(f"Erreur lors du scan avec {rule_file}: {e}")

    return matches_dict