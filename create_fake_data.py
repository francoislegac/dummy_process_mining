#600 patients numéroté de 1 à 600
#7 événements
#20 000 events
import numpy as np
import pandas as pd

np.random.seed(123)

events = [
    'Examen clinique',
    'biopsie',
    'Imagerie',
    'Diagnostic',
    'Scanner',
    'PET-scan',
    'Autre test'
    ]



dates = pd.date_range("2000-01-01", periods=31, freq='D') #.astype('category')
N = 20000

df = pd.DataFrame(
    dict(
        id = np.random.randint(1,601, N),
        event = np.random.randint(0,7, N),
        datetime = np.random.randint(0,31, N),
    )
)
df['event'] = df['event'].map(dict(zip(np.arange(0,7), events)))
df['datetime'] = df['datetime'].map(dict(zip(np.arange(0,31), dates)))
df['month'] = df['datetime'].dt.day

df.to_csv('fake_logs.csv')

