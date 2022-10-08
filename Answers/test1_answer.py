import pandas

#imports the .xlsx file and converts to a Dataframe
df = pandas.read_excel("1.Top 3 Customers based on Amount.xlsx")

#filtering the Dataframe to get the top 3 based on the total amount column
df_top_3_amount = df[["customer_id", "total amount"]].nlargest(3, "total amount")

#creates a new Dataframe for final output
df_final = pandas.DataFrame(columns=['customer_id', 'total amount'])

#searches for name in the df['ID'] column that contains the customer ID then add it to the new Dataframe
for customer_id, total_amount in zip(df_top_3_amount['customer_id'], df_top_3_amount['total amount']):
    for name in df["ID"].dropna():
        if str(customer_id) in name:
            df_final = df_final.append({'customer_id': name, 'total amount': total_amount}, ignore_index = True)
    

#prints the Final Dataframe
print(df_final)

#creates a .xlsx file of the final Dataframe
df_final.to_excel(r"Answers/Answer - Top 3 Customers based on Amount.xlsx", index=False)