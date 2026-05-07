# AI AdOps Monitoring Dashboard

An AI-powered AdOps monitoring and optimization system built using **n8n**, **Gemini AI**, **Google Sheets**, and **Streamlit**.

This project automatically detects campaign performance drops, analyzes root causes using AI, generates optimization recommendations, and visualizes alerts in a real-time dashboard.

---

# Features

* Automated AdOps anomaly detection
* CTR, eCPM, and Fill Rate monitoring
* AI-generated root cause analysis
* Revenue recovery recommendations
* Low-code automation workflow using n8n
* Interactive Streamlit dashboard
* Google Sheets integration for campaign data storage
* Real-time webhook-based execution

---

# Tech Stack

## Frontend

* Streamlit
* Plotly

## Automation

* n8n (Low-code workflow automation)

## AI Model

* Google Gemini API

## Data Storage

* Google Sheets

## Backend Processing

* Python
* Pandas
* Requests

---

# Workflow Architecture

```text
Streamlit Dashboard
        ↓
n8n Webhook Trigger
        ↓
Google Sheets Campaign Data
        ↓
Python Metric Processing
        ↓
Gemini AI Analysis
        ↓
Alert Generation
        ↓
Google Sheets Logging
        ↓
Dashboard Visualization
```

---

# Project Screenshots

## n8n Workflow
<img width="1289" height="532" alt="Screenshot 2026-05-07 at 12 17 54" src="https://github.com/user-attachments/assets/9f34a036-5c8b-410e-bb99-4252b073287a" />

## Streamlit Dashboard
<img width="1416" height="802" alt="Screenshot 2026-05-07 at 12 19 04" src="https://github.com/user-attachments/assets/4105cb1a-bacd-4998-a571-dffe27825ba0" />

---
# Application Link 
[live application](https://adops-ai-alert-system-9sqnycvwb7dzrv2sq3qt35.streamlit.app)


---

# Key Capabilities

## Performance Monitoring

The system compares:

* Yesterday CTR vs Today CTR
* Yesterday eCPM vs Today eCPM
* Yesterday Fill Rate vs Today Fill Rate

## AI Analysis

Gemini AI generates:

* Root cause analysis
* Optimization strategies
* Revenue recovery suggestions
* Priority severity assessment

## Dashboard Analytics

The dashboard displays:

* Total alerts
* High severity campaigns
* Affected SSPs
* Campaign performance drops
* AI recommendations

---

# Installation

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-adops-monitoring-dashboard.git
cd ai-adops-monitoring-dashboard
```

---

# Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Run Streamlit App

```bash
streamlit run frontend.py
```

---

# Requirements

```txt
streamlit
pandas
requests
plotly
```

---

# n8n Workflow Components

* Webhook Trigger
* Google Sheets Nodes
* Python Processing Node
* Merge Node
* Filter Node
* Gemini API HTTP Request
* Response Formatter
* Google Sheets Append Node

---

# Example AI Recommendation

```text
Root Cause:
- Significant CTR and eCPM drop caused by creative fatigue.

Optimization Actions:
- Rotate creatives
- Adjust floor pricing
- Run A/B testing

Revenue Recovery:
- Increase bids on high-performing placements
- Reallocate budget to higher-yield inventory
```

---

# Future Improvements

* Real-time alert notifications
* Slack/Email integration
* Predictive anomaly detection
* Multi-SSP benchmarking
* Historical trend analysis
* Authentication and role-based access

---

# Deployment

## Frontend

Deployed using Streamlit Community Cloud.

## Automation Backend

Hosted on n8n Cloud.

---

# Author

Vidyasagar

--
