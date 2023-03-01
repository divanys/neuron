import gensim

w2v_fpath = "all.norm-sz100-w10-cb0-it1-min100.w2v"
w2v = gensim.models.KeyedVectors.load_word2vec_format(w2v_fpath, binary=True, unicode_errors='ignore')
w2v.init_sims(replace=True)

for word, score in w2v.most_similar(positive=[u"птица", u"животное"], negative=[u"рыба"]):
    print(word, score)
