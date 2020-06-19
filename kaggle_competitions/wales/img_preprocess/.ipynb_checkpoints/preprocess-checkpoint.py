from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
import pandas as pd
import numpy as np

def scale_data(data,div_by):
    scales_data = list(map(lambda x: x/div_by , data))
    return scales_data

def prepare_labels_string_to_onehot(data, label_name):
    """
    get 1d arrays of categorical strings -> return onehot matrix with shape len(labels) * unique values in labels
    """
    values = np.array(data[label_name])
    label_encoder = LabelEncoder()
    integer_encoded = label_encoder.fit_transform(values)
    # print(integer_encoded)

    onehot_encoder = OneHotEncoder(sparse=False)
    integer_encoded = integer_encoded.reshape(len(integer_encoded), 1)
    onehot_encoded = onehot_encoder.fit_transform(integer_encoded)
    # print(onehot_encoded)

    y = onehot_encoded
    
    #keep names in the correct order
    
    data['label_encode'] = label_encoder.fit_transform(data[label_name])
    keep_names_ordered = data[['label_encode', label_name]].drop_duplicates().sort_values(by='label_encode')
    
    y = pd.DataFrame(y)
    y.columns = keep_names_ordered['Id']
    
    return y, label_encoder

    