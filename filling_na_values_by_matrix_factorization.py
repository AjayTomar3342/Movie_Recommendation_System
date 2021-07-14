# import numpy as np
# import pandas as pd
#
# #Class to fill na values in user-movie matrix with predicted ratings by users for users which aren't predicted yet
# class matrix_factorization():
#
#     #Initializing various values to be used in the prediction part. R stands for user-movie matrix, K is the number of latent features,
#     #Alpha and beta help in gradient descent which helps to find the optimized P and Q matrix which are multiplied with diagonal matrix
#     #to find predicted na values in the original user-movie matrix. Iterations indicate the number of times gradient descent algorithm
#     #will run to find optimized P and Q matrices.
#     def __init__(self, R, K, alpha, beta, iterations):
#         print("First")
#         self.R = R
#         self.num_users,self.num_items = R.shape
#         self.K = K
#         self.alpha = alpha
#         self.beta = beta
#         self.iterations = iterations
#
#     def train(self):
#         #Initizalizing user-feature matrix P
#         print("2nd")
#         self.P = np.random.normal(scale=1./self.K, size=(self.num_users, self.K))
#         #Initializing item-feature matrix Q
#         self.Q = np.random.normal(scale=1./self.K, size=(self.num_items, self.K))
#
#         # Initializing the bias terms. These will be used for gradient descent to get optimized P and Q matrices
#         self.b_u = np.zeros(self.num_users)
#         self.b_i = np.zeros(self.num_items)
#         self.b = np.mean(self.R[np.where(self.R != 0)])
#
#         # List of training samples
#         self.samples = [
#         (i, j, self.R[i, j])
#         for i in range(self.num_users)
#         for j in range(self.num_items)
#         if self.R[i, j] > 0
#         ]
#
#         # Stochastic gradient descent for given number of iterations
#         training_process = []
#         for i in range(self.iterations):
#             np.random.shuffle(self.samples)     #Randomly take training samples
#             self.sgd()                          #Use sgd to find optimized P and Q
#             mse = self.mse()                    #Calculate error per training sample
#             training_process.append((i, mse))
#         if (i+1) % 20 == 0:
#             print("Iteration: %d ; error = %.4f" % (i+1, mse))
#
#         return training_process
#
#     # Computing total mean squared error
#     def mse(self):
#         print("3rd")
#         xs, ys = self.R.nonzero()
#         predicted = self.full_matrix()
#         error = 0
#         for x, y in zip(xs, ys):
#             error += pow(self.R[x, y] - predicted[x, y], 2)
#         return np.sqrt(error)
#
#     # Stochastic gradient descent to get optimized P and Q matrix
#     def sgd(self):
#         print("4rth")
#         for i, j, r in self.samples:
#             prediction = self.get_rating(i, j)
#             e = (r - prediction)
#
#             self.b_u[i] += self.alpha * (e - self.beta * self.b_u[i])
#             self.b_i[j] += self.alpha * (e - self.beta * self.b_i[j])
#
#             self.P[i, :] += self.alpha * (e * self.Q[j, :] - self.beta * self.P[i,:])
#             self.Q[j, :] += self.alpha * (e * self.P[i, :] - self.beta * self.Q[j,:])
#
#     # Ratings for user i and movie j
#     def get_rating(self, i, j):
#         print("5th")
#         prediction = self.b + self.b_u[i] + self.b_i[j] + self.P[i, :].dot(self.Q[j, :].T)
#         return prediction
#
#     # Full user-movie rating matrix
#     def full_matrix(self):
#         print("6th")
#         return mf.b + mf.b_u[:,np.newaxis] + mf.b_i[np.newaxis:,] + mf.P.dot(mf.Q.T)
#
#     #In-Case, a new user gets added to the movie rating system, the only change has to be done in the user-feature relevance matrix P.
#     #Similarly, in case of a new item addition in the movie rating system, only change is to be done in item-feature relevance matrix Q
#
# #Read in file to be filled with matrix factorization
# input = pd.read_csv("input_data/file_for_matrix_factorization.csv")
# input=input.to_numpy()
#
# mf = matrix_factorization(input, K=20, alpha=0.001, beta=0.01, iterations=1)
# training_process = mf.train()
# print(" ")
# print("P x Q:")
# print(mf.full_matrix())
# print(" ")
#
# def full_matrix():
#     finished_matrix=mf.full_matrix()
#     return finished_matrix
#
