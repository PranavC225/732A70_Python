import sys
from gmm import GMM
import numpy as np

def calc_llh(data, wgt, mu, sigma):
    """
    calculating the loglikelihood of the data using pdfs of gmm
    """
    gmm = GMM()
    pdf = gmm.pdf(data, wgt, mu, sigma)

    if np.any(pdf <= 0):  # Prevent negative pdf
        raise ValueError("PDF values must be strictly positive to calculate log-likelihood.")

    return np.sum(np.log(pdf))

def calc_AIC(data, wgt, mu, sigma):
    """
    calculating the AIC
    """
    llh = calc_llh(data, wgt, mu, sigma)
    k = len(wgt) + len(mu) + len(sigma) # getting number of parameters
    return 2 * (k - llh)

def string_to_number(string):
    """
    converts string to numbers and eventually numpy array
    """
    numbers = [float(value) for value in string.split(',')]
    return np.array(numbers)

def main(file):
    """
    function to process the data file and get the best AIC value
    """
    # read file
    with open(file, 'r') as f:
        data_string = f.read().strip()

    # convert to number array
    data = string_to_number(data_string)

    best_aic = float('inf')
    best_model = None

    print("Fitting models for k = 2 to k = 10")
    for i in range(2, 11):
        gmm = GMM()
        weights, means, sigmas = gmm.fit(data, i)
        aic = calc_AIC(data, weights, means, sigmas)
        log_likelihood = calc_llh(data, weights, means, sigmas)
        
        print(f"K={i}, Log-Likelihood={log_likelihood:.2f}, AIC={aic:.2f}")

        # Update best model if this model has the lowest AIC
        if aic < best_aic:
            best_aic = aic
            best_model = (i, weights, means, sigmas)

    # Output the best model
    K, weights, means, sigmas = best_model
    print("\nBest Model:")
    print(f"Number of components: {K}")
    print(f"Weights: {weights}")
    print(f"Means: {means}")
    print(f"Standard deviations: {sigmas}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Correct command: python analyze.py data_file.csv")
        sys.exit(1)

    file_name = sys.argv[1]
    main(file_name)
