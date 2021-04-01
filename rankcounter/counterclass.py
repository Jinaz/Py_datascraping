import bs4
import pandas as pd


class RankCounter():
    Challenger = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Grandmaster = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Master = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])

    Dia1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Dia1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Dia2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Dia2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Dia3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Dia3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Dia4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Dia4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])

    Plat1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Plat1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Plat2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Plat2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Plat3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Plat3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Plat4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Plat4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])

    Gold1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Gold1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Gold2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Gold2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Gold3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Gold3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Gold4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Gold4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])

    Sil1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Sil1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Sil2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Sil2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Sil3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Sil3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Sil4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Sil4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])

    B1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    B1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    B2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    B2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    B3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    B3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    B4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    B4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])

    Iron1_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Iron1_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Iron2_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Iron2_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Iron3_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Iron3_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Iron4_50 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])
    Iron4_0 = pd.DataFrame(columns=['Summonername', 'Rank', 'LP'])

    climbs = None

    def __init__(self):
        self.climbs = False

    def readurl(self, url):
        import urllib.request

        fp = urllib.request.urlopen(url)
        mybytes = fp.read()

        string = mybytes.decode("utf8")
        fp.close()
        return string

    def postfilterString(self, string, replaceComma=False):

        result = string.replace('\n', '')
        result = result.replace('\t', '')
        if replaceComma:
            result = result.replace(',', '')
        return result

    def loopOverOPGG(self, url="https://euw.op.gg/ranking/ladder/page=1"):
        htmlstring = self.readurl(url)
        soup = bs4.BeautifulSoup(htmlstring, features="html.parser")
        mydiv = soup.find_all("div", {"class": "ranking-pagination__desc"})
        summonercount = int(self.postfilterString(mydiv[0].find_all("span")[1].getText(), True))
        pagecount = int(summonercount / 100)
        for i in range(pagecount):
            self.runspider("https://euw.op.gg/ranking/ladder/page={}".format(pagecount))

        print(self.Challenger)

    def runspider(self, url="https://euw.op.gg/ranking/ladder/page=1"):

        htmlstring = self.readurl(url)
        soup = bs4.BeautifulSoup(htmlstring, features="html.parser")
        mytr = soup.find_all("tr", {"class": "ranking-table__row"})
        # print(mytr[1])
        for tr in mytr:
            trsoup = tr
            cells = trsoup.find_all("td", {"class": "ranking-table__cell"})
            num = 0
            for cell in cells:
                # print("Cell", num, cell)
                num += 1
            key = cells[1].find_all("span")[0].getText()
            tier = self.postfilterString(cells[2].getText())
            lpamount = int(self.postfilterString(cells[3].getText(), True).strip(" LP"))

            self.insertIntoTable((key, tier, lpamount))

    def insertIntoTable(self, obj):
        newrow = {'Summonername': obj[0], 'Rank': obj[1], 'LP': obj[2]}
        if obj[1] == 'Challenger':
            self.Challenger.append(newrow)
        if obj[1] == 'Grandmaster':
            self.Grandmaster.append(newrow)
        if obj[1] == 'Master':
            self.Master.append(newrow)

        if obj[1] == 'Diamond 1':
            if obj[2] > 50:
                self.Dia1_50.append(newrow)
            else:
                self.Dia1_0.append(newrow)
        if obj[1] == 'Diamond 2':
            if obj[2] > 50:
                self.Dia2_50.append(newrow)
            else:
                self.Dia2_0.append(newrow)
        if obj[1] == 'Diamond 3':
            if obj[2] > 50:
                self.Dia3_50.append(newrow)
            else:
                self.Dia3_0.append(newrow)
        if obj[1] == 'Diamond 4':
            if obj[2] > 50:
                self.Dia4_50.append(newrow)
            else:
                self.Dia4_0.append(newrow)

        if obj[1] == 'Platinum 1':
            if obj[2] > 50:
                self.Plat1_50.append(newrow)
            else:
                self.Plat1_0.append(newrow)
        if obj[1] == 'Platinum 2':
            if obj[2] > 50:
                self.Plat2_50.append(newrow)
            else:
                self.Plat2_0.append(newrow)
        if obj[1] == 'Platinum 3':
            if obj[2] > 50:
                self.Plat3_50.append(newrow)
            else:
                self.Plat3_0.append(newrow)
        if obj[1] == 'Platinum 4':
            if obj[2] > 50:
                self.Plat4_50.append(newrow)
            else:
                self.Plat4_0.append(newrow)

        if obj[1] == 'Gold 1':
            if obj[2] > 50:
                self.Gold1_50.append(newrow)
            else:
                self.Gold1_0.append(newrow)
        if obj[1] == 'Gold 2':
            if obj[2] > 50:
                self.Gold2_50.append(newrow)
            else:
                self.Gold2_0.append(newrow)
        if obj[1] == 'Gold 3':
            if obj[2] > 50:
                self.Gold3_50.append(newrow)
            else:
                self.Gold3_0.append(newrow)
        if obj[1] == 'Gold 4':
            if obj[2] > 50:
                self.Gold4_50.append(newrow)
            else:
                self.Gold4_0.append(newrow)

        if obj[1] == 'Silver 1':
            if obj[2] > 50:
                self.Sil1_50.append(newrow)
            else:
                self.Sil1_0.append(newrow)
        if obj[1] == 'Silver 2':
            if obj[2] > 50:
                self.Sil2_50.append(newrow)
            else:
                self.Sil2_0.append(newrow)
        if obj[1] == 'Silver 3':
            if obj[2] > 50:
                self.Sil3_50.append(newrow)
            else:
                self.Sil3_0.append(newrow)
        if obj[1] == 'Silver 4':
            if obj[2] > 50:
                self.Sil4_50.append(newrow)
            else:
                self.Sil4_0.append(newrow)

        if obj[1] == 'Bronze 1':
            if obj[2] > 50:
                self.B1_50.append(newrow)
            else:
                self.B1_0.append(newrow)
        if obj[1] == 'Bronze 2':
            if obj[2] > 50:
                self.B2_50.append(newrow)
            else:
                self.B2_0.append(newrow)
        if obj[1] == 'Bronze 3':
            if obj[2] > 50:
                self.B3_50.append(newrow)
            else:
                self.B3_0.append(newrow)
        if obj[1] == 'Bronze 4':
            if obj[2] > 50:
                self.B4_50.append(newrow)
            else:
                self.B4_0.append(newrow)

        if obj[1] == 'Iron 1':
            if obj[2] > 50:
                self.Iron1_50.append(newrow)
            else:
                self.Iron1_0.append(newrow)
        if obj[1] == 'Iron 2':
            if obj[2] > 50:
                self.Iron2_50.append(newrow)
            else:
                self.Iron2_0.append(newrow)
        if obj[1] == 'Iron 3':
            if obj[2] > 50:
                self.Iron3_50.append(newrow)
            else:
                self.Iron3_0.append(newrow)
        if obj[1] == 'Iron 4':
            if obj[2] > 50:
                self.Iron4_50.append(newrow)
            else:
                self.Iron4_0.append(newrow)

    def savedata(self):
        import generated.generatedcode as gn
        gn.save(self)

    def saveWithCSV(self, data, filename):
        data.to_csv('Data/{}.csv'.format(filename))

    def loaddata(self):
        import generated.generatedcode as gn
        gn.load(self)

    def compare_before(self, cl2, tier):
        import generated.generatedcode as gn

        if type(cl2) == type(self):
            negatives, positives = gn.compare(self, cl2, tier)
            return negatives, positives
