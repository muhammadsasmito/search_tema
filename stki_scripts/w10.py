import math, w3, w4, w6, os
from pprint import pprint
import tfidf

def dob():
    path = './text files'
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

def test_similarity():
    table = tfidf.TfIdf()
    table.add_document("foo", ["a", "b", "c", "d", "e", "f", "g", "h"])
    table.add_document("bar", ["a", "b", "c", "i", "j", "k"])
    table.add_document("baz", ["k", "l", "m", "n"])

    # self.assertEqual(
    print table.similarities(["a", "b", "c"])
    #     [["foo", 0.6875], ["bar", 0.75], ["baz", 0.0]])

# test_similarity()
# def tfidf(keywrd, dict_doc):
#     dic_dic = {}
#     # menampilkan data keyword di suatu doc
#     # for item in keywrd:
#     for doc, values in dict_doc.items():
#         ls_ls = []
#         ls_ls2 = []
#         # perulangan setiap dokumen
#         ls_ls1 = []
#         for key, value in values.items():
#             # perulangan setiap keyword
#             for item in keywrd:   
#                 # not in untuk menghilangkan duplikasi  
#                 if key == item and key not in ls_ls:
#                     # key sesuai dengan keyword dan belum pernah masuk ke ls_ls 
#                     ls_ls.append(key)
#                 elif item not in ls_ls:
#                     # not in untuk menghilangkan duplikasi
#                     # ls_ls2.append(item)
#                     ls_ls.append(item)
#         dic_dic[doc] = ls_ls
#     return dic_dic

keyw = ['saya','yakin','dia','menolak','tembak','sebelum']
print text_exam()
pprint(tfidf(keyw,text_exam()))