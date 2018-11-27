from recommend.models import Alcohol, History
from surprise import Reader, Dataset, KNNBasic, SVD
import pandas
import csv


def collaborative_filtering():
    history_list = History.objects.all()
    with open('recommend/dataset_cf.csv', 'w', encoding='utf-8', newline='') as csv_file:
        header = ['history_id', 'user_id', 'alco_name', 'data_joined', 'review']
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow(header)
        for history in history_list:
            row = []
            row += [history.history_id,
                    history.user_id,
                    history.alco_name,
                    history.data_joined,
                    history.review]
            writer.writerow(row)

    alco = pandas.read_csv("recommend/alcohol_cf.csv", encoding='utf-8')
    alco = alco.set_index('alco_name')

    data = pandas.read_csv("recommend/dataset_cf.csv", encoding='utf-8').fillna(0)
    data = data.drop('history_id', axis=1)
    data = data.drop('data_joined', axis=1)
    alcohol_id_list = []
    for i in range(len(data.index)):
        alcohol_id_list.append(alco.at[data['alco_name'][i], 'alcohol_id'])

    data = data.drop('alco_name', axis=1)
    data['alcohol_id'] = alcohol_id_list
    data = data.loc[:, ["user_id", "alcohol_id", "review"]]
    data.to_csv("recommend/dataset_cf.score", sep=' ', header=None, index=False, encoding='utf-8')

    reader = Reader(line_format='user item rating', sep=' ')
    dataset = Dataset.load_from_file("recommend/dataset_cf.score", reader=reader)
    trainset = dataset.build_full_trainset()
    sim_options = {
        'name': 'pearson',  # 類似度を計算する方法を指定（ cosine,msd,pearson,pearson_baseline ）
        'user_based': True  # False にするとアイテムベースに
    }
    algo = KNNBasic(k=5, min_k=1, sim_options=sim_options)
    algo.fit(trainset)
    # algo = SVD()
    # algo.train(trainset)
    # print(algo.sim)

    alcohol_num = Alcohol.objects.latest('alcohol_id').alcohol_id
    user_num = History.objects.latest('user_id').user_id

    with open('recommend/answer_cf.csv', 'w', encoding='utf-8', newline='') as csv_file:
        header = ['user_id', 'alcohol_id', 'predicted_value']
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow(header)
        for j in range(1, user_num + 1):
            user_id = j
            for i in range(1, alcohol_num + 1):
                item_id = i
                pred = algo.predict(uid=str(user_id), iid=str(item_id))
                row = []
                row += [pred.uid,
                        pred.iid,
                        pred.est]
                writer.writerow(row)
