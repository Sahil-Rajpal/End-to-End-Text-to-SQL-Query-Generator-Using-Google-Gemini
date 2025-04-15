# End-to-End-Text-to-SQL-Query-Generator-Using-Google-Gemini 📊

This project provides a user-friendly interface to generate SQL queries from natural language descriptions. It utilizes the Gemini AI model from Google AI and connects to a local SQLite database named "student.db".

## Prerequisites
- Python 3.7 or later
- `streamlit` package
- `dotenv` package
- Google AI account and API key for the Gemini model
- `sqlite3` package (usually comes pre-installed)

## Installation
1. Clone this repository.
2. Create a virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate  # Windows: env\Scripts\activate.bat
    # you can use conda env also
    ```
    Use code with caution.

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```
    Use code with caution.

## Usage
1. Replace `YOUR_API_KEY` in the `.env` file with your actual Google AI API key.
2. Run the app:

    ```bash
    streamlit run app.py
    ```
    Use code with caution.

## Explanation
- The `app.py` file contains the main logic of the application. It:
  - Loads the necessary libraries and configures Gemini AI using the API key.
  - Defines a prompt explaining the functionality of the app.
  - Uses `st.text_input` to create a text box where users can enter their natural language question.
  - Uses a button (`st.button`) to trigger the query generation process.
  - Upon clicking the button, it uses the `get_gemini_response` function to send the user question and prompt to the Gemini model and retrieve the generated SQL query.
  - It then calls the `read_sql` function to execute the generated query on the "student.db" and displays the results.
  - Implements basic error handling to handle potential issues.

## Additional Notes
- This example uses a simple database with sample data. You can modify the code to connect to and work with your specific database.
- The code utilizes the Streamlit library for building the user interface. Refer to the Streamlit documentation for more information on customizing the app design and functionalities.
- Consider adding comments to your code to improve readability and maintainability.
