# STATIFY

simple spotify analyzer

## Project Structure

```
statify/
├── backend/
│   ├── main.py              # The FastAPI application and endpoint routes
│   ├── spotify_client.py    # Spotipy logic for authentication and fetching data
│   ├── requirements.txt     # Python dependencies (fastapi, uvicorn, spotipy, etc.)
│   └── .env
├── frontend/
│   ├── index.html           # The main dashboard HTML layout
│   ├── css/
│   │   └── style.css        # Custom styling and CSS grid/flexbox layouts
│   └── js/
│       └── app.js           # Fetch API calls to the backend and Chart.js rendering
├── .gitignore
└── README.md
```
