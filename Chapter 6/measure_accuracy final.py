import numpy as np
import pandas as pd
import matrix_factorization_utilities

# Load user ratings
raw_training_dataset_df = pd.read_csv(r'Chapter 6\movie_ratings_data_set_training.csv')
raw_testing_dataset_df = pd.read_csv(r'Chapter 6\movie_ratings_data_set_testing.csv')

# Convert the running list of user ratings into a matrix
ratings_training_df = pd.pivot_table(raw_training_dataset_df, index='user_id', columns='movie_id', aggfunc=np.max)
ratings_testing_df = pd.pivot_table(raw_testing_dataset_df, index='user_id', columns='movie_id', aggfunc=np.max)

# Apply matrix factorization to find the latent features
U, M = matrix_factorization_utilities.low_rank_matrix_factorization(ratings_training_df.as_matrix(),
                                                                    num_features=11,
                                                                    regularization_amount=1.1)

# Find all predicted ratings by multiplying U and M
predicted_ratings = np.matmul(U, M)

# Measure RMSE
rmse_training = matrix_factorization_utilities.RMSE(ratings_training_df.as_matrix(),
                                                    predicted_ratings)
rmse_testing = matrix_factorization_utilities.RMSE(ratings_testing_df.as_matrix(),
                                                   predicted_ratings)

print("Training RMSE: {}".format(rmse_training))
print("Testing RMSE: {}".format(rmse_testing))
