import math, w3, w4, w6, os, cosine
from pprint import pprint
import tfidf

path = './text files'
path_kategori = './text kategori'
def dob(path):
    this_path = os.path.split(__file__)[0]
    path = os.path.join(this_path, path)

    # membaca sekaligus pre-processing semua artikel simpan ke dictionary
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + "/" + item, 'r') as file:
                articles[item] = w3.preprotext(file.read())

    # representasi bow
    list_of_bow = [] # membuat list kosong
    dict_of_bow = {} # membuat dict kosong
    for key, value in articles.items(): # iterasi pasangan key, value
        # print key, value
        list_token = value.split() # cari kata2 dengan men-split
        dic = w4.bow(list_token)   # membuat bow
        # dict_of_bow[key] = list_of_bow.append(dic)    # append bow ke list kosong yg di atas
        # dict_of_bow[key] = dic
        dic = w4.sortdic(dic,descending=True)
        dic_bow = {}
        # print dic 
        for keys,values in dic:
            # if values > 3: # dengan bobot setiap kata yang dihitung lebih dari 3 
            dic_bow[keys] = values
        dict_of_bow[key] = dic_bow
    # membuat matrix
    # matrix_akhir = w4.matrix(list_of_bow,normalized=True) # jalankan fungsi matrix ke list_of_bow
    return dict_of_bow

def dob_kategori(path_kategori):
    this_path = os.path.split(__file__)[0]
    path = os.path.join(this_path, path_kategori)

    # membaca sekaligus pre-processing semua artikel kategori lalu disimpan ke dictionary
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + "/" + item, 'r') as file:
                articles[item] = w3.preprotext(file.read())

    # representasi bow
    list_of_bow = [] # membuat list kosong
    dict_of_bow = {} # membuat dict kosong
    for key, value in articles.items(): # iterasi pasangan key, value
        # print key, value
        list_token = value.split() # cari kata2 dengan men-split
        dic = w4.bow(list_token)   # membuat bow
        # dict_of_bow[key] = list_of_bow.append(dic)    # append bow ke list kosong yg di atas
        # dict_of_bow[key] = dic
        dic = w4.sortdic(dic,descending=True)
        dic_bow = {}
        # print dic
        for keys,values in dic:
            # if values > 3: # dengan bobot setiap kata yang dihitung lebih dari 3
            dic_bow[keys] = values
        dict_of_bow[key] = dic_bow
    # membuat matrix
    # matrix_akhir = w4.matrix(list_of_bow,normalized=True) # jalankan fungsi matrix ke list_of_bow
    return dict_of_bow

def article_limit(path):
    this_path = os.path.split(__file__)[0]
    path = os.path.join(this_path, path)

    # membaca sekaligus pre-processing semua artikel simpan ke dictionary
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + "/" + item, 'r') as file:
                articles[item] = w3.preprotext(file.read())

    # representasi bow
    list_of_bow = [] # membuat list kosong
    for key, value in articles.items(): # iterasi pasangan key, value
        list_token = value.split() # cari kata2 dengan men-split
        dic = w4.bow(list_token)   # membuat bow
        list_of_bow.append(dic) # daftar list of bow

    # membuat matrix dan jalankan fungsi matrix ke list_of_bow
    matrix_akhir = w4.matrix(list_of_bow,normalized=True) 

    dict_of_bow = {} # membuat dict kosong
    for key, value in articles.items(): # iterasi pasangan key, value
        list_token = value.split() # cari kata2 dengan men-split
        dic = w4.bow(list_token)   # membuat bow
        # dict_of_bow[key] = list_of_bow.append(dic)    # append bow ke list kosong yg di atas
        # dict_of_bow[key] = dic
        dic = w4.sortdic(dic,descending=True)
        dic_bow = {}
        # print dic 
        for keys,values in dic:
            if values > 1: # dengan bobot setiap kata yang dihitung lebih dari 3
                dic_bow[keys] = values
        dict_of_bow[key] = dic_bow
    # membuat matrix
    # matrix_akhir = w4.matrix(list_of_bow,normalized=True) # jalankan fungsi matrix ke list_of_bow
    #print ("LALALLA")
    #print(dict_of_bow)
    return dict_of_bow

def article(path):
    this_path = os.path.split(__file__)[0]
    path = os.path.join(this_path, path)

    # membaca sekaligus pre-processing semua artikel simpan ke dictionary
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    return articles

def text_exam():
    text_dic = {
        'd1' : 'saya yakin dia tiada mampu menolak saya',
        'd2' : 'pokoknya tembak dulu urusan sakit belakangan',
        'd3' : 'sepertinya dia sudah menolak saya sebelum sempat saya tembak',
        'd4' : 'saya mau untuk tembak langsung tapi takut dia menolak'
    }
    kalimat = {}
    for key,value in text_dic.items():
        kalimat[key] = w3.prepro_base(value)

    dobs = {}
    for key,value in kalimat.items():
        list_token = value.split()
        dic = w4.bow(list_token)
        dobs[key] = dic

    return dobs

def test_similarity(dict_document,keywod):
    keywod = w3.prepro_base(keywod).split()
    print keywod
    table = tfidf.TfIdf()
    for key,value in dict_document.items():
         table.add_document(key, value)
    return table.similarities(keywod)
    # return w4.sortdic(table.similarities(keywod),descending=True)



def findSim(keyword,pathcorpus):
    res_tf = test_similarity(dob(path),keyword) # Hasil tf idf

    keyword = w3.prepro_base(keyword) # prepo kata kuncinya dan artikel
    articles = article_limit(pathcorpus)
    # doct = dob(pathcorpus) # artikel/document yang utuh

    # Hitung jarak Jarak Cosine hasil dari tfidf
    simi = {}
    for key, value in res_tf.items():
        keyw = cosine.text_to_vector(keyword)
        doc = articles[key] # artikel dengan minimal 4 freq kemunculan

        # doc = cosine.text_to_vector(value) # artikel di vectorkan
        score = round(cosine.get_cosine(keyw, doc)*100,4)
        if score != 0.0:
            simi[key] = score
        #print(key)
        #print(doc[key])
        #print(doc)

    # hasil_simi = w4.sortdic(simi, descending=True) # hasil return di zip dan sort

    return simi


def test_kategori(path, path_kategori, keyw):
    hasil_dob_kategori = dob_kategori(path_kategori)
    hasil_findSim = findSim(keyw, path)

    list_judul = []
    for key, value in hasil_findSim.items():
        list_judul.append(key)

    this_path = os.path.split(__file__)[0]
    path = os.path.join(this_path, path)

    words = {}
    for item in list_judul:
        if item.endswith(".txt"):
            with open(path + "/" + item, 'r') as file:
                words[item] = w3.preprotext(file.read())

    words2 = {}
    for item in list_judul:
        if item.endswith(".txt"):
            with open(path + "/" + item, 'r') as file:
                #print(dob(w3.preprotext(file.read())))
                words2[item] = w3.prepro_base(file.read())


    dict_of_bow = {}  # membuat dict kosong
    for key, value in words.items():  # iterasi pasangan key, value
        # print key, value
        list_token = value.split()  # cari kata2 dengan men-split
        dic = w4.bow(list_token)  # membuat bow
        # dict_of_bow[key] = list_of_bow.append(dic)    # append bow ke list kosong yg di atas
        # dict_of_bow[key] = dic
        dic = w4.sortdic(dic, descending=True)
        dic_bow = {}
        # print dic
        for keys, values in dic:
            # if values > 3: # dengan bobot setiap kata yang dihitung lebih dari 3
            dic_bow[keys] = values
        dict_of_bow[key] = dic_bow
    # membuat matrix
    # matrix_akhir = w4.matrix(list_of_bow,normalized=True) # jalankan fungsi matrix ke list_of_bow

    hasil_cek_kategori = {}
    kategori = {}
    for judul_file_hasil_cosine, value_hasil_cosine in words2.items():
        simi = {}
        vector_hasil_cosine = cosine.text_to_vector(value_hasil_cosine)

        for judul_file_kategori, value_file_kategori in hasil_dob_kategori.items():
            score = round(cosine.get_cosine(vector_hasil_cosine, value_file_kategori)*100,4)

            if score != 0.0:
                nama_kategori = judul_file_kategori.split(".")[0]
                #print (nama_kategori)
                simi[nama_kategori] = score

        hasil_cek_kategori[judul_file_hasil_cosine] = w4.sortdic(simi, descending=True, n=1)[0]
        # hasil_cek_kategori[judul_file_hasil_cosine] = simi

        #hasil_cek_kategori[judul_file_hasil_cosine] = w4.sortdic(simi, descending=True, n=1)
    #kategori = hasil_cek_kategori.values()
    #print (hasil_cek_kategori)
    return hasil_cek_kategori

def final_terakhir(keyw,path, path_kategori = './text kategori'):
    similarity = findSim(keyw,path)
    kategori = test_kategori(path,path_kategori,keyw)
    final = w4.sortdic_last(similarity, kategori , descending=True)
    return final

keyw = "jokowi adalah presiden"
#final = zip(findSim(keyw,path),test_kategori(path, path_kategori, keyw))
# print(final(path, path_kategori, keyw))
#print(test_kategori(path, path_kategori, keyw))

# keyw = ['saya','yakin','dia','menolak','tembak','sebelum']
# keyw = ['yang']
# print text_exam()
# print findSim(keyw, path)
# print test_similarity(dob(path),keyw)
# doct = dob(path) 
# print doct['lf.txt']
