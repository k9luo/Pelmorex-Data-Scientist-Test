from sklearn.feature_selection import mutual_info_classif
from sklearn.preprocessing import LabelEncoder

def fill_nan(df, column):
    df[column] = df[column].fillna('unknown_' + column)


def calculate_mutual_information(df, feature_column_name, target_column_name):
    le = LabelEncoder()
    le.fit(df[feature_column_name])
#    le.classes_
    res = le.transform(df[feature_column_name])
    res = res.reshape(-1, 1)

    mi = mutual_info_classif(res, df[target_column_name].to_numpy(), discrete_features=True)[0]
    return mi
#    mis.append((mi, column))
