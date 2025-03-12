# Project Setup Guide

## Prerequisites
Ensure you have Python installed on your system. If not, download and install it from [python.org](https://www.python.org/).

## Steps to Run the Code

### 1. Create a Groq API Key
- Sign up or log in to [Groq](https://groq.com/) to obtain your API key.
- Store the API key in a `.env` file with the following format:
  ```
  groq_api=your_groq_api_key_here
  ```

### 2. Install Dependencies
- Install the required packages using:
  ```
  pip install -r requirements.txt
  ```

### 3. Download Required Data
- Before running the Streamlit app, download the **Gale Encyclopedia of Medicine** PDF from Google.
- Store the downloaded PDF in a folder named **"data"** in the same directory as your project.

### 4. Running the Streamlit App
- If you're using Streamlit, ensure all dependencies are installed, and then run:
  ```
  streamlit run app.py
  ```
- Make sure the **Gale Encyclopedia of Medicine** PDF is available in the **"data"** folder before running the app.

## Additional Notes
- Ensure your `.env` file is in the same directory as your project.
- If you encounter any issues, check if all dependencies are installed correctly.
- Make sure the **"data"** folder exists and contains the necessary PDF file before running the Streamlit app.

Happy coding! 🚀
