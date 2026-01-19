import pandas as pd

# Reading CSV files
ord_det= pd.read_csv('csv files/order_details.csv', encoding='unicode_escape')
ord=pd.read_csv('csv files/orders.csv')
piz=pd.read_csv('csv files/pizzas.csv')
piz_typ=pd.read_csv('csv files/pizza_types.csv', encoding='unicode_escape')
# Merging dataframes
merged_piz=ord_det.merge(piz, on='pizza_id', how='left')
merged_piz= merged_piz.merge(piz_typ, on='pizza_type_id', how='left')
merged_piz= merged_piz.merge(ord, on='order_id', how='left')
# Creating new column total_price
merged_piz['total_price']= merged_piz['quantity'] * merged_piz['price']
# Converting 'date' and 'time' columns to datetime
merged_piz['date']= pd.to_datetime(merged_piz['date'])
time_series= pd.to_datetime(merged_piz['time'], format = '%H:%M:%S')
# Extracting date and time features
merged_piz['hour'] = time_series.dt.hour
merged_piz['day_name'] =merged_piz['date'].dt.day_name()
merged_piz['month_name'] = merged_piz['date'].dt.month_name()
merged_piz['time'] = time_series.dt.time
# Top 5 pizzas by revenue
top_revenue = merged_piz.groupby('name')['total_price'].sum().sort_values(ascending=False).head(5)
print(top_revenue)