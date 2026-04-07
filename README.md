# 🌟 Stash — Notes App

**Stash** is a fast, lightweight, API-first notes app.  
Store and manage notes & folders entirely via **HTTP APIs**, **Postman**, or **cURL** — no frontend required.  
Perfect for devs, scripts, automation, or running headless on a server.

> ⚠️ **Work in progress** — actively developed, expect breaking changes.  
> 🎨 **A simple UI is planned** — Stash is built API-first, with a minimal web interface coming in a future release.

---

## 🚀 Features

- 🗂 **Folders** — Create, list, update, delete folders
- 📝 **Notes** — Create, list, update, delete, filter notes by folder
- ⚡ **API-First** — Fully usable via cURL, Postman, or any HTTP client
- 🛠 **SQLite** — Lightweight, zero-config database
- 🐳 **Docker-ready** — Run anywhere, no local install needed

---

## 📁 Project Structure

```
Stash/
│
├── utils/
│   └── sql_utils.py
├── data/
│   └── notes.db
├── app.py
├── requirements.txt
└── Dockerfile
```

---

## 🌐 Architecture

```
┌─────────────────┐        HTTP        ┌──────────────────────────┐
│   Client PC     │  ──────────────►   │  Server (Docker)         │
│   (terminal)    │                    │  app.py + notes.db       │
└─────────────────┘                    └──────────────────────────┘
```

From any machine on the network — no client install needed, just a terminal.

---

## ⚡ Quick Start

### Without Docker

```bash
git clone https://github.com/dasabhijeet/Stash.git
cd Stash
pip install -r requirements.txt
python app.py
```

### With Docker

```bash
docker build -t stash .
docker run -d -p 6969:6969 --name stash stash
```

API will be live at `http://localhost:6969` or `http://<server-ip>:6969` from any machine on the network.

---

## 🔥 API Endpoints

### Folders

| Method | Endpoint | Description |
|---|---|---|
| POST | `/folders` | Create a folder |
| GET | `/folders` | List all folders |
| PUT | `/folders/{id}` | Update a folder |
| DELETE | `/folders/{id}` | Delete a folder and its notes |

### Notes

| Method | Endpoint | Description |
|---|---|---|
| POST | `/notes` | Create a note |
| GET | `/notes` | List all notes |
| GET | `/notes/{folder_id}` | List notes by folder |
| PUT | `/notes/{note_id}` | Update a note |
| DELETE | `/notes/{note_id}` | Delete a note |

---

## 💡 cURL Examples

```bash
# ── FOLDERS ──────────────────────────────────────────────────────

# Create folders
curl -X POST http://localhost:6969/folders -H "Content-Type: application/json" -d '{"name":"GYM","description":"Workout notes"}'
curl -X POST http://localhost:6969/folders -H "Content-Type: application/json" -d '{"name":"Work","description":"Office tasks"}'
curl -X POST http://localhost:6969/folders -H "Content-Type: application/json" -d '{"name":"Recipes","description":"Food and cooking"}'
curl -X POST http://localhost:6969/folders -H "Content-Type: application/json" -d '{"name":"Travel","description":"Trip plans"}'

# List all folders
curl http://localhost:6969/folders

# Update a folder
curl -X PUT http://localhost:6969/folders/1 -H "Content-Type: application/json" -d '{"name":"GYM Updated","description":"New description"}'

# Delete a folder (also deletes its notes)
curl -X DELETE http://localhost:6969/folders/1


# ── NOTES ────────────────────────────────────────────────────────

# Create notes in GYM (folder_id=1)
curl -X POST http://localhost:6969/notes -H "Content-Type: application/json" -d '{"folder_id":1,"title":"Day 1","content":"Bench press 5x5, squats 3x8"}'
curl -X POST http://localhost:6969/notes -H "Content-Type: application/json" -d '{"folder_id":1,"title":"Day 2","content":"Deadlift 4x5, pull-ups 3x10"}'

# Create notes in Work (folder_id=2)
curl -X POST http://localhost:6969/notes -H "Content-Type: application/json" -d '{"folder_id":2,"title":"Meeting","content":"Discuss Q2 roadmap with team"}'
curl -X POST http://localhost:6969/notes -H "Content-Type: application/json" -d '{"folder_id":2,"title":"TODO","content":"Fix login bug, review PRs, update docs"}'

# Create notes in Recipes (folder_id=3)
curl -X POST http://localhost:6969/notes -H "Content-Type: application/json" -d '{"folder_id":3,"title":"Pasta","content":"Boil pasta, add tomato sauce, top with cheese"}'

# Create notes in Travel (folder_id=4)
curl -X POST http://localhost:6969/notes -H "Content-Type: application/json" -d '{"folder_id":4,"title":"Goa Trip","content":"Book flights, hotel near beach, pack sunscreen"}'

# List all notes
curl http://localhost:6969/notes

# List notes by folder
curl http://localhost:6969/notes/1
curl http://localhost:6969/notes/2
curl http://localhost:6969/notes/3
curl http://localhost:6969/notes/4

# Update a note
curl -X PUT http://localhost:6969/notes/1 -H "Content-Type: application/json" -d '{"title":"Day 1 Updated","content":"Bench press 6x5, squats 4x8"}'

# Delete a note
curl -X DELETE http://localhost:6969/notes/1
```

---

## 🛠 Tech Stack

| Layer | Tool |
|---|---|
| API | FastAPI |
| Server | Uvicorn |
| Database | SQLite |
| Container | Docker |
| Language | Python 3.11 |

---

## 📌 Why Stash?

- Zero frontend, zero browser — just HTTP
- Works over the network from any terminal
- Perfect for scripts and automation
- Lightweight and fully portable via Docker
- Built API-first so any UI can be layered on top later

---

## 🗺 Roadmap

- [x] Folders CRUD
- [x] Notes CRUD
- [x] Docker support
- [ ] Simple web UI
- [ ] Search across notes
- [ ] Authentication

---

## 💖 Contributing

- Fork the repo
- Submit PRs or open issues
- ⭐ Star the project if you find it useful

---

## ⚡ License

MIT License — do whatever you want 💥
