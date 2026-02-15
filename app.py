"""
Envelope – Open Me, My Valentine.
Flask app: serves the envelope page and photos from the photos/ folder.
Run: flask --app app run  (or python app.py)
Deploy: same as dashboard (e.g. Render, Railway) — push to GitHub and connect the repo.
"""
import os
from flask import Flask, render_template, send_from_directory

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates"),
    static_folder=os.path.join(BASE_DIR, "static"),
)
PHOTOS_DIR = os.path.join(BASE_DIR, "photos")


@app.route("/")
def index():
    return render_template("envelope.html")


@app.route("/favicon.ico")
def favicon():
    return send_from_directory(app.static_folder, "favicon.ico", mimetype="image/x-icon")


@app.route("/envelope-config.js")
def envelope_config():
    """Serve config with no-cache so browser always loads latest on refresh."""
    r = send_from_directory(app.static_folder, "envelope-config.js", mimetype="application/javascript")
    r.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    r.headers["Pragma"] = "no-cache"
    return r


VIDEO_MIMETYPES = {
    ".mp4": "video/mp4",
    ".mov": "video/quicktime",
    ".webm": "video/webm",
}
PHOTO_MIMETYPES = {
    ".gif": "image/gif",
}


@app.route("/photos/<path:filename>")
def serve_photo(filename):
    """Serve images and videos from the photos/ folder so /photos/photo.jpg and /photos/video.mp4 work when hosted."""
    ext = os.path.splitext(filename)[1].lower()
    mimetype = VIDEO_MIMETYPES.get(ext) or PHOTO_MIMETYPES.get(ext)
    return send_from_directory(PHOTOS_DIR, filename, mimetype=mimetype)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5002))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(debug=debug, host="0.0.0.0", port=port)
