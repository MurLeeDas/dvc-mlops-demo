# Generate synthetic dataset (~500MB)
python3 << 'EOF'
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)
n_records = 5_000_000  # 5 million records = ~500MB

print("Generating 5 million customer reviews...")

data = {
    'review_id': range(1, n_records + 1),
    'customer_id': np.random.randint(1000, 50000, n_records),
    'product_id': np.random.randint(100, 10000, n_records),
    'rating': np.random.choice([1, 2, 3, 4, 5], n_records, p=[0.05, 0.10, 0.20, 0.35, 0.30]),
    'review_text': np.random.choice([
        'Great product!', 'Not satisfied', 'Excellent quality', 
        'Poor delivery', 'Highly recommend', 'Waste of money',
        'Good value', 'Amazing!', 'Terrible experience', 'Worth buying'
    ], n_records),
    'purchase_date': [
        (datetime.now() - timedelta(days=np.random.randint(1, 365))).strftime('%Y-%m-%d')
        for _ in range(n_records)
    ],
    'verified_purchase': np.random.choice([True, False], n_records, p=[0.8, 0.2])
}

df = pd.DataFrame(data)
df.to_csv('ecommerce_reviews.csv', index=False)
print(f"Dataset created: {len(df):,} rows")
print(f"File size: {df.memory_usage(deep=True).sum() / (1024**2):.2f} MB")
print("\nFirst few rows:")
print(df.head())
EOF