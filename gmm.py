'''
- contains the implementation of GMM wrt scipy
- creating subclass of rv_continuous provided in scipy.stats
- override the functions that are mentioned right now
- argcheck should check that all wgt are +ve and sum to 1
- wgt, mu and sigma are params to GMM
- pdf, cdf should allow x to be vector
- can use fit function in sklearn.mixture class GaussianMixture (k in fit is no. of components in mixture model)
- wgt, mu and sigma are coulmn vectors and x is a row vector
- wrap the testing code (meaning that it should not run if this script is used in another file)
- rvs: generate RVs from a GMM
    - todo for each RV: sample what mixture to use by sampling an index from wgt vector
    - sample a Gaussian RV using this index with corresponding mu and sigma
'''

from scipy.stats import rv_continuous

class gmm(rv_continuous):
    def _argcheck(self, wgt, mu, sigma):

        pass

    def _pdf(self, x, wgt, mu, sigma):
        pass

    def _cdf(self, x, wgt, mu, sigma):
        pass

    def _rvs(self, wgt, mu, sigma, size=None, random_state=None):
        pass

    def fit(self, data, k):
        pass
