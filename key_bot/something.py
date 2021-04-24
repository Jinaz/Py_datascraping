import pandas as pd
from matplotlib import pyplot as plt

df = pd.read_csv("dataset.csv")
print(df.to_string())

countryranked = {it["Rank"]:[it["Country"],it["Score"]] for it in df}

print(countryranked)
plt.plot([ct["Rank"] for ct in df], [ct["Score"] for ct in df])
plt.show()