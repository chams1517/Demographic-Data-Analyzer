import pandas as pd


def calculate_demographic_data(print_data=True):
    df = pd.read_csv(
        "adult.data.csv",
        names=[
            "age",
            "workclass",
            "fnlwgt",
            "education",
            "education-num",
            "marital-status",
            "occupation",
            "relationship",
            "race",
            "sex",
            "capital-gain",
            "capital-loss",
            "hours-per-week",
            "native-country",
            "salary"
        ],
        skipinitialspace=True
    )
    df = df[df["race"] != "race"]

    text_columns = [
        "workclass",
        "education",
        "marital-status",
        "occupation",
        "relationship",
        "race",
        "sex",
        "native-country",
        "salary"
    ]

    for column in text_columns:
        df[column] = df[column].astype(str).str.strip()

    df["age"] = pd.to_numeric(df["age"], errors="coerce")
    df["hours-per-week"] = pd.to_numeric(
        df["hours-per-week"], errors="coerce"
    )

    race_count = df["race"].value_counts()

    average_age_men = round(
        df[df["sex"] == "Male"]["age"].mean(), 1
    )

    percentage_bachelors = round(
        (df["education"] == "Bachelors").sum()
        / len(df) * 100,
        1
    )

    higher_education = df[
        df["education"].isin(
            ["Bachelors", "Masters", "Doctorate"]
        )
    ]

    lower_education = df[
        ~df["education"].isin(
            ["Bachelors", "Masters", "Doctorate"]
        )
    ]

    higher_education_rich = round(
        (higher_education["salary"] == ">50K").sum()
        / len(higher_education) * 100,
        1
    )

    lower_education_rich = round(
        (lower_education["salary"] == ">50K").sum()
        / len(lower_education) * 100,
        1
    )

    min_work_hours = df["hours-per-week"].min()

    min_workers = df[
        df["hours-per-week"] == min_work_hours
    ]

    min_work_hours_rich = round(
        (min_workers["salary"] == ">50K").sum()
        / len(min_workers) * 100,
        1
    )

    country_earning = (
        df.groupby("native-country")["salary"]
        .apply(lambda x: (x == ">50K").mean() * 100)
    )

    highest_earning_country = country_earning.idxmax()

    highest_earning_country_percentage = round(
        country_earning.max(), 1
    )

    india_rich = df[
        (df["native-country"] == "India")
        & (df["salary"] == ">50K")
    ]

    top_IN_occupation = (
        india_rich["occupation"]
        .value_counts()
        .index[0]
    )

    if print_data:
        print("Number of each race:")
        print(race_count)
        print("Average age of men:", average_age_men)
        print("Percentage with Bachelors degrees:",
              percentage_bachelors)
        print("Percentage with higher education that earn >50K:",
              higher_education_rich)
        print("Percentage without higher education that earn >50K:",
              lower_education_rich)
        print("Min work time:", min_work_hours, "hours/week")
        print("Percentage of rich among those who work minimum hours:",
              min_work_hours_rich)
        print("Country with highest percentage of rich:",
              highest_earning_country)
        print("Highest percentage of rich people in country:",
              highest_earning_country_percentage)
        print("Top occupations in India:", top_IN_occupation)

    return {
        "race_count": race_count,
        "average_age_men": average_age_men,
        "percentage_bachelors": percentage_bachelors,
        "higher_education_rich": higher_education_rich,
        "lower_education_rich": lower_education_rich,
        "min_work_hours": min_work_hours,
        "min_work_hours_rich": min_work_hours_rich,
        "highest_earning_country": highest_earning_country,
        "highest_earning_country_percentage":
            highest_earning_country_percentage,
        "top_IN_occupation": top_IN_occupation
    }