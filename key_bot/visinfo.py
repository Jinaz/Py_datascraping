import pandas
from matplotlib import pyplot as plt

# using pandas as reader
df = pandas.read_csv("dataset.csv", sep=",")
print(df["Score"])

# countryranked = {it["Rank"]:[it["Country"],it["Score"]] for it in df}

# print(countryranked)
countries = df["Country"]
print(countries)
countries = [ct for ct in countries]

score = df["Score"]
score = [sc for sc in score]

gdp = df["GDP"]
support = df["Support"]
health = df["Health"]
freedom = df["Freedom"]
generosity = df["Generosity"]
corruption = df["Corruption"]

hdi = df["HDI"]
leab = df["Life expectancy at birth"]
eyos = df["Expected years of schooling"]
myos = df["Mean years of schooling"]
gnipc = df["Gross national income (GNI) per capita"]
hdi2018 = df["HDI rank 2018"]

gdp = [sc for sc in gdp]
support = [sc for sc in support]
health = [sc for sc in health]
freedom = [sc for sc in freedom]
generosity = [sc for sc in generosity]
corruption = [sc for sc in corruption]
hdi = [sc for sc in hdi]
leab = [sc for sc in leab]
eyos = [sc for sc in eyos]
myos = [sc for sc in myos]
gnipc = [sc for sc in gnipc]
hdi2018 = [sc for sc in hdi2018]

# top 50
plt.xticks(rotation=90)
plt.bar([countries[i] for i in range(int(len(countries)))], [score[i] for i in range(int(len(countries)))])
plt.show()


plt.xticks(rotation=90)
plt.bar([countries[i] for i in range(int(len(countries)/3))], [score[i] for i in range(int(len(countries)/3))])
plt.show()
plt.xticks(rotation=90)
line1 = plt.scatter([countries[i] for i in range(int(len(countries) / 3))],
                    [support[i] for i in range(int(len(countries) / 3))])

line2 = plt.scatter([countries[i] for i in range(int(len(countries) / 3))],
                    [health[i] for i in range(int(len(countries) / 3))])

line3 = plt.scatter([countries[i] for i in range(int(len(countries) / 3))],
                    [freedom[i] for i in range(int(len(countries) / 3))])

line4 = plt.scatter([countries[i] for i in range(int(len(countries) / 3))],
                    [generosity[i] for i in range(int(len(countries) / 3))])

line5 = plt.scatter([countries[i] for i in range(int(len(countries) / 3))],
                    [corruption[i] for i in range(int(len(countries) / 3))])

plt.legend((line1, line2, line3, line4, line5), ('Support', 'Health', 'Freedom', 'Generosity', 'Corruption'))
plt.show()

plt.xticks(rotation=90)
plt.bar([countries[i] for i in range(int(len(countries) / 3))],
        [hdi[i] - hdi2018[i] for i in range(int(len(countries) / 3))])
# plt.bar([countries[i] for i in range(int(len(countries)/3))], [ for i in range(int(len(countries)/3))])
plt.show()

plt.xticks(rotation=90)
line1 = plt.bar([countries[i] for i in range(int(len(countries) / 3))],
                [leab[i] for i in range(int(len(countries) / 3))])
line2 = plt.bar([countries[i] for i in range(int(len(countries) / 3))],
                [eyos[i] for i in range(int(len(countries) / 3))])
line3 = plt.bar([countries[i] for i in range(int(len(countries) / 3))],
                [myos[i] for i in range(int(len(countries) / 3))])

plt.legend((line1, line2, line3),
           ('Life expectancy at birth', 'Expected years of schooling', 'Mean years of schooling'))
plt.show()

plt.xticks(rotation=90)
plt.bar([countries[i] for i in range(int(len(countries) / 3))], [gdp[i] for i in range(int(len(countries) / 3))])
plt.show()
plt.xticks(rotation=90)
plt.bar([countries[i] for i in range(int(len(countries) / 3))], [gnipc[i] for i in range(int(len(countries) / 3))])
plt.show()

# bottom 50
plt.xticks(rotation=90)
line1 = plt.scatter([countries[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))],
                    [support[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))])

line2 = plt.scatter([countries[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))],
                    [health[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))])

line3 = plt.scatter([countries[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))],
                    [freedom[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))])

line4 = plt.scatter([countries[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))],
                    [generosity[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))])

line5 = plt.scatter([countries[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))],
                    [corruption[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))])

plt.legend((line1, line2, line3, line4, line5), ('Support', 'Health', 'Freedom', 'Generosity', 'Corruption'))
plt.show()

plt.xticks(rotation=90)
plt.bar([countries[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))],
        [hdi[i + int(len(countries) / 3)] - hdi2018[i + int(len(countries) / 3)] for i in
         range(int(len(countries) / 3))])
# plt.bar([countries[i] for i in range(int(len(countries)/3))], [ for i in range(int(len(countries)/3))])
plt.show()

plt.xticks(rotation=90)
line1 = plt.bar([countries[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))],
                [leab[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))])
line2 = plt.bar([countries[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))],
                [eyos[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))])
line3 = plt.bar([countries[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))],
                [myos[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))])

plt.legend((line1, line2, line3),
           ('Life expectancy at birth', 'Expected years of schooling', 'Mean years of schooling'))
plt.show()

plt.xticks(rotation=90)
plt.bar([countries[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))],
        [gdp[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))])
plt.show()
plt.xticks(rotation=90)
plt.bar([countries[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))],
        [gnipc[i + int(len(countries) / 3)] for i in range(int(len(countries) / 3))])
plt.show()

plt.xticks(rotation=90)
line1 = plt.bar([countries[i] for i in range(int(len(countries)))], [leab[i] for i in range(int(len(countries)))])
line2 = plt.bar([countries[i] for i in range(int(len(countries)))], [eyos[i] for i in range(int(len(countries)))])
line3 = plt.bar([countries[i] for i in range(int(len(countries)))],
                [myos[i] for i in range(int(len(countries)))])
plt.legend((line1, line2, line3),
           ('Life expectancy at birth', 'Expected years of schooling', 'Mean years of schooling'))
plt.show()
plt.xticks(rotation=90)
plt.bar([countries[i] for i in range(int(len(countries)))],
        [hdi[i] - hdi2018[i] for i in range(int(len(countries)))])
# plt.bar([countries[i] for i in range(int(len(countries)/3))], [ for i in range(int(len(countries)/3))])
plt.show()

# for ct in countries:
# print(ct)

# plt.plot([df[i] for i in range(len(df['Score']))], [float(ct["Score"][i]) for i in range(len(ct)) for ct in df])
# plt.show()
