import random
import re
import string

from flask import Flask, render_template, redirect, request,flash

app = Flask(__name__)
app.secret_key = "Rickey@18980"
shortened_urls = {}


def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = "".join(random.choice(chars) for _ in range(length))
    return short_url


def is_valid_url(url):
    # Simple regex to check if the URL is valid
    regex = re.compile(
        r'^(?:http|ftp)s?://'  # http:// or https://
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
        r'localhost|'  # localhost...
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # ...or ipv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # ...or ipv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    return re.match(regex, url) is not None


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        long_url = request.form['long_url']
        # Check if the input is empty
        if not long_url:
            flash("Please enter a URL.", "error")
            return render_template("index.html")

            # Validate the URL
        if not is_valid_url(long_url):
            flash("Please enter a valid URL.", "error")
            return render_template("index.html")

        short_url = generate_short_url()
        while short_url in shortened_urls:
            short_url = generate_short_url()
        shortened_urls[short_url] = long_url

        # Return success message with the shortened URL
        flash(f"Shortened URL: {request.url_root}{short_url}", "success")
        return render_template("index.html")
    return render_template("index.html")


@app.route("/<short_url>")
def redirect_url(short_url):
    long_url = shortened_urls.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return "URL is not found", 404


if __name__ == "__main__":
    app.run(debug=True)
