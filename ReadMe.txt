
# Pension Fund Analysis - Portfolio Project

## Project Overview

**Title:** Pension Fund Analysis for Stakeholder Insights  
**Objective:** To analyze simulated pension fund data, offering stakeholders actionable insights on retirement readiness, contribution patterns, risk profiles, and other essential metrics for informed decision-making.

### Skills Demonstrated
- **Data Analysis and Manipulation:** Python (Pandas)
- **Statistical Summaries and Reporting**
- **Data Visualization:** Power BI, Matplotlib, Seaborn
- **Stakeholder Communication and Reporting**

---

## Table of Contents

- [Data Source](#data-source)
- [Installation Instructions](#installation-instructions)
- [Usage Instructions](#usage-instructions)
- [Key Analyses and Queries](#key-analyses-and-queries)
- [Visualizations in Power BI and Python](#visualizations-in-power-bi-and-python)
- [Stakeholder Summary Report](#stakeholder-summary-report)
- [Skills and Tools Utilized](#skills-and-tools-utilized)
- [Reflections and Learning Outcomes](#reflections-and-learning-outcomes)
- [Future Improvements](#future-improvements)
- [License](#license)

---

## Data Source

This project uses a simulated dataset representing pension fund data for 4,000 individuals over a 50-year period. The dataset includes critical information on individual contributions, balances, withdrawals, risk profiles, income levels, and healthcare expenses.

---

## Installation Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Akinwale2907/Pension-Analysis
   cd pension-fund-analysis
   ```

2. **Install required packages:**
   Ensure you have Python 3.x installed. Install necessary Python packages using:
   ```bash
   pip install -r requirements.txt
   ```
   The `requirements.txt` file includes:
   - Pandas
   - Matplotlib
   - Seaborn
   - Jupyter (optional, for interactive notebooks)

3. **Power BI Setup (optional):**
   To visualize data interactively, use Power BI Desktop. Download it [here](https://powerbi.microsoft.com/en-us/desktop/).

---

## Usage Instructions

1. **Run Jupyter Notebooks (Optional):**
   If using Jupyter Notebooks for interactive analysis, launch it using:
   ```bash
   jupyter notebook
   ```
   Open the appropriate notebook files and follow the cells to conduct the analysis.

2. **Execute Python Scripts:**
   Run the main analysis script to generate insights:
   ```bash
   python analysis_script.py
   ```

3. **Power BI Dashboard:**
   Open the Power BI file (`pension_analysis_dashboard.pbix`) to explore interactive visualizations.

---

## Key Analyses and Queries

The following analyses provide insights into retirement readiness, contribution patterns, risk profiles, and other areas of interest:

### A. Summary Statistics
- **Objective:** Provide a summary of balances, contributions, and withdrawals.
- **Query:** `df.describe()` to calculate assets under management.

### B. Balance Progression by Age
- **Objective:** Track average balance growth for compound growth insights.
- **Query:** `avg_balance_by_age = df.groupby('Age')['Balance'].mean()`

### C. Retirement Readiness
- **Objective:** Identify individuals meeting a $500,000 balance target at retirement.
- **Query:** `retirement_ready = df[(df['Age'] == 65) & (df['Balance'] >= 500000)]`

### D. Contribution Patterns by Occupation and Income
- **Objective:** Compare average contributions across occupations and income levels.
- **Query:** `avg_contribution_by_occupation = df.groupby('Occupation')['Contribution'].mean()`

### E. Risk Profile Performance
- **Objective:** Assess performance across different risk profiles.
- **Query:** `risk_profile_performance = df.groupby('Risk_Profile')[['Balance', 'Annual_Return_Rate']].mean()`

### F. Lifetime Contribution vs. Withdrawal
- **Objective:** Calculate net savings by comparing cumulative contributions to withdrawals.
- **Query:** `lifetime_contrib_withdraw = df.groupby('Individual_ID')[['Contribution', 'Withdrawal']].sum()`

### G. Healthcare Costs in Retirement
- **Objective:** Summarize healthcare expenses in the last five years of life expectancy.
- **Query:** `healthcare_costs = df[(df['Age'] >= df['Life_Expectancy'] - 5) & (df['Employment_Status'] == 'Retired')]`

---

## Visualizations in Power BI and Python

### Power BI Dashboard:
- **Average Balance by Age:** Line chart
- **Contribution Patterns by Occupation:** Bar chart
- **Risk Profile Distribution:** Pie chart
- **Lifetime Contribution vs. Withdrawal:** Scatter plot

### Python Visualizations (Matplotlib):
- **Balance Progression by Age:** Line chart for compound growth
- **Final Balance Distribution at Retirement:** Histogram for balance distribution at retirement age

---

## Stakeholder Summary Report

A detailed report was generated with the following key sections:

- **Executive Summary:** High-level objectives and data insights.
- **Key Findings:** Insights on balance progression, risk profiles, and contribution patterns.
- **Recommendations:** Suggestions for enhancing fund performance and contributor support.

---

## Skills and Tools Utilized

- **Python (Pandas, Matplotlib, Seaborn):** For data analysis, manipulation, and visualizations.
- **Power BI:** For creating interactive dashboards.
- **Data Querying:** Advanced grouping and filtering to generate insights.
- **Reporting:** PDF reports summarizing actionable insights and recommendations.

---

## Reflections and Learning Outcomes

This project provided experience in:

- **Data Storytelling:** Translating complex datasets into accessible insights.
- **Interactive Reporting:** Using Power BI to create user-friendly dashboards.

---

## Future Improvements

To enhance the project, future improvements could include:

- **Predictive Modeling:** Implement predictive models for various retirement scenarios.
- **Scenario Testing:** Integrate Power BI’s What-If parameters for interactive scenario exploration.
- **Demographic Segmentation:** Segment analyses by demographics for tailored insights.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

--- 

This README provides a detailed summary of the project’s objectives, analyses, and outcomes, while offering installation and usage instructions to ensure seamless setup for new users.
