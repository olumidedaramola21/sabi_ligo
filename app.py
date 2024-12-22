from flask import Flask, request,redirect, url_for, render_template, session
import requests, os, uuid, json
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():

    return render_template(
        "index.html"
    )

@app.route("/", methods=[ "POST"])
def index():
    translated_text="",
    original_text="",
    target_language="",

    if request.method == "POST":
        # read the text from the user
        original_text = request.form["text"]
        target_language = request.form["language"]

        # retrive environment variables
        key = os.environ["KEY"]
        endpoint = os.environ["ENDPOINT"]
        location = os.environ["LOCATION"]
        path = "/translate?api-version=3.0"

        # construct target url
        target_language_parameter = "&to=" + target_language
        constructed_url = endpoint + path + target_language_parameter

        # construct header information
        headers = {
            "Ocp-Apim-Subscription-Key": key,
            "Ocp-Apim-Subscription-Region": location,
            "Content-type": "application/json",
            "X-ClientTraceId": str(uuid.uuid4()),
        }

        # body inforamtion
        body = [{"text": original_text}]

        # request
        translator_request = requests.post(constructed_url, headers=headers, json=body)
        # retrieve the json response
        translator_response = translator_request.json()
        # retrieve the translation
        translated_text = translator_response[0]["translations"][0]["text"]
        print(translated_text)



    return render_template(
        "result.html",
        translated_text=translated_text,
        original_text=original_text,
        target_language=target_language,
    )


if __name__ == "__main__":
    app.run(debug=True)
