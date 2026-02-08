import pandas as pd

REQUIRED_COLUMNS = [
    "Equipment Name",
    "Type",
    "Flowrate",
    "Pressure",
    "Temperature"
]

def analyze_csv(file):
    df = pd.read_csv(file)

    # Validate columns
    for col in REQUIRED_COLUMNS:
        if col not in df.columns:
            raise ValueError(f"Missing column: {col}")

    summary = {
        "total_equipment": int(len(df)),
        "average_flowrate": round(df["Flowrate"].mean(), 2),
        "average_pressure": round(df["Pressure"].mean(), 2),
        "average_temperature": round(df["Temperature"].mean(), 2),
        "type_distribution": df["Type"].value_counts().to_dict(),
    }

    return summary
