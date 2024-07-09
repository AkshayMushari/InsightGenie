# InsightGenie
AI-Powered Data Analysis and Visualization
InsightGenie: AI-Powered Data Analysis and Visualization
Project Description
InsightGenie is an innovative application designed to simplify data analysis and visualization. Leveraging the power of AI, particularly the Llama-2 model, InsightGenie provides users with a comprehensive tool for understanding and interpreting their CSV data. Whether you're a data scientist, business analyst, or just someone looking to gain insights from your data, InsightGenie is here to help.

Features
CSV File Upload: Easily upload your CSV files for analysis.
Data Preview: Get a quick look at your data with a preview of the first few rows.
Descriptive Statistics: Calculate essential statistics including mean, median, mode, and standard deviation.
Correlation Analysis: Compute and visualize the correlation matrix for numeric columns.
Interactive Plots: Generate various plots to visualize your data, including:
Histograms
Scatter Plots
Line Plots
Pair Plots
Heatmaps
Count Plots for categorical data
AI-Powered Q&A: Ask questions about your data and get comprehensive answers using the Llama-2 model.
User-Friendly Interface: Experience an intuitive and interactive user interface built with Streamlit.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/InsightGenie.git
cd InsightGenie
Create and activate a virtual environment:

bash
Copy code
python3 -m venv venv
source venv/bin/activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up environment variables:

Create a .env file in the project root directory.
Add your Langchain API key and other necessary environment variables:
makefile
Copy code
LANGCHAIN_API_KEY=your_langchain_api_key
LANGCHAIN_TRACING_V2=true
Usage
Run the application:

bash
Copy code
streamlit run app.py
Open your web browser and go to http://localhost:8501.

Upload your CSV file, explore the data, generate visualizations, and ask questions using the interactive interface.

Example

Contributing
We welcome contributions from the community! If you have any suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Special thanks to the developers of the pandas, matplotlib, seaborn, and streamlit libraries.
Thanks to the Langchain and Llama-2 teams for providing the powerful tools that make InsightGenie possible.
InsightGenie is your go-to solution for AI-powered data analysis and visualization. Transform your data into actionable insights with ease!
