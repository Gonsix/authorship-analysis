def count_pos_patterns(documents, window_size=3):
    width = window_size
    pos_patterns = []
    pos_freq_vectors = [[] for _ in range(len(documents))]
    for docId, document in enumerate(documents):
        len_doc = len(document)
        for i in range(len_doc - (width-1)):
            key_str = ""
            key_str += document[i][0] # word

            for j in range(1, width):
                key_str += " " + document[i+j][1] # POS

            if key_str not in pos_patterns:
                pos_patterns.append(key_str)
                # パターンが現れたドキュメント -> 1 , それ以外　-> 0
                for i in range(len(pos_freq_vectors)): # loop for K1, K2, Q
                    if i == docId:
                        pos_freq_vectors[i].append(1)
                    else:
                        pos_freq_vectors[i].append(0)

            else: 
                idx = pos_patterns.index(key_str)
                pos_freq_vectors[docId][idx] += 1

    return (pos_patterns, pos_freq_vectors)
            