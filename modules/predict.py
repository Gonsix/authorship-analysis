import os
import numpy as np

# start からend までのIDの配列を返す
def extract_features(freq_vector, start=0, end=20):
    
    # # argsortを使用してインデックスの配列を取得
    sorted_indices = np.argsort(freq_vector)[::-1]
    return sorted_indices[start:end]



# return the score of how many types of pattern are appered in both vectors?
def get_similarity(feature_vector1,feature_vector2): 
    return len(set(feature_vector1) & set(feature_vector2))

def get_shared_list(feature_vector1, feature_vector2):
    return list(set(feature_vector1) & set(feature_vector2))


def predict(Q_df,K_df, target, _list=None):
    start = 0
    end = 20
    suspected = [author for author in K_df['author'] ]
    while(len(suspected) > 1):
        # os.system('clear')
        print('='*20 + f' Top {end} ' + '='*20)
        print("Suspected : ", end="")
        print(set(suspected))
        Q_features = extract_features(Q_df[target], start, end)
        similarityWithQ = {}
        
        if _list is not None: # words or pos_patterns
            print(f"Q  :", end="")
            for idx in Q_features:
                print(_list[idx], end=" | ")
        print("\n")

        # for author, reference_vector in zip(K_df['author'], K_df[target]):
        for i in range(len(K_df)):
            print()
            author = K_df.loc[i]['author']
            target_vector = K_df.loc[i][target]
            if author in suspected: #
                feature_vector = extract_features(target_vector,start, end)
                shared_list = get_shared_list(feature_vector, Q_features)
                score = len(shared_list)
                similarityWithQ[author]=len(shared_list)

                # if _list is not None: # words or pos_patterns
                print(f"{author} : ", end="")
                for idx in feature_vector:
                    print(_list[idx], end=" | ")
                print()
                
                print("Score :", score)
                print(f"Shared list Q-{author} : ", end="")
                for idx in shared_list:
                    print(_list[idx], end = " | ")
                print()

        print('-'*48)            

        # innocent_list に含まれない著者の中から1人を選ぶ

        innocent = min(similarityWithQ, key=similarityWithQ.get)
        if input(f'Do you want to rule out {innocent} in top {end} patterns ? (y/n) ') == 'y':
            suspected.remove(innocent)
        end += 20
    return suspected[0]
