import pandas as pd
import os


def create_dataframe():
    df01 = pd.DataFrame(columns=['name', 'class0', 'class2', 'class3', 'class4', 'class5'])
    return df01


def main(path, df01):
    for r, d, f in os.walk(path):
        if 'l01/p04' in r:
            for file in f:
                if 'attentive.csv' in file or 'inattentive.csv' in file:
                    new_path = os.path.join(r, file)
                    files = pd.read_csv(new_path)
                    df = files['endTime'] - files['startTime']
                    df = pd.concat([df, files['classification']], axis=1)
                    name = r.split('/')[6]
                    new_df = df.groupby(['classification'], as_index=False).sum()
                    daf_col = ['name', 'class0', 'class2', 'class3', 'class4', 'class5']
                    index = {'name': 0, 'class0': 1, 'class2': 2, 'class3': 3, 'class4': 4, 'class5': 5}
                    data = [[name, 0, 0, 0, 0, 0]]
                    for i in range(len(new_df['classification'])):
                        class_index = new_df['classification'][i]
                        if class_index == 1:
                            continue
                        val = new_df[0][i]
                        data[0][index['class' + str(class_index)]] = val
                    df1 = pd.DataFrame(data=data, index=[1], columns=daf_col)
                    df01 = df01.append(df1.iloc[[0]], ignore_index=True)
    df01 = df01.groupby(['name'], as_index=False).sum()
    df01.to_csv('result.csv', index=False)


df01 = create_dataframe()
main('/media/maqitian/sda1/data_process/20211228', df01)
