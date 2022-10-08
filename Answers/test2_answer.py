import pandas

#imports the .xlsx file and converts to a Dataframe
df = pandas.read_excel("2.Bottom 3 Products.xlsx")

#filtering the Dataframe to get the top 3 based on the total amount column
df_smallest_3_amount = df[["product_id", "Total orders"]].nsmallest(3, "Total orders")

#creates a new Dataframe for final output
df_final = pandas.DataFrame(columns=['bottom 3 products', 'PRODUCT ID'])

#searches for name in the df['ID'] column that contains the customer ID then add it to the new Dataframe
for product_id, Total_orders in zip(df_smallest_3_amount["product_id"], df_smallest_3_amount["Total orders"]):
    df_final = df_final.append({'bottom 3 products': Total_orders, 'PRODUCT ID': product_id}, ignore_index = True)


#prints the Final Dataframe
print(df_final)

#creates a .xlsx file of the final Dataframe
df_final.to_excel(r"Answers/Answer - Bottom 3 Products.xlsx", index=False)

