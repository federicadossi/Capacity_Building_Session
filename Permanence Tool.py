# CARBON PLAN PERMANENCE CALCULATOR (basically a rent vs buy calculator): https://carbonplan.org/research/permanence-calculator
# This script allows to compare the permanence-adjusted costs of different carbon removal strategies based on a set of input parameters.
# The core calculation is the net present value of a series of carbon removal decisions over a 1000-year period.

# %%  import packages
import numpy as np

# %% Define parameters

# project duration (years)
d = 10

# switching time (years) p.s. t_switch=1000 when permanent technology is not used
t_switch = 50

# discount rate
disc_rate = 0.03

# yearly probability of project failure
risk_failure = 0.1

# temporary initial costs (dollars per ton of CO2)
Cszero = 20

# rate of increase impermanent prospect
h = 0

# function for price of temporary credits
# Cs  = Cszero + h * (t_switch - d*i)

# number of times projects needs to be repeated
z = t_switch // d  # integer division

# permanent initial costs (dollars per ton of CO2)
Cpzero = 500

# rate of increase permanent prospect
g = 0

# function for price of permanent credits at time of the switch
Cp = Cpzero + g * t_switch

# %% initialize variables to track payments and project failure

NPV_beforeswitch = 0
NPV_final = 0
paid = np.zeros(t_switch+1) # +1 is necessary to access the index t_switch, otherwise py stops at t_switch-1 because indexing starts at 49

NPVs_final_array = np.zeros(51)  # initialize array to store NPV_final values

for k in range(1, 51):  # repeat the model 50 times

    # loop used to model the iteration of payments for impermanent prospect
    for i in range(1, z+1):  # for each time that the project is repeated (normally); project is repeated z times if it never fails
        Cs = Cszero + h * (t_switch - d * i)  # [t_switch - d*i] is the year in which the payment is done

        # adding risk of project failure
        for j in range(t_switch - d * i + 1, t_switch - d * (i - 1)):  # j is the current year {would be until t_switch - d * (i - 1)-1) but you need to add 1
            # [t_switch - d*i + 1] is the first year of the current temporary project
            # [t_switch - d*(i-1)-1] is the last year of the current temporary project
            if np.random.rand() <= risk_failure:  # np.random.rand() generates uniformly distributed random numbers in the interval [0,1]
                paid[j] = (Cszero + h * j) / ((1 + disc_rate) ** j)  # j is the current year

        # calculate NPV for current time period
        NPV = Cs / ((1 + disc_rate) ** (t_switch - d * i))  # discount to present value the payment
        NPV_beforeswitch += NPV  # NPV_beforeswitch is the present value of the scheduled payments from start to the switching time

    # final addition
    NPV_final = NPV_beforeswitch + Cp / (1 + disc_rate) ** t_switch + np.sum(paid)  # np.sum calculates sum of the elements in the array
    NPVs_final_array[k] = NPV_final  # adding the current NPV_final value to the list; musn't be reset
    NPV_beforeswitch = 0  # resetting NPV_beforeswitch variable
    NPV_final = 0  # resetting NPV_final variable
    paid = np.zeros(t_switch)  # resetting paid array

mean_NPV_final = np.mean(NPVs_final_array)
std_NPV_final = np.std(NPVs_final_array)
print(f"Mean: ${mean_NPV_final}")
print(f"With a standard deviation of: {std_NPV_final}")

