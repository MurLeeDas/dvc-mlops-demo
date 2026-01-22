import pandas as pd
import numpy as np
from datetime import datetime, timedelta

print("📖 Loading original dataset...")
df = pd.read_csv('ecommerce_reviews.csv')
print(f"   Original: {len(df):,} rows")

print("\n➕ Adding 1,000,000 new reviews...")
np.random.seed(99)
n_new = 1_000_000

review_texts = [
    'Absolutely love this product!',
    'Not satisfied with the quality.',
    'Excellent quality and fast delivery!',
    'Poor delivery experience.',
    'Highly recommend!',
    'Complete waste of money.'
]

product_categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Sports']

new_data = {
    'review_id': range(len(df) + 1, len(df) + n_new + 1),
    'customer_id': np.random.randint(1000, 100000, n_new),
    'product_id': np.random.randint(100, 50000, n_new),
    'product_category': np.random.choice(product_categories, n_new),
    'rating': np.random.choice([1, 2, 3, 4, 5], n_new, p=[0.05, 0.10, 0.20, 0.35, 0.30]),
    'review_text': np.random.choice(review_texts, n_new),
    'review_length': np.random.randint(50, 500, n_new),
    'purchase_date': [
        (datetime.now() - timedelta(days=np.random.randint(1, 30))).strftime('%Y-%m-%d')
        for _ in range(n_new)
    ],
    'verified_purchase': np.random.choice([True, False], n_new, p=[0.85, 0.15]),
    'helpful_votes': np.random.randint(0, 100, n_new),
    'total_votes': np.random.randint(0, 150, n_new)
}

new_df = pd.DataFrame(new_data)
df_updated = pd.concat([df, new_df], ignore_index=True)

print("💾 Saving updated dataset...")
df_updated.to_csv('ecommerce_reviews.csv', index=False)

import os
file_size_mb = os.path.getsize('ecommerce_reviews.csv') / (1024 * 1024)

print(f"\n✅ Dataset updated!")
print(f"   Updated: {len(df_updated):,} rows")
print(f"   File size: {file_size_mb:.2f} MB")