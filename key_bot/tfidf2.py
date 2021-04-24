import math
import pandas

# using pandas as reader
content = pandas.read_csv("postillon.csv", sep="	")

# print(content["news_text"][108])
# "randomly" chosen docs as query
extext1 = content["news_text"][0]
extext2 = content["news_text"][10]
extext3 = content["news_text"][20]

# debug reasons, setting a number of documents makes process faster
# if you want to run all 5000 docs uncomment following line
# documentcount = len(content["news_text"])

documentcount = 300

# make docs into an array of docs as array of strings.
alldocs = [content["news_text"][i].split() for i in range(documentcount)]


def get_bow(tokens):
    # bag of words
    bow = []
    # go through all lists and add terms into a bag of words
    for list in tokens:
        for tk in list:
            if tk not in bow:
                bow.append(tk)
    return bow


def idf(text, bow):
    # build a dictionary of term:weighted idf value
    # count document fequency
    df = {term: 0 for term in bow}
    for term in bow:
        for doc in text:
            if term in doc:
                df[term] += 1
    # apply log10 weighting
    idf = {term: math.log10(len(text) / df[term]) for term in bow}
    return idf


# some command line output and bag of words construction and idf construction
print("preparing bag of words and weighted idf, documents to be read: {}".format(documentcount))
bow = get_bow(alldocs)
print("done preparing bag of words: with {} terms".format(len(bow)))
idf_dict = idf(alldocs, bow)
print("done preparation, {} documents read".format(len(content["news_text"])))


def weightedtf(text, bow):
    termdict = {term: 0.0 for term in bow}
    # count the occurences in one document
    for term in text:
        termdict[term] += 1.0
    # apply w_{t,d} = 1 + log10 (tf_{t,d}) if tf_{t,d} > 0
    for term, value in termdict.items():
        if value > 0:
            termdict[term] = 1.0 + math.log10(value)
    # return a dict of {term: weightedtf}
    return termdict


def simscore(query, text2):
    # turn query into a single string array
    tokenslist1 = []
    for text in query:
        for item in text.split():
            tokenslist1.append(item)

    # prepare document text
    tokenslist2 = text2.split()

    # get the tf values
    tf1 = weightedtf(tokenslist1, bow)
    tf2 = weightedtf(tokenslist2, bow)

    # get idf values
    tfidf1 = {k: tf1[k] * idf_dict[k] for k in bow}
    tfidf2 = {k: tf2[k] * idf_dict[k] for k in bow}

    # use tfidfs and cos sim

    # square root of sum of squares
    # for query
    sqrtpowsum1 = 0
    for val in tfidf1.values():
        sqrtpowsum1 += math.pow(val, 2)
    sqrtpowsum1 = math.sqrt(sqrtpowsum1)

    # for doc
    sqrtpowsum2 = 0
    for val in tfidf2.values():
        sqrtpowsum2 += math.pow(val, 2)
    sqrtpowsum2 = math.sqrt(sqrtpowsum2)

    # sum of products
    sum = 0
    for term in bow:
        sum += (tfidf1[term] * tfidf2[term])

    # similarity score
    # some documents contain NO news text!
    sim = 0.0
    if (sqrtpowsum1 * sqrtpowsum2) > 0:
        sim = sum / (sqrtpowsum1 * sqrtpowsum2)
    else:
        print("document is empty")

    return sim


# running with 2 inout texts
print(simscore([extext1], extext1))


# use 3 docs as query and rank others
def avg3doc(doc1, doc2, doc3):
    from collections import OrderedDict
    print("documents considered: ", documentcount)
    # a dictionary to store all docs
    docranking = {docid: 0 for docid in range(documentcount)}

    # put all sim values into the value of the dict
    for docid in docranking.keys():
        # compare 3 query texts to a news text
        val = simscore([doc1, doc2, doc3], content["news_text"][docid])
        print(docid, "checked: ", val)

        rankvalue = val
        docranking[docid] = rankvalue

    # use ordered dict to sort and reverse to get best sim values
    out = OrderedDict(sorted(docranking.items(), key=lambda kv: kv[1], reverse=True))
    # for some reason using a dict results in {(0 : ' '),(0 : ' '),(0 : ' '),(0 : ' ')} tuples
    # so going for an array
    rankeddoc = []  # {rankid: (0,"") for rankid in range(100)}
    number = 1
    # get the best similarity values
    for k, v in out.items():
        # output top 100 results
        if number < 101:
            print("rank {}: ".format(number),"doc id:", k, content["news_text"][k])
            print("similarity score: ", v)
            rankeddoc.append((k, content["news_text"][k]))
        number += 1

    return rankeddoc


# output of the 3 docs similarity to all others
print(avg3doc(extext1, extext2, extext3))
