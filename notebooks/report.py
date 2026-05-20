import marimo as mo

app = mo.App(title="Event Duration Analysis")

@app.cell
def __():
    import pandas as pd
    import matplotlib.pyplot as plt
    return pd, plt

@app.cell
def __(mo):
    mo.md("# Reproducible Data Pipeline Report")
    return

@app.cell
def __(pd):
    # Load the output file from your DVC features stage
    df = pd.read_csv("data/features/events.csv")
    return df,

@app.cell
def __(df, plt):
    # Generate the histogram for duration_minutes
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(df['duration_minutes'], bins=30, edgecolor='black', alpha=0.7)
    ax.set_title("Distribution of Event Durations")
    ax.set_xlabel("Duration (Minutes)")
    ax.set_ylabel("Frequency")
    plt.tight_layout()
    return fig, ax

if __name__ == "__main__":
    app.run()
