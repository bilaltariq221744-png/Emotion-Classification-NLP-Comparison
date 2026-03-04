


    #-------- Preprocessing Module--------#

    

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def load_data(file_path):
    data = []
    labels = []

    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            text, label = line.strip().split(';')
            data.append(text)
            labels.append(label)

    return pd.DataFrame({'text': data, 'label': labels})


def encode_labels(train_df, val_df, test_df):
    encoder = LabelEncoder()

    train_df['label'] = encoder.fit_transform(train_df['label'])
    val_df['label'] = encoder.transform(val_df['label'])
    test_df['label'] = encoder.transform(test_df['label'])

    return train_df, val_df, test_df, encoder