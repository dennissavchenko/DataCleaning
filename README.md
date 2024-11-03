# Data Cleaning and Standardization

## Project Overview

This project is dedicated to the cleaning and standardization of real estate data, ensuring high data quality for future analysis. By systematically addressing issues such as missing values, outliers, duplicates, and data type inconsistencies, the project aims to prepare the dataset for reliable use in analytical applications and decision-making processes.

## Database Usage

### Database Selection
For this project, MongoDB has been selected as the database solution due to its flexibility in handling diverse datasets and its ability to store records in a document-oriented format.

### Connecting to the Database
A Python script is employed to establish a connection to the MongoDB database. Credentials such as the username, password, and database name are securely managed in a separate configuration file, which is excluded from version control to protect sensitive information.

### Initial Data Load
The raw dataset is initially loaded into the MongoDB database, preserving the original records. This step ensures that the dataset remains intact for reference and verification, allowing for a baseline comparison during the cleaning process.

## Data Cleaning and Standardization

The core focus of this project is on the data cleaning and standardization process, which involves the following steps:

1. **Using Pandas for Data Processing:**  
   The raw data is processed using Pandas, providing efficient tools for data manipulation and analysis.

2. **Handling Missing Data:**  
   Missing values are systematically identified and addressed through methods such as imputation or removal, based on the context and importance of the data.

3. **Outliers and Duplicates:**  
   Techniques are implemented to detect and manage outliers, ensuring that they do not distort the dataset. Duplicate entries are identified and removed to maintain data integrity.

4. **Data Type Correction:**  
   Each column’s data type is reviewed and corrected as needed to ensure consistency and compatibility for future analyses.

5. **Normalization and Standardization of Data:**  
   - **Numerical Data Normalization:** Numerical data is normalized using **Z-score normalization** to rescale values based on the distribution of each column, ensuring consistent scaling across features.
   - **Categorical Data Standardization:** Categorical data is standardized to a consistent format, such as converting text to lowercase, replacing abbreviations, or ensuring uniform category labels.

6. **Final Data Load:**  
   After the cleaning and standardization processes are complete, the refined dataset is reloaded into the MongoDB database, ensuring that only high-quality data is stored for future use.

7. **Documentation:**  
   Comprehensive documentation is provided throughout the script, detailing each cleaning step and the rationale behind the decisions made. This promotes transparency and reproducibility, making it easier for future users to understand and utilize the dataset effectively.

