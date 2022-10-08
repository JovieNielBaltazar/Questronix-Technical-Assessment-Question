import pandas
import numpy as np

#opens .xlsx file and converts the file to a pandas Dataframe
file_name = "3.Top 1 on both billing and delivery country.xlsx"
df = pandas.read_excel(file_name)

#COLUMNS>>
#'ID', 'billing_country', 'Unnamed: 2', 'billing_country.1', 'count',
#'Unnamed: 5', 'delivery_country', 'Unnamed: 7', 'delivery_country.1',
#'count.1'

#to get the maximum value in the column E ('count') column
count_max_value = df['count'].max()

#to get the maximum value in the column J ('count.1') column
count_1_max_value = df['count.1'].max()

#filtering and creating a new Dataframe from df Dataframe(original Dataframe) to get the countries that have the maximum value of the column E ('count') column
df_billing_country_1 = df[df['count'] == count_max_value]

#filtering and creating a new Dataframe from df Dataframe(original Dataframe) to get the countries that have the maximum value of the column J ('count.1') column
df_delivery_country_1 = df[df['count.1'] == count_1_max_value]

#getting the common country from both df_billing_country_1 and df_delivery_country_1
common_country = list(np.intersect1d(df_billing_country_1['billing_country.1'], df_delivery_country_1['delivery_country.1']))

#creates a new Dataframe to store the common country with its corresponding maximum billing_country count and delivery_country count
df_final = pandas.DataFrame(columns=['Top 1 on both billing and delivery country', 
                                     'billing_country count',
                                     'delivery_country count'])

#inserting the data from the df_final Dataframe into the newly created Dataframe
for country in common_country:
    df_final = df_final.append({"Top 1 on both billing and delivery country": country, 
                                "billing_country count": count_max_value, 
                               "delivery_country count": count_1_max_value}, ignore_index = True)

#converts the Dataframe to a .xlsx file and saving it to folder 'Answers'
df_final.to_excel(r"Answers/Answer - Top 1 on both billing and delivery country.xlsx", index=False)

#use "print(df_final)"to see the Top 1 on both billing and delivery country