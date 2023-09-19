import sys
import os
import glob
import pandas as pd

def load_reference(name="Brown"):
    data = ""
    path = f"./data/references/{name}"
    if not os.path.exists(path):
        print(f'Error in load_reference(): Cannot find out data/reference/{name} file or directory  ' , file=sys.stderr)
        sys.exit(1)

    if os.path.isdir(path):
        print("AHJAJAA")
        files = glob.glob(f'{path}/*')
        for file in files:
            f = open(file, 'r')
            data = f.read() + ' ' + data
            f.close()
            break
    elif os.path.isfile(path):
        f = open(path, 'r')
        data = f.read()
        f.close()

    df_ref = pd.DataFrame({"author":["R"],
                            "message": [data]})
    return df_ref
