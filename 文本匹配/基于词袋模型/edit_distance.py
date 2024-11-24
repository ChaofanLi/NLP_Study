import numpy as np
#编辑距离
def edit_distance(string1,string2):
    matrix =np.zeros((len(string1)+1,len(string2)+1)) 
    for i in range(len(string1)+1): 
        matrix[i][0]=i
    for j in range(len(string2)+1): 
        matrix[0][j]=j
    for i in range(1,len(string1)+1):
        for j in range(1,len(string2)+1):
            if string1[i-1]==string2[j-1]:
                d =0
            else:
                d =1
            matrix[i][j]=min(matrix[i-1][j]+1,matrix[i][j-1]+1,matrix[i-1][j-1]+d) 
    return matrix[len(string1)][len(string2)]
 #基于编辑距离的相似度
def similarity_based_on_edit_distance(string1,string2): 
    return 1 -edit_distance(string1,string2)/max(len(string1),len(string2))

if __name__=="__main__":
    string1="我爱北京天安门"
    string2="谁能不爱北京天安门"
    print(similarity_based_on_edit_distance(string1,string2))
