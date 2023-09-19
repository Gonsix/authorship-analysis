import pandas as pd

def load_data():
    with open("./data/Q_dataset.txt") as f:  # from project root
        Q_txt = f.read()
    with open("./data/K1_dataset.txt") as f:
        K1_txt = f.read()
    with open("./data/K2_dataset.txt") as f:
        K2_txt = f.read()

    df = pd.DataFrame([
        ["Q", Q_txt],  
        ["K1", K1_txt], 
        ["K2", K2_txt]
    ],
    columns=['author', 'message'],)
    return df

class DocID():
    Q = 0
    K1 = 1
    K2 = 2
    R = 3

