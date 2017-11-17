import math, w3, w4, w6, os
from pprint import pprint
import tfidf

path = './text files'

def dob(path):
    
    this_path = os.path.split(__file__)[0]
    path = os.path.join(this_path, path)

    # membaca sekaligus pre-processing semua artikel simpan ke dictionary
    articles = {}
    for item in os.listdir(path):
        if item.endswith(".txt"):
            with open(path + "/" + item, 'r') as file:
                articles[item] = w3.prepro_base(file.read())

    # representasi bow
    list_of_bow = [] # membuat list kosong
    dict_of_bow = {} # membuat dict kosong
    for key, value in articles.items(): # iterasi pasangan key, value
        # print key, value
        list_token = value.split() # cari kata2 dengan men-split
        dic = w4.bow(list_token)   # membuat bow
        # dict_of_bow[key] = list_of_bow.append(dic)    # append bow ke list kosong yg di atas
        dict_of_bow[key] = dic
    # membuat matrix
    matrix_akhir = w4.matrix(list_of_bow) # jalankan fungsi matrix ke list_of_bow
    return dict_of_bow

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
    table = tfidf.TfIdf()
    for key,value in dict_document.items():
         table.add_document(key, value)

    return table.similarities(keyw)

def findSim(keyword,pathcorpus):
    return test_similarity(dob(pathcorpus),keyword)

# keyw = ['saya','yakin','dia','menolak','tembak','sebelum']
keyw = ['yang']
# print text_exam()
print test_similarity(dob(path),keyw)