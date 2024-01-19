import yaml

from pathlib import Path
from yaml.loader import SafeLoader
from metaskills import metaskills

def gen_pos_vars(position):
    return f'\\newcommand\\jobpos{{{position}}}\n'

def load_yaml(file):
    with open(file, 'r') as f:
        data = yaml.load(f, Loader=SafeLoader)
    return data


def save_tex(tex, file):
    with open(file, 'w') as fh:
        fh.write(tex)


profiles = load_yaml('data/profiles.yml')

req_keys = {'meta'}
for profile in profiles.keys():
    print(f'Working on profile {profile}')

    if not all(x in profiles[profile] for x in req_keys):
        print(f'Skipping {profile} due to missing keys: {req_keys - set(profiles[profile].keys())}')
        continue

    fin = f'data/meta/{profiles[profile]["meta"]}'

    # metaskills
    fout = Path('generated/meta/') / f'{Path(fin).stem}.tex'
    fout.parent.mkdir(exist_ok=True, parents=True)

    tex = metaskills(load_yaml(fin))
    print(f'Writing to {fout}')
    save_tex(tex, fout)
    
    # position vars
    fout = Path('generated/vars/') / f'{Path(fin).stem}.tex'
    fout.parent.mkdir(exist_ok=True, parents=True)
    tex = gen_pos_vars(Path(fin).stem)
    
    print(f'Writing to {fout}')
    save_tex(tex, fout)
    
    print()



