import numpy as np
from scipy.stats import norm
from sklearn.mixture import GaussianMixture

class GMM:
    def pdf(self, x, wgt, mu, sigma):
        """
        probability density function for the gaussian mixture
        """
        # Converting arguments to numpy arrays
        x = np.atleast_1d(x)[:, None]  # to check that x is a column vector
        wgt = np.asarray(wgt)
        mu = np.asarray(mu)
        sigma = np.asarray(sigma)

        # Checking that all weights sum to 1
        if not np.isclose(np.sum(wgt), 1):
            raise ValueError("Weights must sum to 1.")
        
        # Calculating the pdf using stats.norm and summing it up for GMM pdf
        pdf = np.sum(wgt * norm.pdf(x, loc = mu, scale = sigma), axis=1)
        
        return pdf

    def cdf(self, x, wgt, mu, sigma):
        """
        cumulative density function for the gaussian mixture
        """
        # Converting arguments to numpy arrays
        x = np.atleast_1d(x)[:, None]  # to check that x is a column vector
        wgt = np.asarray(wgt)
        mu = np.asarray(mu)
        sigma = np.asarray(sigma)

        # Checking that all weights sum to 1
        if not np.isclose(np.sum(wgt), 1):
            raise ValueError("Weights must sum to 1.")

        # Calculating the cdf using stats.norm and summing it up for GMM pdf
        cdf = np.sum(wgt * norm.cdf(x, loc = mu, scale = sigma), axis=1)
        
        return cdf

    def rvs(self, wgt, mu, sigma, size=None, random_state=None):
        """
        Generate random variables from the gmm
        """
        # have to set the size to 1 if not specified as per instructions
        size = 1 if size is None else size
        
        # converting to numpy arrays
        wgt = np.asarray(wgt)
        mu = np.asarray(mu)
        sigma = np.asarray(sigma)

        # setting the default random state if not specified
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
    # Testing the gmm file
    np.random.seed(42)
    data = np.concatenate([
        np.random.normal(loc=-2, scale=0.5, size=300),
        np.random.normal(loc=3, scale=1.0, size=700)
    ])

    # instantiating the object and fit the model with k as 2
    gaussmix = GMM()
    weights, means, sigmas = gaussmix.fit(data, k = 2)

    print("Weights:", weights)
    print("Means:", means)
    print("Sigmas:", sigmas)

    # evaluating PDF and CDF at some points
    x = np.linspace(-5, 5, 100)
    pdf_vals = gaussmix.pdf(x, weights, means, sigmas)
    cdf_vals = gaussmix.cdf(x, weights, means, sigmas)

    print("PDF values:", pdf_vals)
    print("CDF values:", cdf_vals)

    # generating random samples
    samples = gaussmix.rvs(weights, means, sigmas, size = 10)
    print("Generated samples:", samples)