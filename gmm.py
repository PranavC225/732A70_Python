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

import numpy as np
import math
from scipy.stats import norm
from sklearn.mixture import GaussianMixture

class GMM:
    def pdf(self, x, wgt, mu, sigma):
        """
        probability density function for the gaussian mixture
        """
        x = np.atleast_1d(x)[:, None]  #to check that x is a column vector
        wgt = np.asarray(wgt)
        mu = np.asarray(mu)
        sigma = np.asarray(sigma)

        if not np.isclose(np.sum(wgt), 1):
            raise ValueError("Weights must sum to 1.")
        
        # pdf = 0
        pdf = np.sum(wgt * norm.pdf(x, loc = mu, scale = sigma), axis=1)
        # for i in range(len(wgt)):
        #     pdf += wgt[i] * ((1/math.sqrt(2 * math.pi * sigma[i]**2)) * math.exp(-(x - mu[i])**2 / (2 * sigma[i] ** 2)))
        
        return pdf

    def cdf(self, x, wgt, mu, sigma):
        """
        cumulative density function for the gaussian mixture
        """
        x = np.atleast_1d(x)[:, None]  #to check that x is a column vector
        wgt = np.asarray(wgt)
        mu = np.asarray(mu)
        sigma = np.asarray(sigma)
        cdf = np.sum(wgt * norm.cdf(x, loc = mu, scale = sigma), axis=1)
        
        return cdf

    def rvs(self, wgt, mu, sigma, size=None, random_state=None):
        """
        Generate random variables from the gmm
        """
        size = 1 if size is None else size
        wgt = np.asarray(wgt)
        mu = np.asarray(mu)
        sigma = np.asarray(sigma)
        random_state = random_state if random_state else np.random.default_rng()

        # to sample mixture component indices based on weights index
        component_indices = random_state.choice(len(wgt), size = size, p = wgt)
        
        # Generate rv samples from the selected gaussian components
        rvs = random_state.normal(loc = mu[component_indices], scale = sigma[component_indices])
        
        return rvs

    def fit(self, data, k):
        """
        fit using sklearn gaussian mixture
        """
        gaussmix = GaussianMixture(n_components = k, random_state = 0)
        gaussmix.fit(data.reshape(-1, 1))

        weights = gaussmix.weights_
        means = gaussmix.means_.flatten()
        covariances = gaussmix.covariances_.flatten()
        
        return weights, means, np.sqrt(covariances)


if __name__ == "__main__":
    # Testing
    np.random.seed(42)
    data = np.concatenate([
        np.random.normal(loc=-2, scale=0.5, size=300),
        np.random.normal(loc=3, scale=1.0, size=700)
    ])

    # Instantiate and fit the model
    gaussmix = GMM()
    weights, means, sigmas = gaussmix.fit(data, k=2)

    print("Weights:", weights)
    print("Means:", means)
    print("Sigmas:", sigmas)

    # Evaluate PDF and CDF at some points
    x = np.linspace(-5, 5, 100)
    pdf_vals = gaussmix.pdf(x, weights, means, sigmas)
    cdf_vals = gaussmix.cdf(x, weights, means, sigmas)

    print("PDF values:", pdf_vals)
    print("CDF values:", cdf_vals)

    # Generate random samples
    samples = gaussmix.rvs(weights, means, sigmas, size=10)
    print("Generated samples:", samples)