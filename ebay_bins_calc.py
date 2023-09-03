# This program is used to determine the price you paid for a specific item at the
# goodwill outlet store (aka the goodwill bins). It was hard to know the exact
# price I paid for an item when inputting its information on my eBay spreadsheet since they charge
# by the pound, so I have created this calculator to solve that issue. Simply weigh your item, input
# its weight, and see the exact price you paid for it. The store in my area charges $1.69 per 2 lbs,
# so this calculator is set up by default to have the rate as 1.69. 

weight = float(input('Enter the weight of the item in ounces as a decimal. '))
#rate = float(input('Enter the store\'s rate per pound as a decimal. '))

fraction = float(weight / 32.0)    # 32.0 represents 32 oz or 2 lbs

final = float(fraction * 1.69)     # 1.69 is the price per 2 pounds at my local goodwill bins
# final = float(fraction * rate)     # 1.69 is the price per 2 pounds at my local goodwill bins

print('You paid ' + str(final) + ' for the item.')
