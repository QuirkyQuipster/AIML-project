## Diamond Price Predictor (Flask)

A simple Flask web app that predicts diamond prices using a machine learning model trained on a public diamonds dataset. The app provides a form where you enter diamond attributes and receive a predicted price.

### Features
- **Interactive form UI** to input diamond attributes
- **On-start training** of a `RandomForestRegressor` model using a public CSV
- **Server-side preprocessing** (outlier filtering and categorical mappings)
- **Immediate prediction** after form submission

### Tech Stack
- **Backend**: Python, Flask
- **ML**: scikit-learn, pandas
- **Templates**: HTML/Jinja2 (`index.html`, `dform.html`)

---

## Project Structure
- `app/app.py`: Flask app, data loading, preprocessing, model training, and routes
- `app/templates/index.html`: Landing page with link to predictor form
- `app/templates/dform.html`: Prediction form and result display
- `app/requirements.txt`: Python dependencies
- `app/start.sh`: Convenience script to run the app

---

## Dataset
- Loaded at runtime from: [diamond.csv (GitHub)](https://raw.githubusercontent.com/sarwansingh/Python/master/ClassExamples/data/diamond.csv)

### Preprocessing (as implemented)
- Drops column: `Unnamed: 0`
- Encodes categories:
  - **cut**: `Premium→1`, `Ideal→2`, `Good→3`, `Very Good→4`, `Fair→5`
  - **color**: `D→1`, `E→2`, `F→3`, `G→4`, `H→5`, `I→6`, `J→7`
  - **clarity**: `I1→1`, `SI2→2`, `SI1→3`, `VS2→4`, `VS1→5`, `VVS2→6`, `VVS1→7`, `IF→8`
- Removes rows where any of `x`, `y`, `z` equals `0`
- Outlier filtering:
  - `45 < depth < 75`
  - `40 < table < 80`
  - `x < 30`, `y < 30`, `2 < z < 30`

### Model
- `RandomForestRegressor` trained on features: `carat, cut, color, clarity, depth, table, x, y, z`

---

## Getting Started

### Prerequisites
- Python 3.9+
- Git (for cloning/pushing)

### Setup
```bash
# 1) Create and activate a virtual environment (recommended)
python -m venv .venv
# Windows PowerShell
. .venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

# 2) Install dependencies
pip install -r app/requirements.txt
```

### Run the App
```bash
# Option A: from project root
cd app
python app.py

# Option B: on Unix-like systems
sh start.sh
```

Then open the app in your browser at `http://127.0.0.1:5000/`.

---

## How to Use
1. Open the home page and click “Diamond Price Predictor System”.
2. Fill in the fields:
   - **Carat** (e.g., 0.2–5.0)
   - **Cut** (Premium/Ideal/Good/Very Good/Fair)
   - **Color** (D–J)
   - **Clarity** (I1, SI2, SI1, VS2, VS1, VVS2, VVS1, IF)
   - **Depth**, **Table**, **Length (x)**, **Width (y)**, **Height (z)**
3. Submit to see the predicted price (in USD).

---

## Endpoints
- `GET /` → Home page
- `GET /dproject` → Prediction form
- `POST /dpredict` → Accepts form fields `carat, cut, color, clarity, depth, table, x, y, z`; returns rendered page with prediction

---

## Notes & Limitations
- The model is trained at server startup on the remote CSV. First request may take longer due to data load/train.
- No model persistence; for production, consider saving/loading a trained model and using a preprocessing pipeline.
- Inputs are minimally validated; ensure values are within reasonable ranges.
- Default Flask development server is used; for production, use a WSGI server (e.g., gunicorn/uwsgi) behind a reverse proxy.

---

## Development
- Dependencies are listed in `app/requirements.txt`:
  - `flask`, `pandas`, `scikit-learn`
- HTML templates live in `app/templates/`.

---

## License
MIT License. See `app/LICENSE`.

---

## Acknowledgments
- Dataset source credit to the original publisher as referenced above.