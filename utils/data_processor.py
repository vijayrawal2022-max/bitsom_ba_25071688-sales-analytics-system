from collections import defaultdict
from datetime import datetime

def parse_and_clean_data(lines):
    transactions = []

    for line in lines:
        try:
            parts = line.split('|')
            transactions.append({
                'TransactionID': parts[0],
                'Date': parts[1],
                'ProductID': parts[2],
                'ProductName': parts[3],
                'Quantity': int(parts[4]),
                'UnitPrice': float(parts[5]),
                'CustomerID': parts[6],
                'Region': parts[7]
            })
        except:
            continue

    return transactions


def validate_transactions(transactions):
    valid, invalid = [], []

    for t in transactions:
        if t['Quantity'] > 0 and t['UnitPrice'] > 0:
            valid.append(t)
        else:
            invalid.append(t)

    return valid, invalid


def sales_summary(transactions):
    total_revenue = sum(t['Quantity'] * t['UnitPrice'] for t in transactions)
    avg_order = total_revenue / len(transactions)

    dates = [datetime.strptime(t['Date'], "%Y-%m-%d") for t in transactions]

    return {
        'total_revenue': total_revenue,
        'total_transactions': len(transactions),
        'average_order_value': avg_order,
        'date_range': f"{min(dates).date()} to {max(dates).date()}"
    }


def region_wise_performance(transactions):
    region_data = defaultdict(lambda: {'sales': 0, 'count': 0})

    for t in transactions:
        region_data[t['Region']]['sales'] += t['Quantity'] * t['UnitPrice']
        region_data[t['Region']]['count'] += 1

    total_sales = sum(r['sales'] for r in region_data.values())

    result = []
    for region, data in region_data.items():
        result.append({
            'region': region,
            'sales': data['sales'],
            'percentage': (data['sales'] / total_sales) * 100,
            'transactions': data['count']
        })

    return sorted(result, key=lambda x: x['sales'], reverse=True)
