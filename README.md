# Sabi_Lingo

This web application allows users to enter a sentence and receive a translation in their desired language using Azure AI Translator. The project is built using Flask, a lightweight WSGI web application framework in Python.

## Features

- Translate sentences to multiple languages
- User-friendly interface
- Fast and accurate translations

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/olumidedaramola21/sabi_lingo.git
    ```
2. Navigate to the project directory:
    ```bash
    cd sabi_lingo
    ```
3. Create a virtual environment:
    ```bash
    python -m venv venv
    ```
4. Activate the virtual environment:
    - On Windows:
        ```bash
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

6. Get the required key-value pairs for the `.env` file from Azure account:
    - Sign in to your [Azure Portal](https://portal.azure.com/)
    - Navigate to your Azure Cognitive Services resource.
    - Create AI Translator service resources
    - Go to the "Keys and Endpoint" section.
    - Copy the key and enpoint values.
    - Update the `.env` fiile with these values

## Usage

1. Run the Flask application:
    ```bash
    flask run
    ```
2. Open your web browser and go to `http://127.0.0.1:5000/`.
3. Enter a sentence and select the target language to get the translation.


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


