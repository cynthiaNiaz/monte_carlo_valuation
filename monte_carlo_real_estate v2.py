import numpy as np
import matplotlib.pyplot as plt
from numpy.random import multivariate_normal

#Set Fixed Parameters
initial_price = 300000  #Initial Property Price
annual_rent = 2000 * 12 #Total Yearly Rent

#Simulation Parameters
years = 10  #Growth Period
num_simulations = 10000  #Number of Monte Carlo Simulations

#Set Parameters for Statstical Assumptions
rent_growth_mean = 0.02 #average annual rent growth rate (2%)
rent_growth_std = 0.01 #standard deviation in rent growth rate
interest_rate_mean = 0.03 #average annual interest rate (3%)
interest_rate_std = 0.005 #standard deviation in interest rate
tax_maintenance_rate = 0.01  #annual tax maintenece rate (1%)
vacancy_rate_mean = 0.05  #average vacancy rate (5%)
vacancy_rate_std = 0.02 #standard deviation in vacancy rate 

#The correlation matrix combines the interest rates and rent growth, making sure the variables are not simulated independently of one another. 
correlation_matrix = [[1, -0.8], [-0.8, 1]]  #Displays a strong negative correlation between interest rates and rent growth. Ex. If rates go up, growth goes down. Conversely, if rates go down, growth goes up.
correlated_means = [rent_growth_mean, interest_rate_mean] #connects the correlation to the variables
correlated_std_devs = [rent_growth_std, interest_rate_std] #connects the correlation to the variable standard deviations.

#Define the simulation. It performs a single simulation of property valuation over the fixed number of years. 
def simulate_property_valuation():
    #Generate a matrix of random samples and utilize the correlation matrix to define the relatonship between variables.
    samples = multivariate_normal(   
        correlated_means, #grabs the growth rate and interest rate mean values
        np.diag(correlated_std_devs) @ correlation_matrix @ np.diag(correlated_std_devs), #connects to the correlation matrix
        size=years #each year gets a pair of values (growth rate and interest rate)
    )
    rent_growth_samples, discount_rate_samples = samples.T #Seperate the variables into two arrays

    current_rent = annual_rent #Base Case - Initializes the rent for the first year
    cash_flows = [] #Empty list to store cash flows for each year

    for year in range(1, years + 1): #Inducive Step. Iterates through the number of years (1 to total number of years)
        vacancy_rate = np.random.normal(vacancy_rate_mean, vacancy_rate_std) #generates a value of the vacancy rate based on the given mean and standard deviations
        adjusted_rent = current_rent * (1 - vacancy_rate) #calculates income from rent adjusted for vacancy rate

        net_cash_flow = adjusted_rent - (initial_price * tax_maintenance_rate) #subtracts tax and maintence costs from income

        discount_rate = discount_rate_samples[year - 1] #grabs the discoount rate for the current year from the pre-generated samples
        present_value = net_cash_flow / (1 + discount_rate) ** year #discount the current cash flow to its present value
        cash_flows.append(present_value) #adds the present value of the cash flow for this year to this list of cash flows

        current_rent *= (1 + rent_growth_samples[year - 1]) #Updates the rent for the next year

    terminal_price_growth = rent_growth_samples[-1] #estimates the terminal property value by using last year's rent growth
    terminal_value = initial_price * (1 + terminal_price_growth) ** years #calculates the property's future value after compounding growth for all years
    discounted_terminal_value = terminal_value / (1 + discount_rate_samples[-1]) ** years  # Discount the terminal value to present value using the final year's discount rate

    return sum(cash_flows) + discounted_terminal_value #combines the discounted annualcash flows and the discounted terminal value to calculate total property valuation

#Performs the Monte Carlo Simulation
valuations = [simulate_property_valuation() for _ in range(num_simulations)] #runs the simulation as many times as stated in the simulation parameters section

#Calculates the Statistics
mean_valuation = np.mean(valuations) #average property valuation
confidence_interval = np.percentile(valuations, [2.5, 97.5]) #sets the confidence interval to 95% (-2.5 on both sides)
value_at_risk = np.percentile(valuations, 5) # Calculates the 5th percentile valuation, representing the worst 5% of outcomes

#Prints the results
print(f"Mean Valuation: ${mean_valuation:,.2f}") 
print(f"95% Confidence Interval: ${confidence_interval[0]:,.2f} to ${confidence_interval[1]:,.2f}")
print(f"Value at Risk (5%): ${value_at_risk:,.2f}")

#Graphs the Distribution
plt.hist(valuations, bins=30, alpha=0.75, edgecolor='k') #creates a histogram
plt.title("Distribution of Property Valuations") #title of the plot
plt.xlabel("Valuation ($)") #lable on x-axis
plt.ylabel("Frequency") #lable on y-axis
plt.axvline(mean_valuation, color='r', linestyle='dashed', linewidth=2, label="Mean Valuation") #Line for the Mean
plt.axvline(value_at_risk, color='g', linestyle='dashed', linewidth=2, label=f"VaR (5%): ${value_at_risk:,.0f}") #Line for the Value at Risk (VaR)
plt.legend() #show legend
plt.show() #display plot
