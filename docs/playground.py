# fcf_list = list of fcf in units of thousands
def compute_company_avg_growth(fcf_list, caution_factor=0.66):
    relative_growths = []
    product_of_growth_rates = 1
    for i, fcf in enumerate(fcf_list):
        if i < len(fcf_list) - 1:
            relative_growths.append((fcf_list[i + 1] - fcf) / fcf)

    for growth in relative_growths:
        product_of_growth_rates *= (1 + growth)
    return (product_of_growth_rates ** (1. / (len(fcf_list) - 1)) - 1) * caution_factor


def compute_start_value(fcf_list):  # use last couple of fcfs
    sum = 0
    for fcf in fcf_list:
        sum += fcf
    return sum / len(fcf_list)


def compute_value(avg_fcf, start_value):
    after_ten_years = 0
    for i in range(1, 11):
        after_ten_years += (start_value * ((1 + avg_fcf) ** float(i))) / (1.05 ** float(i))

    fcf_after_ten_years = (start_value * (1 + avg_fcf) ** float(10)) / (1.05 ** float(10))

    after_hundred_years = 0
    for i in range(11, 101):
        after_ith_year = fcf_after_ten_years / (1.05 ** float(i))
        after_hundred_years += after_ith_year

    return after_ten_years + after_hundred_years

# # Apple 2021 value
# avg_growth = compute_company_avg_growth([50803, 64121, 58896, 73365, 92953])
#
# print('Average Growth Apple')
# print(str(avg_growth) + '%')  # -> 12.2%
# # conservative estimate: 2/3 * value ~ 8%
#
# start_value = compute_start_value([58896, 73365, 92953])
# print(start_value)
# print('Value of Apple')
# value = compute_value(avg_growth, start_value)
# print(value)
#
# # divide by number of 'shares outstanding' to get the fair price of Apple
# # check e.g. https://finance.yahoo.com/quote/AAPL/key-statistics/
# print('Fair price of an Apple Stock')
# print(value * 1000000 / 16300000000)
#
# print('##########################')



# Adidas 2021 value
# avg_growth = compute_company_avg_growth([1939000, 2111000, 1043000, 2525000])
#
# print('Average Growth Adidas')
# print(str(avg_growth) + '%')  # -> 12.2%
# # conservative estimate: 2/3 * value ~ 8&
#
# start_value = compute_start_value([1939000, 2111000, 1043000, 2525000])
# print(start_value)
# print('Value of Adidas')
# value = compute_value(avg_growth, start_value)
# print(value)
#
# # divide by number of 'shares outstanding' to get the fair price of Apple
# # check e.g. https://finance.yahoo.com/quote/AAPL/key-statistics/
# print('Fair price of an Adidas Stock')
# print(value * 1000 / 192100000)
#
# print('##########################')




# Bonduelle 2021 value
# avg_growth = compute_company_avg_growth([43751, 571, 82463, 28982])
#
# print('Average Growth Bonduelle')
# print(str(avg_growth) + '%')  # -> 12.2%
# # conservative estimate: 2/3 * value ~ 8&
#
# start_value = compute_start_value([43751, 571, 82463, 28982])
# print(start_value)
# print('Value of Bonduelle')
# value = compute_value(avg_growth, start_value)
# print(value)
#
# # divide by number of 'shares outstanding' to get the fair price of Apple
# # check e.g. https://finance.yahoo.com/quote/AAPL/key-statistics/
# print('Fair price of an Bonduelle Stock')
# print(value * 1000 / 32630114)
#
# print('##########################')


# Carl Zeiss Meditec 2021 value
# avg_growth = compute_company_avg_growth([152451, 172923, 133541, 296562])
#
# print('Average Growth Carl Zeiss Meditec')
# print(str(avg_growth) + '%')  # -> 12.2%
# # conservative estimate: 2/3 * value ~ 8&
#
# start_value = compute_start_value([152451, 172923, 133541, 296562])
# print(start_value)
# print('Value of Carl Zeiss Meditec')
# value = compute_value(avg_growth, start_value)
# print(value)
#
# # divide by number of 'shares outstanding' to get the fair price of Apple
# # check e.g. https://finance.yahoo.com/quote/AAPL/key-statistics/
# print('Fair price of an Carl Zeiss Meditec Stock')
# print(value * 1000 / 89440000)



# Stratasys 2021 value
avg_growth = compute_company_avg_growth([7596, -33764, 29356])

print('Average Growth Stratasys')
print(str(avg_growth) + '%')  # -> 12.2%
# conservative estimate: 2/3 * value ~ 8&

start_value = compute_start_value([7596, -33764, 29356])
print(start_value)
print('Value of Stratasys')
value = compute_value(avg_growth, start_value)
print(value)

# divide by number of 'shares outstanding' to get the fair price of Apple
# check e.g. https://finance.yahoo.com/quote/AAPL/key-statistics/
print('Fair price of an Stratasys Stock')
print(value * 1000 / 130360000)