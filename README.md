# Crypto Data Pipeline

This project collects data about cryptocurrencies (like Bitcoin, Ethereum, and others) and saves it into a database. The process is simple: the data is gathered, cleaned up, and then stored in a PostgreSQL database. You can then use this data for analysis or to track trends in the crypto market.

## Tools and Technologies Used

- **Python 3.x**: The programming language used to run the project.
- **PostgreSQL**: A free and open-source database used to store cryptocurrency data.
- **CoinGecko API**: A service that provides live data on thousands of cryptocurrencies.
- **pandas**: A Python library used to clean and organize the data.
- **psycopg2**: A library used to interact with the PostgreSQL database.
- **requests**: A Python library to make requests to the CoinGecko API.

## What You’ll Need

To run this project, you need to have:

- **Python 3.x** installed on your system.
- **PostgreSQL** installed and running.
- The required Python packages (listed in `requirements.txt`).


## Query Results Example
Here's an example of how the cryptocurrency data looks in PostgreSQL:

![Crypto Data Query Results](Crypto_ETL\images\results.png)

## How to Set It Up

### 1. Clone the Project

The first thing you’ll want to do is download the project to your computer. Open your terminal (Command Prompt, PowerShell, or terminal in Visual Studio Code) and run:

```bash
git clone https://github.com/AlexPR704/Crypto_Data_Pipeline.git
cd Crypto_Data_Pipeline

### 2. Create a Virtual Environment

A virtual environment helps manage the project dependencies separately from other Python projects. It's a good practice, but if you’re comfortable with managing dependencies globally, you can skip this step.

To create and activate the virtual environment:

On Windows:
python -m venv venv
.\venv\Scripts\activate


### 3. Install Dependencies
Once the virtual environment is activated (or if you're skipping it), you’ll need to install the libraries and packages that the project depends on. Run this command to install everything:

```bash
pip install -r requirements.txt

This will install all the required Python libraries like requests, pandas, psycopg2, etc., that are needed for the project to work.


### 4. Set Up Your PostgreSQL Database
Make sure you have PostgreSQL installed and running on your system. Then, follow these steps:

1. Open pgAdmin or connect to PostgreSQL via the terminal.
2. Create a new database (e.g., crypto_db).
3. Update your database connection settings in the Python script if necessary.

### 5. Run the Crypto Data Pipeline
Now that everything is set up, you can run the script to fetch cryptocurrency data and store it in your PostgreSQL database. Use:

```bash
python crypto_data_pipeline.py

If everything is configured correctly, the script will fetch live crypto data and save it into the PostgreSQL database.
