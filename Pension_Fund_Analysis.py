
# Pension Fund Analysis for Stakeholder Insights
# This script performs key analyses on a simulated pension fund dataset for stakeholder reporting.

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data
df = pd.read_csv('realistic_pension_simulation.csv')

# Summary Statistics
def summary_statistics(df):
    """Provide high-level statistics on balances, contributions, and withdrawals."""
    summary_stats = df[['Balance', 'Contribution', 'Withdrawal']].describe()
    total_assets = df['Balance'].sum()
    print("Summary Statistics:\n", summary_stats)
    print("Total Assets Under Management:", total_assets)

# Average Balance Progression by Age
def plot_avg_balance_by_age(df):
    """Plot the average balance progression over time by age."""
    avg_balance_by_age = df.groupby('Age')['Balance'].mean()
    plt.figure(figsize=(10, 6))
    avg_balance_by_age.plot(kind='line')
    plt.title('Average Balance by Age')
    plt.xlabel('Age')
    plt.ylabel('Average Balance')
    plt.grid()
    plt.show()

# Retirement Readiness Analysis
def retirement_readiness(df, target_balance=500000):
    """Identify individuals with balances meeting or exceeding the target at retirement age."""
    retirement_ready = df[(df['Age'] == 65) & (df['Balance'] >= target_balance)]
    print("Individuals Ready for Retirement:\n", retirement_ready[['Individual_ID', 'Balance']])

# Contribution Patterns by Occupation and Income Level
def contribution_by_occupation_and_income(df):
    """Compare average annual contributions across different occupations and income levels."""
    avg_contribution_by_occupation = df.groupby('Occupation')['Contribution'].mean()
    avg_contribution_by_income_level = df.groupby('Income_Level')['Contribution'].mean()
    print("Average Contribution by Occupation:\n", avg_contribution_by_occupation)
    print("Average Contribution by Income Level:\n", avg_contribution_by_income_level)

# Risk Profile Performance Analysis
def risk_profile_performance(df):
    """Analyze performance across different risk profiles."""
    risk_profile_performance = df.groupby('Risk_Profile')[['Balance', 'Annual_Return_Rate']].mean()
    print("Risk Profile Performance:\n", risk_profile_performance)

# Lifetime Contribution vs. Withdrawal Analysis
def lifetime_contribution_vs_withdrawal(df):
    """Calculate total contributions and withdrawals per individual."""
    lifetime_contrib_withdraw = df.groupby('Individual_ID')[['Contribution', 'Withdrawal']].sum()
    lifetime_contrib_withdraw['Net_Savings'] = lifetime_contrib_withdraw['Contribution'] - lifetime_contrib_withdraw['Withdrawal']
    print("Lifetime Contribution vs. Withdrawal:\n", lifetime_contrib_withdraw)

# Healthcare Costs in Retirement
def healthcare_costs_in_retirement(df):
    """Summarize total healthcare expenses for retirees in the last five years of life expectancy."""
    healthcare_costs = df[(df['Age'] >= df['Life_Expectancy'] - 5) & (df['Employment_Status'] == 'Retired')]
    total_health_expense = healthcare_costs.groupby('Individual_ID')['Health_Expense'].sum()
    print("Total Healthcare Expense in Last 5 Years:\n", total_health_expense)

# Plot Examples
def plot_contribution_by_occupation(df):
    avg_contribution_by_occupation = df.groupby('Occupation')['Contribution'].mean().reset_index()
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Occupation', y='Contribution', data=avg_contribution_by_occupation)
    plt.title('Average Contribution by Occupation')
    plt.xlabel('Occupation')
    plt.ylabel('Average Contribution')
    plt.xticks(rotation=45)
    plt.show()

# Main execution
if __name__ == "__main__":
    print("Running Pension Fund Analysis...")
    summary_statistics(df)
    plot_avg_balance_by_age(df)
    retirement_readiness(df)
    contribution_by_occupation_and_income(df)
    risk_profile_performance(df)
    lifetime_contribution_vs_withdrawal(df)
    healthcare_costs_in_retirement(df)
    plot_contribution_by_occupation(df)
    print("Analysis complete.")
