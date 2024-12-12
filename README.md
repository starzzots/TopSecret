# Trading Data Collection and Backtesting Framework

This repository contains Python scripts for:

* **Data Collection:** 
    - Fetches real-time option and cryptocurrency data from Robinhood using the `robin_stocks` library.
    - Saves the collected data to CSV files for later analysis.
* **Data Reading:** 
    - Reads data from CSV files into Python data structures (lists and dictionaries).
* **(Future Implementation) Backtesting:** 
    - (Planned) Backtesting framework for evaluating trading strategies on historical data.

**Prerequisites:**

- Python 3.x
- `robin_stocks` library: `pip install robin_stocks`
- **(Optional) Virtual Environment:** 
    - Recommended for managing project dependencies: 
        - `python3 -m venv .venv`
        - `source .venv/bin/activate` (or `.venv\Scripts\activate` on Windows)

**Usage:**

1. **Data Collection:**
   - **(Replace placeholders in the script)**: Update the script with your Robinhood credentials (username and password). **Important:** Store these credentials securely outside of the repository (e.g., in a separate configuration file or environment variable).
   - **Run the script:** Execute the data collection script to fetch and save data to CSV files.

2. **Data Reading:**
   - **(Modify the script)**: Adjust the script to read data from the saved CSV files and process it as needed.

3. **Backtesting (Future Implementation):** 
   - (In progress) This feature will allow you to define and test trading strategies using historical data.

**Data Storage:**

- By default, data is saved to CSV files within the repository. 
- You can modify the script to save data to a different location (e.g., a dedicated data directory).

**Note:**

- This project is for **educational and research purposes only**. 
- Trading in financial markets involves significant risks. 
- Always conduct thorough research and consult with a qualified financial advisor before making any investment decisions.

**Contributing:**

Contributions are welcome! Please feel free to fork this repository and submit pull requests.

**Disclaimer:**

This repository and the associated scripts are provided "as is" without any warranties. The author is not responsible for any losses incurred due to the use of this software.
