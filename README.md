

# Company Investment Dashboard

## Overview
This repository contains a Streamlit application that visualizes investment data for various companies, focusing on key metrics such as total investment, fund size, and global south deals funded. The dashboard provides a user-friendly interface to explore and analyze company-specific investment details and comparative analytics across all companies.

## Features
- **Total Investment Overview**: Displays overall investment statistics.
- **Company Selection**: Users can select a company from a dropdown to view specific investment details.
- **Comparative Bar Charts**: Visual comparisons for:
  - Investment vs. Fund Size
  - Investment vs. Global South Deals Funded
  - Fund Size vs. Global South Deals Funded
- **Custom Styling**: CSS is used to enhance the visual appeal of the dashboard.

## Prerequisites
To run this application, you need the following:
- Python 3.6 or higher
- Streamlit library
- Pandas library
- Plotly library

## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_directory>


2. Install the required packages:
   ```bash
   pip install streamlit pandas plotly
   ```

3. Download or create a CSV file named `dummy_sample.csv` with the following columns:
   - **Company Name**: Name of the company.
   - **Investment ($M)**: Investment amount in millions of dollars.
   - **Fund Size ($M)**: Size of the fund in millions of dollars.
   - **Global South Deals Funded**: Number of deals funded in the Global South.
   - **Country**: Country associated with the company.

## Usage
To run the application, execute the following command in your terminal:
```bash
streamlit run app.py
```
This will launch the Streamlit server and open the dashboard in your default web browser.

## Code Structure
- `app.py`: Main application file containing the Streamlit code.
- `dummy_sample.csv`: Sample dataset used for demonstration (make sure to create or download this file).

## Customization
Feel free to modify the CSS styles in the application for personalized appearance or to expand the functionality by adding new visualizations or metrics.

## Contributions
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
```

### Notes:
- Replace `<repository_url>` and `<repository_directory>` with your actual repository URL and directory name.
- You may want to adjust the README based on any additional features or requirements you have.
