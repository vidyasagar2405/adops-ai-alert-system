import streamlit as st
import pandas as pd
import requests
import plotly.express as px

st.set_page_config(page_title="AI AdOps Dashboard",layout="wide")
st.title(":rainbow[AI AdOps Monitoring Dashboard]")

## n8n webhook URL
WEBHOOK_URL = "https://sagguautomation.app.n8n.cloud/webhook/7a4c374a-98bb-4b9f-87e3-6903bf5191f5"

if st.button("🔄 Run AI Analysis"):
    with st.spinner("Running n8n workflow + AI analysis..."):
        try:
            response = requests.post(WEBHOOK_URL,timeout=60)
            response.raise_for_status()
            data = response.json()

            # HANDLE RESPONSE FORMATS
            if isinstance(data, list):
                df = pd.DataFrame(data)
            elif isinstance(data, dict):
                inner = data.get("items")
                if inner:
                    df = pd.DataFrame(inner)
                else:
                    df = pd.DataFrame([data])
            else:
                st.error("Unexpected response format from n8n.")
                st.stop()

            # EMPTY CHECK
            if df.empty:
                st.warning("No alerts generated.")
                st.stop()
            st.success("Analysis Complete")

            # METRICS
            total_alerts = len(df)
            high_alerts = (len(df[df["severity"] == "High"]) if "severity" in df.columns else 0)
            affected_ssps = (df["ssp"].nunique() if "ssp" in df.columns else 0)

            col1, col2, col3 = st.columns(3)

            col1.metric("Total Alerts",total_alerts)
            col2.metric("High Severity",high_alerts)
            col3.metric("Affected SSPs",affected_ssps)
            st.divider()

            # CHARTS
            if ("campaign_id" in df.columns and "ctr_drop" in df.columns):
                st.subheader("CTR Drop by Campaign")
                fig = px.bar(df,x="campaign_id",y="ctr_drop",color="severity"if "severity" in df.columns else None,
                hover_data=["ssp","issue"] if "issue" in df.columns else None)

                st.plotly_chart(fig, use_container_width=True)
            st.divider()

            # CLEAN ALERT TABLE
            st.subheader(":blue[Campaign Alerts]")
            table_columns = []
            preferred_columns = ["campaign_id", "ssp", "severity", "ctr_drop", "ecpm_drop", "fill_drop", "issue"]

            for col in preferred_columns:
                if col in df.columns:
                    table_columns.append(col)
            table_df = df[table_columns]
            st.dataframe(table_df, use_container_width=True)
            st.divider()

            # AI RECOMMENDATIONS
            if "ai_recommendation" in df.columns:
                st.subheader(":blue[AI Recommendations]")
                for _, row in df.iterrows():
                    campaign = row.get("campaign_id", "Unknown")
                    severity = row.get("severity", "Unknown")
                    ssp = row.get("ssp","Unknown")
                    issue = row.get("issue","No issue")
                    recommendation = row.get("ai_recommendation","No recommendation generated.")
                    with st.expander(f"{campaign} | {severity}"):
                        st.markdown(f"""
### SSP
{ssp}

### Issue
{issue}

### AI Recommendation
{recommendation}
""")
        
        # ERROR HANDLING
        except requests.exceptions.Timeout:
            st.error("Request timed out. Check if your n8n workflow is active.")
        except requests.exceptions.RequestException as e:
            st.error(f"Failed to reach n8n webhook: {e}")
        except ValueError:
            st.error("Could not parse response as JSON.")
        except KeyError as e:
            st.error(f"Missing expected column in data: {e}")
            if 'df' in locals():
                st.write("Columns received:", df.columns.tolist())
        except Exception as e:
            st.error(f"Unexpected error: {e}")