# RE·ANALYZE — Market Intelligence Dashboard

Hyderabad residential real-estate market intelligence: supply, pricing, infrastructure, RERA, and buyer insights.

**Product:** RE·ANALYZE by ASBL  
**Stack:** Flask · MongoDB · ECharts · Leaflet  
**Local:** `http://localhost:5000`

---

## What it does

Authenticated users pick a city / locality (or radius) and load live panels from MongoDB:

- Supply KPIs, project map, tower / unit mix  
- Pricing intelligence (ASBL vs market)  
- Infrastructure & POI proximity  
- Buyer persona & demand signals  
- RERA / approval overlays  

The UI is a single `index.html` dashboard; Flask serves pages + JSON APIs; `mongo_supply.py` queries and normalizes `projects_master` and related collections.

---

## Quick start (local)

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# MongoDB must be running locally (or set MONGO_URI)
python app.py
```

Open [http://localhost:5000](http://localhost:5000) → login → `/dashboard`.

---

## Project layout (product surface)

| Path | Role |
|------|------|
| `app.py` | Flask routes, auth, REST APIs |
| `mongo_supply.py` | Mongo queries + normalizers |
| `index.html` | Dashboard UI |
| `templates/` | Landing, login, signup |
| `MARKET_INTELLIGENCE_DASHBOARD.md` | Full technical reference |

---

## Vercel note

The **static UI** (landing + dashboard shell) can be hosted on Vercel. **Live analysis APIs need MongoDB** (local or Atlas). Without a cloud Mongo URI and a Python/serverful backend, Analyze panels will not load live data on Vercel.

Set `MONGO_URI` only via environment variables — never commit credentials.

---

## Related work

See the [GitHub profile](https://github.com/lekha1221) for other products: **SAMVADA** (CRM email intelligence), **Prospect Model / KaalBhojaditya** (lead web-behaviour metrics), and more.

---

## License

Private / internal ASBL tooling unless otherwise stated.
