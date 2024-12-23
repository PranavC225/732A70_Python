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

for arg in sys.argv:
    print(arg)