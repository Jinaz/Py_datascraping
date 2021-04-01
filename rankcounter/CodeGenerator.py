def codeGen():
    template_load = open("templates/template.txt", "r").read()
    template_save = open("templates/template_save.txt", "r").read()
    template_comp = open("templates/compare_template.txt", "r").read()
    # print(template)

    insertedstrings = ['Challenger', 'Grandmaster', 'Master']

    Tiergenerator = [("Dia{}_50", "Dia{}_0"), ("Plat{}_50", "Plat{}_0"), ("Gold{}_50", "Gold{}_0"),
                     ("Sil{}_50", "Sil{}_0"),
                     ("B{}_50", "B{}_0"), ("Iron{}_50", "Iron{}_0")]

    # sorted order up to down
    TierValues = []
    for tier in insertedstrings:
        TierValues.append(tier)
    for val in Tiergenerator:
        for i in range(1, 5):
            TierValues.append(val[0].format(i))
            TierValues.append(val[1].format(i))

    # print(TierValues)

    templatestrings_load = []
    tempaltestrings_save = []
    templatestrings_comparison = []

    index = 0
    for vals in TierValues:
        templatestrings_load.append(template_load.format(val1=vals, val2=vals, val3=vals))
        tempaltestrings_save.append(template_save.format(vals, vals))
        if vals == 'Challenger':
            templatestrings_comparison.append(
                template_comp.format(curr=vals, rankC=vals, rankZ=vals, rankU1=vals, rankD1=TierValues[index + 1],
                                     rankD2=TierValues[index + 2]))
        elif vals == 'Iron4_50':
            templatestrings_comparison.append(
                template_comp.format(curr=vals, rankC=vals, rankZ=vals, rankU1=TierValues[index - 1],
                                     rankD1=TierValues[index + 1],
                                     rankD2=TierValues[index + 1]))
        elif vals == 'Iron4_0':
            templatestrings_comparison.append(
                template_comp.format(curr=vals, rankC=vals, rankZ=vals, rankU1=TierValues[index - 1],
                                     rankD1=vals,
                                     rankD2=vals))
        else:
            templatestrings_comparison.append(
                template_comp.format(curr=vals, rankC=vals, rankZ=vals, rankU1=TierValues[index - 1],
                                     rankD1=TierValues[index + 1],
                                     rankD2=TierValues[index + 2]))
    # print(templatestrings)
    return templatestrings_load, tempaltestrings_save, templatestrings_comparison


f = open("generated/generatedcode.py", "a")
loadstrings, savestrings, compstrings = codeGen()
f.write("import pandas as pd \nimport counterclass")
f.write("\ndef compare(cl1,cl2,tier):\n")
for code in compstrings:
    f.write(code)
    f.write("\n")
f.write("\ndef save(cl1):\n")
for code in savestrings:
    f.write(code)
    f.write("\n")
f.write("\ndef load(cl1):\n")
for code in loadstrings:
    f.write(code)
    f.write("\n")
f.close()
