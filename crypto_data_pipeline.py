import requests
import psycopg2
from psycopg2 import sql

# Fetch cryptocurrency data from CoinGecko API
def fetch_crypto_data():
    url = 'https://api.coingecko.com/api/v3/coins/markets'
    params = {
        'vs_currency': 'usd',  # Fetching data in USD
        'order': 'market_cap_desc',  # Order by market cap (descending)
        'per_page': 15,  # Limit to top 5 cryptocurrencies
        'page': 1,  # Fetch data from the first page
    }
    response = requests.get(url, params=params)
    data = response.json()  # Parse the response into Python dictionary
    return data

# Connect to PostgreSQL database
def connect_to_db():
    conn = psycopg2.connect(
        dbname="crypto_data",  # Name of the database we created earlier
        user="postgres",  # Default PostgreSQL user
        password="*********",  # Replace with your PostgreSQL password
        host="localhost",  # Running PostgreSQL locally
        port="****"  # Default port for PostgreSQL
    )
    return conn

# Insert cryptocurrency data into PostgreSQL table
def insert_data(data):
    conn = connect_to_db()
    cursor = conn.cursor()

    for crypto in data:
        # Check if the cryptocurrency already exists in the database
        cursor.execute(
            sql.SQL("SELECT id FROM cryptocurrencies WHERE symbol = %s"),
            (crypto['symbol'],)
        )
        existing_crypto = cursor.fetchone()

        # If cryptocurrency already exists, skip it, otherwise insert it
        if existing_crypto:
            print(f"Skipping {crypto['name']} ({crypto['symbol']}) as it already exists.")
        else:
            cursor.execute(
                sql.SQL("INSERT INTO cryptocurrencies (name, symbol, price, market_cap, volume_24h, circulating_supply) VALUES (%s, %s, %s, %s, %s, %s)"),
                (crypto['name'], crypto['symbol'], crypto['current_price'], crypto['market_cap'], crypto['total_volume'], crypto['circulating_supply'])
            )
            print(f"Inserted {crypto['name']} ({crypto['symbol']}) into the database.")

    conn.commit()  # Save the changes to the database
    cursor.close()  # Close the cursor
    conn.close()  # Close the database connection

# Main function to run the pipeline
if __name__ == "__main__":
    crypto_data = fetch_crypto_data()  # Fetch data from the API
    insert_data(crypto_data)  # Insert the data into the PostgreSQL database
    print("Data inserted successfully!")
