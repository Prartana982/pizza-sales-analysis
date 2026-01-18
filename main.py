import pandas as pd


ord_det= pd.read_csv('csv files/order_details.csv')
ord=pd.read_csv('csv files/orders.csv')
piz=pd.read_csv('csv files/pizzas.csv')
piz_typ=pd.read_csv('csv files/pizza_types.csv')
merged_piz=ord_det.merge(piz, on='pizza_id', how='left')
merged_piz= merged_piz.merge(piz_typ, on='pizza_type_id', how='left')
merged_piz= merged_piz.merge(ord, on='order_id', how='left')
merged_piz['total_price']= merged_piz['quantity'] * merged_piz['price']
merged_piz['date']= pd.to_datetime(merged_piz['date'])
merged_piz['time']= pd.to_datetime(merged_piz['time'], format = '%H:%M:%S').dt.time
