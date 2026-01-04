import pandas as pd

INPUT_FILE = "data/input.xlsx"
OUTPUT_FILE = "data/output.xlsx"


def load_data(path):
    df = pd.read_excel(path)
    return df


def validate_data(df):
    errors = []

    for index, row in df.iterrows():
        row_errors = []

        if pd.isna(row.get("name")):
            row_errors.append("Name is empty")

        age = row.get("age")
        if pd.isna(age):
            row_errors.append("Age is empty")
        elif not isinstance(age, (int, float)):
            row_errors.append("Age is not a number")
        elif age < 9:
            row_errors.append("He/She is a baby")
        elif age > 125:
            row_errors.append("He/She is not a human")

        errors.append(", ".join(row_errors))

    df["validation_errors"] = errors
    return df


def clean_data(df):
    df = df.dropna(subset=["name"])
    return df


def save_data(df, path):
    df.to_excel(path, index=False)
    print("Misson Accomplished./n" \
        f"Output saved to {path}")


def main():
    df = load_data(INPUT_FILE)
    df = validate_data(df)
    df = clean_data(df)
    save_data(df, OUTPUT_FILE)


if __name__ == "__main__":
    main()