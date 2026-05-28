import streamlit as st
import plotly.express as px
import pandas as pd
import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from agents.aqi_agent import AQIAgent
from tools.aqi_tool import get_air_quality
from utils.constants import (
    AVAILABLE_CITIES,
    POLLUTANT_LABELS
)

st.set_page_config(
    page_title="Environmental Intelligence Agent",
    page_icon="🌍",
    layout="wide"
)

st.title(
    "🌍 Environmental Intelligence AI Agent"
)

st.caption(
    "Real-time Air Quality Monitoring "
    "+ Conversational AI"
)

agent = AQIAgent()

#--------------------------------------------
# SIDEBAR
#--------------------------------------------

st.sidebar.header("Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "AQI Dashboard",
        "AI Assistant"
    ]
)

#==========================================
# AQI Dashboard
#==========================================

if page == "AQI Dashboard":
    st.header("Live Air Quality Dashboard")
    city = st.selectbox(
        "Select City",
        AVAILABLE_CITIES
    )


    if st.button("Analyze Air Quality"):

        data = get_air_quality(city)

        if data is None:
            st.error(
                "Could not fetch air quality data."
            )
            st.stop()

        row = data.iloc[0]

        st.success(
            f"Live Air Quality Analysis "
            f"for {city}"
        )

        st.markdown(
            f"""
            ## {row['indicator']}
            AQI Status:
            **{row['aqi_category']}**
            """
        )

        # KPI Section
        st.subheader("Key Pollution Metrics")

        col1, col2, col3, col4 = st.columns(4)

        col1.metric(
            "PM2.5",
            row["pm2_5"]
        )

        col2.metric(
            "PM10",
            row["pm10"]
        )

        col3.metric(
            "NO₂",
            row["nitrogen_dioxide"]
        )

        col4.metric(
            "CO",
            row["carbon_monoxide"]
        )

        st.divider()

        # Chart Section
        st.subheader(
            "Pollution Distribution"
        )

        pollutants = []

        for key, label in (
            POLLUTANT_LABELS.items()
        ):

            pollutants.append({
                "Pollutant": label,
                "Value": row[key]
            })

        pollutant_df = pd.DataFrame(
            pollutants
        )

        fig = px.bar(
            pollutant_df,
            x="Pollutant",
            y="Value",
            title=(
                f"Pollution Levels in "
                f"{city}"
            )
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # Health recommendation
        st.subheader(
            "🩺 Health Recommendation"
        )

        category = row[
            "aqi_category"
        ]

        if category == "Good":

            st.success(
                "Air quality is good. "
                "Outdoor activities "
                "are safe."
            )

        elif category == "Moderate":

            st.warning(
                "Moderate pollution. "
                "Sensitive individuals "
                "should limit exposure."
            )

        elif category == (
            "Unhealthy for "
            "Sensitive Groups"
        ):

            st.warning(
                "Sensitive groups "
                "should avoid prolonged "
                "outdoor activity."
            )

        elif category == "Unhealthy":

            st.error(
                "Poor air quality. "
                "Reduce outdoor "
                "activities."
            )

        else:

            st.error(
                "Avoid outdoor "
                "exposure if possible."
            )

        with st.expander(
            "View Raw AQI Data"
        ):
            st.dataframe(data)

#========================================
# AI Assistant
#========================================

elif page == "AI Assistant":

    st.header(
        "Environmental AI assistant"
    )

    st.caption(
        "Ask anything about "
        "air quality"
    )

    #Initialize chat history

    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Display old messages
    for message in (
        st.session_state.messages
    ):
        with st.chat_message(
            message["role"]
        ):
            st.markdown(
                message["content"]
            )
    
    # Chat input
    prompt = st.chat_input(
        "Ask about AQI..."
    )

    if prompt:

        # Show user message
        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        with st.chat_message(
            "user"
        ):
            st.markdown(prompt)

        # Generative AI response
        with st.chat_message(
            "assistant"
        ):
            
            with st.spinner(
                "Thinking..."
            ):
                response = (
                    agent.generate_response(
                        prompt,
                        st.session_state.messages
                    )
                )
                st.markdown(
                    response
                )
        
        # Save assistance response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response
        })