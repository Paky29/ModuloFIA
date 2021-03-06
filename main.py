import os
import numpy as np
import pandas as pd
from lightfm import cross_validation
from scipy.sparse import csr_matrix

from model.model import define_features, create_model, evaluate_model, recommend_user, dizionario_user, \
    dizionario_item, define_interaction_table, recommend_unknown_user
from utility.manageModel import store_model
from utility.preprocessing import books_with_ratings
from utility.visualization import create_rating_hist, variation_epochs

if __name__ == '__main__':
    # create_gender()
    # users, books, ratings=pre_process(25, 300)
    datapath = os.path.join("dataset\\dataset_processati", "")
    users = pd.read_csv(datapath + "UsersProcessati.csv")
    books = pd.read_csv(datapath + "BooksProcessati.csv")
    ratings = pd.read_csv(datapath + "RatingsProcessati.csv")

    books_selected = books_with_ratings(books, ratings)
    user_f, item_f, interactions, weights = define_features(users, books_selected, ratings)
    interactions_table = define_interaction_table(ratings)

    train, test = cross_validation.random_train_test_split(interactions, test_percentage=0.30,
                                                           random_state=np.random.RandomState(seed=1))
    train_weights, test_weights = cross_validation.random_train_test_split(weights, test_percentage=0.30,
                                                                           random_state=np.random.RandomState(seed=1))

    model = create_model(train, train_weights, user_f, item_f)
    store_model(model, "modello.sav")
    variation_epochs(train, train_weights, test, item_f, user_f)
    prec, auc = evaluate_model(model, train, test, user_f, item_f)
    print(prec)
    print(auc)

    item_dict = dizionario_item(books)
    user_id, user_dict = dizionario_user(interactions_table)

    recommend_user(model, interactions_table, user_id[1], user_dict, item_dict, user_f, item_f)

    user_feature_list = [['18', 'M']]
    new_user = pd.DataFrame(user_feature_list, columns=['age', 'gender'])
    new_user_selected = pd.get_dummies(new_user, columns=['age', 'gender'])
    new_user_selected = new_user_selected.reset_index().drop('index', axis=1)
    users_metadata_csr = csr_matrix(new_user_selected.values)

    recommend_unknown_user(model, interactions_table, item_dict, users_metadata_csr, item_f)