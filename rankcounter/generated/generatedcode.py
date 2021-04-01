import pandas as pd 
import counterclass
def compare(cl1,cl2,tier):
    if tier == "Challenger":
        diffs = []
        for el in cl1.Challenger:
            if el not in cl2.Challenger:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Challenger:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Grandmaster":
        diffs = []
        for el in cl1.Grandmaster:
            if el not in cl2.Grandmaster:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Master":
        diffs = []
        for el in cl1.Master:
            if el not in cl2.Master:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Dia1_50":
        diffs = []
        for el in cl1.Dia1_50:
            if el not in cl2.Dia1_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Dia1_0":
        diffs = []
        for el in cl1.Dia1_0:
            if el not in cl2.Dia1_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Dia2_50":
        diffs = []
        for el in cl1.Dia2_50:
            if el not in cl2.Dia2_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Dia2_0":
        diffs = []
        for el in cl1.Dia2_0:
            if el not in cl2.Dia2_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Dia3_50":
        diffs = []
        for el in cl1.Dia3_50:
            if el not in cl2.Dia3_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Dia3_0":
        diffs = []
        for el in cl1.Dia3_0:
            if el not in cl2.Dia3_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Dia4_50":
        diffs = []
        for el in cl1.Dia4_50:
            if el not in cl2.Dia4_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Dia4_0":
        diffs = []
        for el in cl1.Dia4_0:
            if el not in cl2.Dia4_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Plat1_50":
        diffs = []
        for el in cl1.Plat1_50:
            if el not in cl2.Plat1_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Plat1_0":
        diffs = []
        for el in cl1.Plat1_0:
            if el not in cl2.Plat1_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Plat2_50":
        diffs = []
        for el in cl1.Plat2_50:
            if el not in cl2.Plat2_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Plat2_0":
        diffs = []
        for el in cl1.Plat2_0:
            if el not in cl2.Plat2_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Plat3_50":
        diffs = []
        for el in cl1.Plat3_50:
            if el not in cl2.Plat3_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Plat3_0":
        diffs = []
        for el in cl1.Plat3_0:
            if el not in cl2.Plat3_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Plat4_50":
        diffs = []
        for el in cl1.Plat4_50:
            if el not in cl2.Plat4_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Plat4_0":
        diffs = []
        for el in cl1.Plat4_0:
            if el not in cl2.Plat4_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Gold1_50":
        diffs = []
        for el in cl1.Gold1_50:
            if el not in cl2.Gold1_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Gold1_0":
        diffs = []
        for el in cl1.Gold1_0:
            if el not in cl2.Gold1_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Gold2_50":
        diffs = []
        for el in cl1.Gold2_50:
            if el not in cl2.Gold2_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Gold2_0":
        diffs = []
        for el in cl1.Gold2_0:
            if el not in cl2.Gold2_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Gold3_50":
        diffs = []
        for el in cl1.Gold3_50:
            if el not in cl2.Gold3_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Gold3_0":
        diffs = []
        for el in cl1.Gold3_0:
            if el not in cl2.Gold3_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Gold4_50":
        diffs = []
        for el in cl1.Gold4_50:
            if el not in cl2.Gold4_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Gold4_0":
        diffs = []
        for el in cl1.Gold4_0:
            if el not in cl2.Gold4_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Sil1_50":
        diffs = []
        for el in cl1.Sil1_50:
            if el not in cl2.Sil1_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Sil1_0":
        diffs = []
        for el in cl1.Sil1_0:
            if el not in cl2.Sil1_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Sil2_50":
        diffs = []
        for el in cl1.Sil2_50:
            if el not in cl2.Sil2_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Sil2_0":
        diffs = []
        for el in cl1.Sil2_0:
            if el not in cl2.Sil2_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Sil3_50":
        diffs = []
        for el in cl1.Sil3_50:
            if el not in cl2.Sil3_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Sil3_0":
        diffs = []
        for el in cl1.Sil3_0:
            if el not in cl2.Sil3_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Sil4_50":
        diffs = []
        for el in cl1.Sil4_50:
            if el not in cl2.Sil4_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Sil4_0":
        diffs = []
        for el in cl1.Sil4_0:
            if el not in cl2.Sil4_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "B1_50":
        diffs = []
        for el in cl1.B1_50:
            if el not in cl2.B1_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "B1_0":
        diffs = []
        for el in cl1.B1_0:
            if el not in cl2.B1_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "B2_50":
        diffs = []
        for el in cl1.B2_50:
            if el not in cl2.B2_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "B2_0":
        diffs = []
        for el in cl1.B2_0:
            if el not in cl2.B2_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "B3_50":
        diffs = []
        for el in cl1.B3_50:
            if el not in cl2.B3_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "B3_0":
        diffs = []
        for el in cl1.B3_0:
            if el not in cl2.B3_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "B4_50":
        diffs = []
        for el in cl1.B4_50:
            if el not in cl2.B4_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "B4_0":
        diffs = []
        for el in cl1.B4_0:
            if el not in cl2.B4_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Iron1_50":
        diffs = []
        for el in cl1.Iron1_50:
            if el not in cl2.Iron1_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Iron1_0":
        diffs = []
        for el in cl1.Iron1_0:
            if el not in cl2.Iron1_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Iron2_50":
        diffs = []
        for el in cl1.Iron2_50:
            if el not in cl2.Iron2_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Iron2_0":
        diffs = []
        for el in cl1.Iron2_0:
            if el not in cl2.Iron2_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Iron3_50":
        diffs = []
        for el in cl1.Iron3_50:
            if el not in cl2.Iron3_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Iron3_0":
        diffs = []
        for el in cl1.Iron3_0:
            if el not in cl2.Iron3_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Master:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Iron4_50":
        diffs = []
        for el in cl1.Iron4_50:
            if el not in cl2.Iron4_50:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Grandmaster or diff in cl2.Grandmaster:
                    negatives.append(diff)
            return negatives, positives
    if tier == "Iron4_0":
        diffs = []
        for el in cl1.Iron4_0:
            if el not in cl2.Iron4_0:
                diffs.append(el)
            negatives = []
            positives = []
            for diff in diffs:
                if diff in cl2.Iron4_0:
                    positives.append(diff)
                elif diff in cl2.Iron4_0 or diff in cl2.Iron4_0:
                    negatives.append(diff)
            return negatives, positives

def save(cl1):
    cl1.saveWithCSV(cl1.Challenger, 'Challenger')
    cl1.saveWithCSV(cl1.Grandmaster, 'Grandmaster')
    cl1.saveWithCSV(cl1.Master, 'Master')
    cl1.saveWithCSV(cl1.Dia1_50, 'Dia1_50')
    cl1.saveWithCSV(cl1.Dia1_0, 'Dia1_0')
    cl1.saveWithCSV(cl1.Dia2_50, 'Dia2_50')
    cl1.saveWithCSV(cl1.Dia2_0, 'Dia2_0')
    cl1.saveWithCSV(cl1.Dia3_50, 'Dia3_50')
    cl1.saveWithCSV(cl1.Dia3_0, 'Dia3_0')
    cl1.saveWithCSV(cl1.Dia4_50, 'Dia4_50')
    cl1.saveWithCSV(cl1.Dia4_0, 'Dia4_0')
    cl1.saveWithCSV(cl1.Plat1_50, 'Plat1_50')
    cl1.saveWithCSV(cl1.Plat1_0, 'Plat1_0')
    cl1.saveWithCSV(cl1.Plat2_50, 'Plat2_50')
    cl1.saveWithCSV(cl1.Plat2_0, 'Plat2_0')
    cl1.saveWithCSV(cl1.Plat3_50, 'Plat3_50')
    cl1.saveWithCSV(cl1.Plat3_0, 'Plat3_0')
    cl1.saveWithCSV(cl1.Plat4_50, 'Plat4_50')
    cl1.saveWithCSV(cl1.Plat4_0, 'Plat4_0')
    cl1.saveWithCSV(cl1.Gold1_50, 'Gold1_50')
    cl1.saveWithCSV(cl1.Gold1_0, 'Gold1_0')
    cl1.saveWithCSV(cl1.Gold2_50, 'Gold2_50')
    cl1.saveWithCSV(cl1.Gold2_0, 'Gold2_0')
    cl1.saveWithCSV(cl1.Gold3_50, 'Gold3_50')
    cl1.saveWithCSV(cl1.Gold3_0, 'Gold3_0')
    cl1.saveWithCSV(cl1.Gold4_50, 'Gold4_50')
    cl1.saveWithCSV(cl1.Gold4_0, 'Gold4_0')
    cl1.saveWithCSV(cl1.Sil1_50, 'Sil1_50')
    cl1.saveWithCSV(cl1.Sil1_0, 'Sil1_0')
    cl1.saveWithCSV(cl1.Sil2_50, 'Sil2_50')
    cl1.saveWithCSV(cl1.Sil2_0, 'Sil2_0')
    cl1.saveWithCSV(cl1.Sil3_50, 'Sil3_50')
    cl1.saveWithCSV(cl1.Sil3_0, 'Sil3_0')
    cl1.saveWithCSV(cl1.Sil4_50, 'Sil4_50')
    cl1.saveWithCSV(cl1.Sil4_0, 'Sil4_0')
    cl1.saveWithCSV(cl1.B1_50, 'B1_50')
    cl1.saveWithCSV(cl1.B1_0, 'B1_0')
    cl1.saveWithCSV(cl1.B2_50, 'B2_50')
    cl1.saveWithCSV(cl1.B2_0, 'B2_0')
    cl1.saveWithCSV(cl1.B3_50, 'B3_50')
    cl1.saveWithCSV(cl1.B3_0, 'B3_0')
    cl1.saveWithCSV(cl1.B4_50, 'B4_50')
    cl1.saveWithCSV(cl1.B4_0, 'B4_0')
    cl1.saveWithCSV(cl1.Iron1_50, 'Iron1_50')
    cl1.saveWithCSV(cl1.Iron1_0, 'Iron1_0')
    cl1.saveWithCSV(cl1.Iron2_50, 'Iron2_50')
    cl1.saveWithCSV(cl1.Iron2_0, 'Iron2_0')
    cl1.saveWithCSV(cl1.Iron3_50, 'Iron3_50')
    cl1.saveWithCSV(cl1.Iron3_0, 'Iron3_0')
    cl1.saveWithCSV(cl1.Iron4_50, 'Iron4_50')
    cl1.saveWithCSV(cl1.Iron4_0, 'Iron4_0')

def load(cl1):
    df = pd.read_csv('Data/Challenger.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Challenger = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Challenger.append(newrow)
    df = pd.read_csv('Data/Grandmaster.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Grandmaster = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Grandmaster.append(newrow)
    df = pd.read_csv('Data/Master.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Master = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Master.append(newrow)
    df = pd.read_csv('Data/Dia1_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Dia1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Dia1_50.append(newrow)
    df = pd.read_csv('Data/Dia1_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Dia1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Dia1_0.append(newrow)
    df = pd.read_csv('Data/Dia2_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Dia2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Dia2_50.append(newrow)
    df = pd.read_csv('Data/Dia2_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Dia2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Dia2_0.append(newrow)
    df = pd.read_csv('Data/Dia3_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Dia3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Dia3_50.append(newrow)
    df = pd.read_csv('Data/Dia3_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Dia3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Dia3_0.append(newrow)
    df = pd.read_csv('Data/Dia4_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Dia4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Dia4_50.append(newrow)
    df = pd.read_csv('Data/Dia4_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Dia4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Dia4_0.append(newrow)
    df = pd.read_csv('Data/Plat1_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Plat1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Plat1_50.append(newrow)
    df = pd.read_csv('Data/Plat1_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Plat1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Plat1_0.append(newrow)
    df = pd.read_csv('Data/Plat2_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Plat2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Plat2_50.append(newrow)
    df = pd.read_csv('Data/Plat2_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Plat2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Plat2_0.append(newrow)
    df = pd.read_csv('Data/Plat3_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Plat3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Plat3_50.append(newrow)
    df = pd.read_csv('Data/Plat3_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Plat3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Plat3_0.append(newrow)
    df = pd.read_csv('Data/Plat4_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Plat4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Plat4_50.append(newrow)
    df = pd.read_csv('Data/Plat4_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Plat4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Plat4_0.append(newrow)
    df = pd.read_csv('Data/Gold1_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Gold1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Gold1_50.append(newrow)
    df = pd.read_csv('Data/Gold1_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Gold1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Gold1_0.append(newrow)
    df = pd.read_csv('Data/Gold2_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Gold2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Gold2_50.append(newrow)
    df = pd.read_csv('Data/Gold2_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Gold2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Gold2_0.append(newrow)
    df = pd.read_csv('Data/Gold3_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Gold3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Gold3_50.append(newrow)
    df = pd.read_csv('Data/Gold3_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Gold3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Gold3_0.append(newrow)
    df = pd.read_csv('Data/Gold4_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Gold4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Gold4_50.append(newrow)
    df = pd.read_csv('Data/Gold4_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Gold4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Gold4_0.append(newrow)
    df = pd.read_csv('Data/Sil1_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Sil1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Sil1_50.append(newrow)
    df = pd.read_csv('Data/Sil1_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Sil1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Sil1_0.append(newrow)
    df = pd.read_csv('Data/Sil2_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Sil2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Sil2_50.append(newrow)
    df = pd.read_csv('Data/Sil2_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Sil2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Sil2_0.append(newrow)
    df = pd.read_csv('Data/Sil3_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Sil3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Sil3_50.append(newrow)
    df = pd.read_csv('Data/Sil3_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Sil3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Sil3_0.append(newrow)
    df = pd.read_csv('Data/Sil4_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Sil4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Sil4_50.append(newrow)
    df = pd.read_csv('Data/Sil4_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Sil4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Sil4_0.append(newrow)
    df = pd.read_csv('Data/B1_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.B1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.B1_50.append(newrow)
    df = pd.read_csv('Data/B1_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.B1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.B1_0.append(newrow)
    df = pd.read_csv('Data/B2_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.B2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.B2_50.append(newrow)
    df = pd.read_csv('Data/B2_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.B2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.B2_0.append(newrow)
    df = pd.read_csv('Data/B3_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.B3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.B3_50.append(newrow)
    df = pd.read_csv('Data/B3_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.B3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.B3_0.append(newrow)
    df = pd.read_csv('Data/B4_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.B4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.B4_50.append(newrow)
    df = pd.read_csv('Data/B4_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.B4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.B4_0.append(newrow)
    df = pd.read_csv('Data/Iron1_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Iron1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Iron1_50.append(newrow)
    df = pd.read_csv('Data/Iron1_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Iron1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Iron1_0.append(newrow)
    df = pd.read_csv('Data/Iron2_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Iron2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Iron2_50.append(newrow)
    df = pd.read_csv('Data/Iron2_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Iron2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Iron2_0.append(newrow)
    df = pd.read_csv('Data/Iron3_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Iron3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Iron3_50.append(newrow)
    df = pd.read_csv('Data/Iron3_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Iron3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Iron3_0.append(newrow)
    df = pd.read_csv('Data/Iron4_50.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Iron4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Iron4_50.append(newrow)
    df = pd.read_csv('Data/Iron4_0.csv')
    sn = df['Summonername']
    rank = df['Rank']
    lp = df['LP']
    cl1.Iron4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    for i in range(len(sn)):
        newrow = {'Summonername': sn[i], 'Rank': rank[i], 'LP': lp[i]}
        cl1.Iron4_0.append(newrow)
