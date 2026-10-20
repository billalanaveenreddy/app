# CareWatch – Health Monitoring Dashboard

A Streamlit dashboard prototype for monitoring elderly patients: a patient overview, key vitals and a recent activity feed in one screen.

## Features
- Summary cards (patients monitored, alerts, status)
- Patient grid with status labels (Stable / Monitor / Critical)
- Patient detail panel with six vitals and an activity feed
- "Add patient" and "Log vitals" forms with on-screen confirmations

> Prototype: uses sample data (no database yet) to demonstrate the UI and workflow.

## Tech
Python · Streamlit · HTML/CSS · Tabler Icons

## Run it
```bash
pip install streamlit
streamlit run app.py
```

## Next steps
- Connect to a real data source (CSV / SQL) and persist entries
- Add trend charts for vitals and alert thresholds
