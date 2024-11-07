from collections import defaultdict

def main(text: str):
    d = defaultdict(list)
    for symbol in text:
        if symbol != ' ':
            d[symbol].append(symbol)
    return d

func = main('asdf sdf asd  sger ty')
for k, v in sorted(func.items()):
    print(f"'{k}': {v} x{v.count(v[0])}")