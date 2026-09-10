import csv, random
from datetime import datetime, timedelta

# Generates 50,000 mock records for ouro
with open('Internal_Orders.csv', 'w', newline='') as f1, open('3PL_Shipping_Logs.csv', 'w', newline='') as f2:
    w1, w2 = csv.writer(f1), csv.writer(f2)
    w1.writerow(['OrderID', 'OrderDate', 'SKU', 'Revenue', 'Payment_Status'])
    w2.writerow(['Logistics_ID', 'Ref_OrderID', 'Delivery_Status'])
    
    for i in range(1, 50001):
        order_id = f"ORD-{100000+i}"
        date = (datetime.now() - timedelta(days=random.randint(1, 365))).strftime('%Y-%m-%d')
        w1.writerow([order_id, date, f"OURO-{random.randint(10,99)}", random.randint(50, 500), random.choice(['Paid', 'Paid', 'Pending'])])
        
        # 95% of orders have shipping logs, 5% are missing to create anomalies
        if random.random() > 0.05: 
            w2.writerow([f"TRK-{900000+i}", order_id, random.choice(['Delivered', 'In Transit', 'RTO'])])