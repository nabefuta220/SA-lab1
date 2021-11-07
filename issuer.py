import argparse
import os
import subprocess


def inputer():
    arg=argparse.ArgumentParser()
    arg.add_argument('command',nargs='*')
    parse=arg.parse_args()
    return parse.command


if __name__=='__main__':
    str=inputer()
    print(str)
    out_file=f"output/{os.path.splitext(os.path.basename(str[1]))[0]}.txt"
    print(out_file)
    command=['pipenv' ,'run']+str
    cp = subprocess.run(command, encoding='utf-8', stdout=subprocess.PIPE)

    with open(out_file, 'w') as f:
        f.write(f"${' '.join(command)}\n")
        f.write(cp.stdout)
        