from flask import Flask, request, render_template
import json
import wit
import pyipinfodb
import private

app = Flask(__name__)


@app.route("/")
def home(ip=None):
    ip_lookup = pyipinfodb.IPInfo(private.IP_INFO_TOKEN)
    response = ip_lookup.get_city()
    postcode = response['zipCode']
    city = response['cityName']

    return render_template('index.html', postcode=postcode, city=city)


@app.route("/api", methods=['GET'])
def api():
    """Return a message from query."""
    text = request.args.get('question', '')
    print text

    return json.dumps({'answer': text})


def handle_query(text):
    answer = text

    return answer


if __name__ == "__main__":
    app.run(debug=True)
