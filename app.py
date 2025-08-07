import streamlit as st
import io

# Title
st.title("💸 Finance Prompt Generator")
st.markdown("Select a finance category and sub-topic to get a reusable AI prompt.")

# Prompt library structure
prompt_library = {
    "Financial Analysis & Reporting": {
        "Ratio Analysis": "Guide me through conducting a [profitability/liquidity/leverage] ratio analysis for a [type of company, e.g., SaaS], using these figures: [insert data]. Explain each ratio, calculation, and interpretation.",
        "Vertical & Horizontal Analysis": "Perform vertical and horizontal analysis for the following income statement [insert table or data]. Present findings with key takeaways and trends.",
        "Financial Commentary": "Draft a quarterly financial statement commentary highlighting revenue trends, margin movement, cost drivers, and forward-looking risks for a [industry] company."
    },
    "Forecasting & Budgeting": {
        "Revenue Forecasting": "Create a 12-month revenue forecast using historical data for the past 3 years. Assume a compound annual growth rate of [X%] and explain your forecasting method.",
        "Rolling Forecast Model": "Design a 3-year rolling forecast template for a [industry] company with seasonal fluctuations. Suggest assumption drivers and KPIs to monitor.",
        "Budget Variance Commentary": "Provide a narrative explanation for budget variances in operating expenses vs. actuals for Q2. Focus on marketing, COGS, and labor costs."
    },
    "Cash Flow & Treasury": {
        "Liquidity KPIs": "Calculate and interpret the Current Ratio, Quick Ratio, and Cash Ratio for the following data: [insert figures]. Provide clear steps and implications.",
        "Cash Flow Optimization": "Suggest strategies to improve operating cash flow for a retail company facing seasonal dips in revenue.",
        "Treasury Dashboard Design": "Design a cash management dashboard showing inflows, outflows, cash burn, and runway. Recommend visuals and KPIs."
    },
    "Investment & Valuation": {
        "DCF Valuation": "Perform a DCF valuation for a startup using assumed free cash flows for 5 years and a WACC of [X%]. Include terminal value and sensitivity analysis.",
        "IRR / NPV Simulation": "Calculate the IRR and NPV of a real estate investment given initial investment, projected cash flows, and discount rate. Show steps and interpretation.",
        "Scenario Planning": "Build a prompt chain to evaluate best case, base case, and worst-case financial projections for a manufacturing business."
    },
    "Strategic Finance & Board-Level Insights": {
        "Strategic Options Evaluation": "Compare financial impact of three strategic options: cost-cutting, market expansion, and product diversification. Use financial metrics like ROI and payback period.",
        "Board Memo Drafting": "Draft a board-level financial summary for Q3, focusing on EBITDA movement, debt metrics, and strategic risks. Keep it under 300 words.",
        "Investment Committee Brief": "Prepare a one-pager investment brief for a new project requiring SAR 100M, with IRR, DSCR, payback, and SWOT highlights."
    },
    "Compliance, Audit & Risk": {
        "Zakat / VAT Compliance (Saudi Arabia)": "Generate a checklist to ensure Zakat and VAT compliance for a KSA-based real estate company for FY2025.",
        "Risk Assessment Matrix": "Create a risk matrix identifying top 5 financial risks for a capital-intensive business. Include likelihood, impact, and mitigation strategies.",
        "Audit Working Paper Prompt": "Structure an audit working paper for testing accounts payable balances under ISA standards. Include sampling method and conclusion template."
    },
    "Excel & Power BI Automation": {
        "Excel Financial Model": "Guide me in building a dynamic 3-statement Excel model with linked assumptions, schedules, and dashboards for a startup.",
        "Power BI Dashboard Prompt": "Design a Power BI dashboard layout for monthly performance review, with Revenue, Gross Margin %, Operating Profit, and Cash Flow.",
        "Excel Formula Explanation": "Explain how to use Excel's OFFSET and MATCH formulas to build a dynamic range for a rolling forecast."
    },
    "ESG & Sustainability Reporting": {
        "ESG Report Generator": "Draft an ESG report section for a manufacturing company under GRI standards, focusing on environmental KPIs.",
        "ESG Score Estimation": "Estimate an ESG score for a real estate developer using qualitative input under IFRS S2 and CDP frameworks.",
        "Regulatory Tracker Prompt": "Summarize upcoming ESG regulatory requirements impacting listed companies in the GCC region. Provide deadlines and data requirements."
    }
}

# User selections
category = st.selectbox("Select Finance Domain", list(prompt_library.keys()))
sub_topic = st.selectbox("Select Sub-topic", list(prompt_library[category].keys()))
selected_prompt = prompt_library[category][sub_topic]

# Display the prompt
st.subheader("💬 Generated Prompt")
st.code(selected_prompt, language="text")

# Enable download as .txt file
buffer = io.BytesIO()
buffer.write(selected_prompt.encode('utf-8'))
buffer.seek(0)

st.download_button(
    label="📥 Download Prompt as .txt",
    data=buffer,
    file_name="finance_prompt.txt",
    mime="text/plain"
)

# User guidance
st.info("Use this prompt in ChatGPT, GROQ, or any AI assistant for finance insights.")
