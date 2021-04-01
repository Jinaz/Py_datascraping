import counterclass

if __name__ == "__main__":
    ranker_old = counterclass.RankCounter()
    #ranker.runspider()
    try:
        ranker_old.loaddata()
    except Exception:
        ranker_old.loopOverOPGG()

    ranker_new = counterclass.RankCounter()
    ranker_new.loopOverOPGG()

    result = ranker_old.compare_before(ranker_new, "Sil1_0")

    ranker_new.savedata()

    print("negatives number:", len(result[0]))
    #print("negatives : ",result[0])
    print("positives number:", len(result[1]))
    #print("positives : ", result[1])