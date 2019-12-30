# Bioinformatics-Project
Feature (Gene) Selection Project for Bioinformatics

* DLBCL Dataset (Shipp, et al., 2002)
* Lung Cancer Dataset (Gordon, et al., 2002)
* Prostate Cancer Dataset (Singh, et al., 2002)
* Myeloma Cancer Dataset (Tian, et al., 2002)

1. Import the libraries first! DLBCL dataset is available here, and other libraries can be accessed through this link: 
   https://drive.google.com/open?id=1UmXzApJ2nGdpCh7-JenxpfCgMlP_RPbS
2. Make sure that the datasets are in the correct directory!
3. Type the name of the dataset you want to apply feature selection!
  3.1. You have 4 options: 'gordon' for lung cancer, 'shipp' for dlbcl, 'singh' for prostate, 'tian' for myeloma
  3.2. Note that the experimental results are based on dlbcl dataset.
4. There are 6 different classifiers and the best one for the given dataset is automatically selected!
  4.1. SVM (Support Vector Machine)
  4.2. Non-Linear SVM (Support Vector Machine)
  4.3. K-NN (K-Nearest Neighbor)
  4.4. NN (Neural Network)
  4.5. D-Tree (Decision Tree)
  4.6. R-Forest (Random Forest)
5. After selection of the best classifier, run NSGA-II to see the results.
  5.1. The results are printed at every generation.
  5.2. The results include the solution (i.e. [1, 0, 1, 0, 1, 1, ..., 1]), the fitness values for the first objective which is number of features (i.e. 25) and the fitness values for the second objective which is classification accuracy (i.e. 0.9394).  
  5.3 The selected features are equal to 1 and vice versa.
  5.4. At the end, the figure will be shown, in which the pareto-frontier with best optimal solutions (note that there can be multiple optimal solutions) is drawn.
6. Please, ask questions/points you may not understand. We will be available to answer as soon as possible!
