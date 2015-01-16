#Logistic Regression

#Import necessary libraries
DIR_PATH = "F:\Educational Stuff\Hebi\Machine Learning and Data Science\Machine Learning\Machine Learning Algorithm-My Work\Machine Learning-Andrw.Ng Exercises\Exercise 2\mlclass-ex2/"
import scipy.optimize, scipy.special
from numpy import *
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn import datasets, linear_model
#-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

def main():
	data = genfromtxt(DIR_PATH+'ex2data1.txt',delimiter = ',') # Get Data from dataset
	m, n = shape(data)[0], shape(data)[1]-1
	X = data[ : ,:n]
	y = data[ : ,n:n+1]

	logreg = linear_model.LogisticRegression() #Creat :Logget object
	logreg.fit(X, y.flatten()) # Fit data
	
	print logreg.intercept_[0] 
	print logreg.coef_[0]
	
	#Test Data
	test = array([60.18259938620976,86.30855209546826])
	print logreg.predict(test)

	# Now Enough of testing ,lets Plot the data
	# First Separate Positive and Negative data and plot the data
	pos = data[data[ : ,2]==1] #Positive Datasets
	neg = data[data[ : ,2]==0] #Negative Datasets

	plt.xlabel('Exam 1 Score')
	plt.ylabel('Exam 2 Score')
	plt.title('Training data of Exam Score')
	plt.xlim(25,115)
	plt.ylim(25,115)
	plt.scatter(pos[:,0],pos[:,1],c= 'b', marker='+', s=40,linewidth=1,label='Admitted')
	plt.scatter(neg[:,0],neg[:,1],c='y', marker='o', s=40,linewidth=1,label='Not Admitted')
	plt.legend()

	# Appologies No idea how to plot the boundry but will update soon as I found the solution
	h =.02
	xx, yy = meshgrid(arange(data[:,0].min(), data[:,0].max(),h), arange(data[:,1].min(), data[:,1].max(),h))
	

	z = logreg.decision_function(c_[xx.ravel(), yy.ravel()])
	z = z.reshape(xx.shape)
	print z.shape
	
	plt.imshow(z, interpolation='nearest', extent=(xx.min(), xx.max(), yy.min(), yy.max()), aspect='auto', origin='lower', cmap=plt.cm.PuOr_r)
	contours = plt.contour(xx, yy, z, levels=[0], linewidths=2, linetypes='--')

	plt.xticks(())
	plt.yticks(())
	plt.show()
	plt.close()

if __name__ == '__main__':
	main()