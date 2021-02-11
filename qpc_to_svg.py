import json
import re
import subprocess

exec = lambda cmd: subprocess.run(cmd, shell=True, capture_output=True, encoding='utf-8').stdout
def apply_repls(text, repls):
    for r in repls:
        text = re.sub(r[1], r[2], text) if r[0] else text.replace(r[1], r[2])
    return text

symbol_repls = [
    (1, r'<!--[\s\S]*?-->', ''),
    (1, r"<svg width='(\d+)px' height='(\d+)px' xmlns='http://www.w3.org/2000/svg' version='1.1'>", r'<symbol id="%s" viewBox="0 0 \1 \2">'),
    (0, '</svg>', '</symbol>'),
    (1, r'\n\n+', '\n'),
    (1, ' +\n', '\n'),
]

pg_chars_old = [hex(64337 + i + (33 if i > 96 else 0)).upper() for i in range(0, 195)]
data = json.load(open('qpc-old.json'))

svg_tpl = '<svg xmlns="http://www.w3.org/2000/svg">\n%s\n\n\n<!-- Symbols --><defs>\n%s\n</defs></svg>\n'

def convert_page(pg_num):
    code_points = pg_chars_old[:int(data['stops'][pg_num - 1].split(',')[-1]) + 1]
    cmd = f'./example2 mushaf/QCF_P{pg_num:03}.TTF '
    symbols = [apply_repls(exec(cmd + symbol), symbol_repls).strip() % i for i, symbol in enumerate(code_points, 1)]
    open(f'pages/qpc-pg-{pg_num:03}.svg', 'w').write(svg_tpl % ('\n'.join(use), '\n'.join(symbols)))

for i in range(1, 605):
    convert_page(i)
