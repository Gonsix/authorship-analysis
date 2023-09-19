# Keyness
import math
from modules.load_data import DocID

def keyness(tf_vector1, ref_tf_vector2, effort='log-ratio'): # freq_vector1 and freq_vector2 are both already normalized

    keyness_vec = []

    
    def log_ratio(freq1, size1, freq2, size2): 
            freq1_norm = freq1/size1 * 1000000
            freq2_norm = freq2/size2 * 1000000
            try:
                value = math.log2(freq1_norm/freq2_norm)
            except:
                print(f"Error Here: freq1_norm={freq1_norm}, size1={size1}, freq2_norm={freq2_norm}, size2={size2}")
            return value
        
    def perc_diff(freq1, size1, freq2, size2):
        freq1_norm = freq1/size1 * 1000000
        freq2_norm = freq2/size2 * 1000000
        value = ((freq1_norm - freq2_norm) * 100)/freq2_norm
        return value
    
    def odds_ratio(freq1, size1, freq2, size2):

        if size1 - freq1 == 0: 
            size1 += 1
        if size2 - freq2 == 0:
            size2 += 1
        value = (freq1/(size1-freq1)) / (freq2/(size2-freq2))
        return value
    
    
    for i, x in enumerate(tf_vector1):
        
        # we change the tiny number if the value is zero, this is because zeros will cause problems
        freq1 = tf_vector1[i]
        size1 = sum(tf_vector1)
        freq2 = ref_tf_vector2[i]
        size2 = sum(ref_tf_vector2)

        if freq1 == 0:
            freq1 = 0.00000001
        if freq2 == 0:
            freq2 = 0.00000001

        if effort == 'log-ratio':
            value = log_ratio(freq1, size1, freq2, size2)
        elif effort == '%diff':
            value = perc_diff(freq1, size1, freq2, size2)
        elif effort == 'odds-ratio':
            value = odds_ratio(freq1, size1, freq2, size2)

        keyness_vec.append(value)

    return keyness_vec


def create_keyness_col(df, effort='log-ratio'):
    # create keyness col
    keyness_mat = []
    for tf_vector in df['tf']:
        tf_ref = df['tf'][DocID.R]
        keyness_vec = keyness(tf_vector, tf_ref, effort=effort)
        keyness_mat.append(keyness_vec)

    # keyness を　Dataframe に追加
    df['keyness'] = keyness_mat
