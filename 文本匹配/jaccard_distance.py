#jaccard距离
def jaccard_distance(string1,string2): 
    return 1-len(set(string1) & set(string2))/len(set(string1) | set(string2))
#基于jaccard相似度
def similarity_based_on_jaccard_distance(string1,string2): 
    return 1-jaccard_distance(string1,string2)

if __name__=="__main__":
    string1="我爱北京天安门"
    string2="谁能不爱北京天安门"
    print(similarity_based_on_jaccard_distance(string1,string2))