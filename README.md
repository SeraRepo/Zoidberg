# Project Zoidberg

The goal of this project is to, given some X-ray images, use machine learning to help doctors detecting pneumonia.
We have access to 3 datasets available [here](https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia).

**We must:**

- use a train-validation-test procedure
- use a cross validation procedure,
- compare our results with a simple train test split,
- use one of the datasets to tune our algorithms.

**We deliver:**

- a technical documents:
a Jupyter notebook-like file, containing code and text, possibly graphics and an html-file to prove our results without rerunning the code
[notebook](/zoidberg.ipynb)
- a synthesis document:
a pdf file to sum up our results and figures
[pdf](/zoidberg.pdf)

We choose to use the following Machine Learning (ML) algorithm:

- k-Nearest Neighbors ([KNN](https://scikit-learn.org/stable/modules/neighbors.html))
- Support Vector Machine ([SVM](https://scikit-learn.org/stable/modules/svm.html))
- Naive Bayes ([NB](https://scikit-learn.org/stable/modules/naive_bayes.html))
- Convolutionnal Neural Network ([CNN](https://en.wikipedia.org/wiki/Convolutional_neural_network) with keras (tensorflow))
