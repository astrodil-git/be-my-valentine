# Envelope – Open Me, My Valentine

One-page envelope animation. Add your photos, run one command (or deploy from GitHub), and share the link. Works on phone and desktop.

---

## 1. Add your files to `photos/`

| File | Where it appears |
|------|------------------|
| `photo.jpg` | Main photo |
| `filmstrip1.jpg`, `filmstrip2.jpg`, `filmstrip3.jpg` | Filmstrip frames |
| `video.mp4` | Video after you open all items and dock the last one |

---

## 2. Run it (one command)

From the **Envelope Animation App** folder:

```bash
bash run.sh
```

Then open **http://localhost:5002** in your browser. The script creates a venv and installs Flask the first time; after that it just starts the app.

---

## 3. Put it on GitHub and host it

1. **Push this folder to a GitHub repo** (create a new repo, then push `app.py`, `requirements.txt`, `run.sh`, `templates/`, `photos/`, and `render.yaml`).

2. **Deploy on Render (free)**  
   - Go to [render.com](https://render.com) → sign in with GitHub.  
   - **New** → **Web Service** → connect your repo.  
   - Render will use **`render.yaml`** in the repo to build and start the app (no extra config).  
   - You get a URL like `https://your-app.onrender.com` — open it on any device and it works.

Once deployed, the site runs by itself; when someone loads the URL, they get the envelope and can interact with it (open, slide out, video) with no extra steps.
