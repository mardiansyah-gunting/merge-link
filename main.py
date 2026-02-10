import pandas as pd

# 1. Membaca file CSV input
input_filename = 'obel_plots.csv'
try:
    df = pd.read_csv(input_filename)
except FileNotFoundError:
    print(f"Error: File '{input_filename}' tidak ditemukan.")
    exit()

# 2. Mendefinisikan pola URL
base_url = "https://cloud.treeo.one/forestry/plot/{}?tab=activities&page=1"

# 3. Membuat kolom baru 'Generated URL' dengan mengganti {} dengan Plot ID
df['Generated URL'] = df['Plot ID'].apply(lambda x: base_url.format(x))

# 4. Menyimpan hasil ke file CSV baru
output_filename = 'obel_treeo_plot_urls.csv'
df.to_csv(output_filename, index=False)

print(f"Berhasil! File '{output_filename}' telah dibuat.")
print(df.head()) # Menampilkan 5 baris pertama sebagai preview