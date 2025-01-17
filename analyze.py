'''
- contains a py program reading a file and processes the content of the file
- ensures checking of csv and values as numbers
- should fit GMM for various number of mixtures form k = 2 to 10
- prints loglikelihood of data from these models and choose best AIC - (https://en.wikipedia.org/wiki/Akaike_information_criterion)
- prints text containing the chosen number of components and all parameters
- should run using "python analyze.py data_file.csv"
- functions to be implemented:
    - calc_llh(data, wgt, mu, sigma) - calculates loglikelihood
    - calc_AIC(data, wgt, mu, sigma) - calcuclates the AIC value
    - string_to_number(string) - takes the text string, splits on ',', converts everything to numbers and returns in a numpy array
- to pass the data file as argument, we need to import sys in the file: test using 'python analyze.py hello this is some arguments'
'''

import sys
from gmm import GMM
import numpy as np

def calc_llh(data, wgt, mu, sigma):
    """
    calculating the loglikelihood of the data using pdfs of gmm
    """
    gmm = GMM()
    pdf = gmm.pdf(data, wgt, mu, sigma)

    if np.any(pdf <= 0):  # Prevent log(0) issues
        raise ValueError("PDF values must be strictly positive to calculate log-likelihood.")

    return np.sum(np.log(pdf))

def calc_AIC(data, wgt, mu, sigma):
    """
    calculating the AIC
    """
    llh = calc_llh(data, wgt, mu, sigma)
    k = len(wgt) + len(mu) + len(sigma) #getting number of parameters
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
    #read file
    with open(file, 'r') as f:
        data_string = f.read().strip()

    #convert to number array
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
