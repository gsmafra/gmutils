from random import sample
from sys import exit

from numpy import argmax, empty, mean, mod, reshape

from listutils import indexes_matching, most_common, replicate_list, sub_list, unique_elements

def bag_of_frames(Y, F):

	# Inputs:
	#	Y			n-sized 1d-vector/list with classes for each frame
	#	F			n-sized 1d-vector/list with m files/classification targets for each frame
	#
	# Outputs:
	#	Y_vote		m-sized list containing the class for each file/classification target

	Y = list(Y)
	F = list(F)
	
	assert len(Y) == len(F)
	
	file_list = unique_elements(F)
	n_files = len(file_list)
	
	Y_vote = [None]*n_files
	for i in file_list:

		indexes = indexes_matching(F, i)
		Y_sub_i = sub_list(Y, indexes)
		
		Y_vote[i] = most_common(Y_sub_i)
		
	return Y_vote
	
	
def random_subsample(X, Y, k):

	n = len(Y)
	
	if n < k:
		print('Warning: specified number of sub-samples is smaller than the size of the sample')
		print('Number of samples: ' + str(n))
		print('Returning original data')
		return (X, Y)
	
	subsamp = sample(range(n), k)
	
	X_new = X[subsamp, :]
	Y_new = Y[subsamp]
	
	return (X_new, Y_new)


def segment_mean_subsample(X, Y, ratio=None, k=None):

	(n_frames, feat_size) = X.shape

	if not k is None:
		ratio = n_frames / k

	ratio = int(round(ratio))
	if not ratio > 1:
		print('Expected ratio higher than 1, returning original data')
		return (X, Y)

	# Cut ends to be divisible by ratio
	n_frames_subsample = n_frames / ratio
	n_frames_cut = n_frames_subsample * ratio
	X_cut = X[0:n_frames_cut, :]
	Y_cut = Y[0:n_frames_cut]
	
	# Reshape to 3d (divide in segments)
	X_3d = reshape(X_cut.T, (feat_size, n_frames_cut / ratio, ratio))

	# Mean of 3d object (means of segments)
	X_new = mean(X_3d, axis=2).T

	# Subsample labels
	Y_new = bag_of_frames(Y_cut, replicate_list(range(n_frames_subsample), ratio))

	return (X_new, Y_new)
	
