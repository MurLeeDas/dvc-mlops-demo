<<<<<<< HEAD
# Generate synthetic dataset (~500MB)
python3 << 'EOF'
=======
#!/usr/bin/env python3
"""
Dataset Generator for DVC MLOps Demo
Generates a realistic e-commerce customer reviews dataset (~500-600MB)
"""

>>>>>>> 33a6979 (DVC hands-on demo)
import pandas as pd
import numpy as np
from datetime import datetime, timedelta

<<<<<<< HEAD
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
=======
def generate_dataset(n_records=8_000_000, output_file='ecommerce_reviews.csv'):
    """
    Generate e-commerce customer reviews dataset
    
    Args:
        n_records: Number of records to generate (default: 8M for ~500-600MB)
        output_file: Output CSV filename
    """
    print(f"🚀 Generating {n_records:,} customer reviews...")
    print("⏱️  This will take about 30-60 seconds...\n")
    
    np.random.seed(42)
    
    # Generate review texts with more variety
    review_texts = [
        'Absolutely love this product! Exceeded all my expectations.',
        'Not satisfied with the quality. Returned immediately.',
        'Excellent quality and fast delivery. Will buy again!',
        'Poor delivery experience. Package was damaged.',
        'Highly recommend! Best purchase I have made this year.',
        'Complete waste of money. Very disappointed.',
        'Good value for money. Works as described.',
        'Amazing product! Five stars from me.',
        'Terrible experience. Customer service was unhelpful.',
        'Worth every penny. Very satisfied with my purchase.',
        'Product stopped working after a week. Very upset.',
        'Great product but shipping took too long.',
        'Perfect! Exactly what I was looking for.',
        'Quality is decent but overpriced in my opinion.',
        'Outstanding! Would definitely buy from this seller again.',
        'Arrived broken. Had to go through lengthy return process.',
        'Decent product for the price point.',
        'Fantastic! My family loves it too.',
        'Not as advertised. Photos were misleading.',
        'Superb quality! Impressed with the craftsmanship.'
    ]
    
    # Product categories for more realistic data
    product_categories = [
        'Electronics', 'Clothing', 'Home & Kitchen', 'Books', 
        'Sports', 'Toys', 'Beauty', 'Automotive', 'Garden', 'Health'
    ]
    
    print("📊 Creating dataset structure...")
    
    # Generate data in chunks to manage memory
    chunk_size = 1_000_000
    chunks = []
    
    for i in range(0, n_records, chunk_size):
        current_chunk_size = min(chunk_size, n_records - i)
        
        chunk_data = {
            'review_id': range(i + 1, i + current_chunk_size + 1),
            'customer_id': np.random.randint(1000, 100000, current_chunk_size),
            'product_id': np.random.randint(100, 50000, current_chunk_size),
            'product_category': np.random.choice(product_categories, current_chunk_size),
            'rating': np.random.choice([1, 2, 3, 4, 5], current_chunk_size, 
                                      p=[0.05, 0.10, 0.20, 0.35, 0.30]),
            'review_text': np.random.choice(review_texts, current_chunk_size),
            'review_length': np.random.randint(50, 500, current_chunk_size),
            'purchase_date': [
                (datetime.now() - timedelta(days=np.random.randint(1, 730))).strftime('%Y-%m-%d')
                for _ in range(current_chunk_size)
            ],
            'verified_purchase': np.random.choice([True, False], current_chunk_size, 
                                                  p=[0.85, 0.15]),
            'helpful_votes': np.random.randint(0, 100, current_chunk_size),
            'total_votes': np.random.randint(0, 150, current_chunk_size)
        }
        
        chunk_df = pd.DataFrame(chunk_data)
        chunks.append(chunk_df)
        
        progress = ((i + current_chunk_size) / n_records) * 100
        print(f"  ⚙️  Progress: {progress:.1f}% ({i + current_chunk_size:,} / {n_records:,} rows)")
    
    print("\n🔗 Combining chunks...")
    df = pd.concat(chunks, ignore_index=True)
    
    print("💾 Writing to CSV file...")
    df.to_csv(output_file, index=False)
    
    # Calculate actual file size
    import os
    file_size_bytes = os.path.getsize(output_file)
    file_size_mb = file_size_bytes / (1024 * 1024)
    
    print(f"\n✅ Dataset created successfully!")
    print(f"📁 Filename: {output_file}")
    print(f"📊 Total rows: {len(df):,}")
    print(f"📏 File size: {file_size_mb:.2f} MB ({file_size_bytes:,} bytes)")
    print(f"🔢 Memory usage: {df.memory_usage(deep=True).sum() / (1024**2):.2f} MB")
    
    print(f"\n👀 First few rows:")
    print(df.head(10))
    
    print(f"\n📈 Dataset statistics:")
    print(f"  - Average rating: {df['rating'].mean():.2f}")
    print(f"  - Verified purchases: {df['verified_purchase'].sum():,} ({df['verified_purchase'].mean()*100:.1f}%)")
    print(f"  - Date range: {df['purchase_date'].min()} to {df['purchase_date'].max()}")
    print(f"  - Unique customers: {df['customer_id'].nunique():,}")
    print(f"  - Unique products: {df['product_id'].nunique():,}")

if __name__ == "__main__":
    # Generate 8 million records for ~500-600MB file
    generate_dataset(n_records=8_000_000, output_file='ecommerce_reviews.csv')
    print("\n✨ Ready for DVC demo!")
>>>>>>> 33a6979 (DVC hands-on demo)
