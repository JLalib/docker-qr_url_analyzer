from flask import Flask, request, jsonify
import requests
import os
import base64

app = Flask(__name__)
VIRUSTOTAL_API_KEY = os.environ.get("VT_API_KEY")
VIRUSTOTAL_URL = "https://www.virustotal.com/api/v3/urls"
VIRUSTOTAL_BASE_URL = "https://www.virustotal.com/gui/url/"

def analyze_url(url):
    headers = {"x-apikey": VIRUSTOTAL_API_KEY}
    url_base64 = base64.urlsafe_b64encode(url.encode()).decode().strip("=")
    response = requests.get(f"{VIRUSTOTAL_URL}/{url_base64}", headers=headers)

    if response.status_code == 200:
        result_data = response.json()
        if result_data.get("data"):
            attr = result_data["data"]["attributes"]
            stats = attr["last_analysis_stats"]
            vt_url = f"{VIRUSTOTAL_BASE_URL}{url_base64}"
            return {
                "safe": stats["malicious"] == 0 and stats["suspicious"] == 0,
                "malicious": stats.get("malicious", 0),
                "suspicious": stats.get("suspicious", 0),
                "undetected": stats.get("undetected", 0),
                "harmless": stats.get("harmless", 0),
                "vt_url": vt_url
            }

    response_post = requests.post(VIRUSTOTAL_URL, headers=headers, data={"url": url})
    if response_post.status_code == 200:
        url_id = response_post.json()["data"]["id"]
        response = requests.get(f"{VIRUSTOTAL_URL}/{url_id}", headers=headers)
        if response.status_code == 200:
            result_data = response.json()
            if result_data.get("data"):
                attr = result_data["data"]["attributes"]
                stats = attr["last_analysis_stats"]
                vt_url = f"{VIRUSTOTAL_BASE_URL}{url_base64}"
                return {
                    "safe": stats["malicious"] == 0 and stats["suspicious"] == 0,
                    "malicious": stats.get("malicious", 0),
                    "suspicious": stats.get("suspicious", 0),
                    "undetected": stats.get("undetected", 0),
                    "harmless": stats.get("harmless", 0),
                    "vt_url": vt_url
                }
    return {"safe": False, "error": "No se pudo analizar"}

@app.route("/analyze", methods=["POST"])
def analyze():
    try:
        data = request.get_json()
        url = data.get("url")
        if not url:
            return jsonify({"error": "No se proporcionó URL"}), 400
        result = analyze_url(url)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
