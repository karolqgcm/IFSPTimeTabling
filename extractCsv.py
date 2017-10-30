import pandas as pd
import numpy as np

data = pd.read_csv("original.csv", usecols=[0,4,6])

data.to_csv("codProf_apelido_regime.csv", index=False)

