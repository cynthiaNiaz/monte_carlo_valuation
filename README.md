# Monte Carlo Simulation for Real Estate Valuation

## About  

This project is a Python-based Monte Carlo simulation designed to estimate property values over a longer-term horizon, like 10 years. It takes into account key factors such as rent growth, interest rates, vacancy rates, taxes, and maintenance costs. These factors are all interconnected (e.g., rising interest rates can slow rent growth), and the simulation reflects those relationships.

---

## Features  

- **Key Variables Modeled**:  
    - Rent Growth  
    - Interest Rates  
    - Vacancy Rates  
    - Taxes and Maintenance Costs  

- **Outputs**:  
    - Average Valuation  
    - 95% Confidence Interval  
    - Value at Risk (5%)  
    - Histogram of the Valuation Distribution  

- Simulates correlations between variables, like how changes in growth and interest rates might interact.

---

## How It Works  

The simulation generates correlated samples for variables (like rent growth and interest rates) using a multivariate normal distribution. Annual cash flows are adjusted for things like vacancy and maintenance costs, then discounted to their present value. Running thousands of iterations creates a full valuation distribution to account for uncertainty.

---

## How to Run

1. **Clone the Repository**:
   - Use the following command to clone this repository to your local machine:
     ```bash
     git clone https://github.com/your-username/monte-carlo-valuation.git
     cd monte-carlo-valuation
     ```

2. **Install Required Libraries**:
   - Make sure the required Python libraries are installed:
     ```bash
     pip install numpy matplotlib
     ```

3. **Run the Simulation**:
   - Execute the script using Python:
     ```bash
     python property_valuation.py
     ```

4. **Customize Parameters**:
   - You can customize variables like `years`, `initial_price`, or `num_simulations` by editing the script directly or adding a configuration file.

5. **View the Results**:
   - The script will output statistics (e.g., mean valuation, confidence intervals) to the terminal and generate visualizations (e.g., histograms) for detailed analysis.

---

## Example Output  

Running the simulation produces the following results:  
Mean Valuation: $460,665.82
95% Confidence Interval: $391,522.02 to $544,129.55
Value at Risk (5%): $400,841.22

---

## Sample Visualization  

The histogram below shows the distribution of simulated property valuations (refer to valuation-distribution file):

![Valuation Distribution](images/valuation_distribution.png)

---

## Why I Built This  

Real estate markets are unpredictable, and I wanted to create a tool to make "what-if" scenarios easier to understand. As someone who enjoys Python programming and financial modeling, this felt like a fun way to experiment and learn more about both areas.

---

## Customization  

You can adjust parameters like:  
- Investment period (years)  
- Initial property price  
- Annual rent  
- Growth rates, interest rates, and other statistical assumptions  

You can also tweak the number of simulations for precision vs. performance.

---

## Applications  

This tool could be useful if you’re:  
- Considering real estate investments  
- Interested in financial modeling  
- Curious about Monte Carlo simulations and risk assessment  

---

## Contact  

If you have questions or ideas for improvement, feel free to reach out!

---

## License

This project is licensed under the MIT license. See the License file for details.
