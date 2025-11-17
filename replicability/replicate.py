import pandas as pd
import numpy as np
import argparse
import statsmodels.api as sm
import statsmodels.formula.api as smf
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer

def load_data(path="data.csv"):
    df = pd.read_csv(path)

    # Compute skin tone
    df["skin"] = df[["rater1", "rater2"]].mean(axis=1)

    # Binary skin tone
    df["skin_binary"] = (df["skin"] >= 0.5).astype(int)

    # Binary red card
    df["red_dummy"] = (df["redCards"] > 0).astype(int)

    # Convert birthday to datetime → compute age
    df["birthday"] = pd.to_datetime(df["birthday"], errors="coerce", dayfirst=True)
    df["age"] = 2013 - df["birthday"].dt.year  # season 2012–2013

    return df


def encode_position(df, mode):
    if mode == "onehot":
        return pd.get_dummies(df, columns=["position"], drop_first=True)
    elif mode == "ordinal":
        df["position"] = df["position"].astype("category").cat.codes
        return df
    elif mode == "drop":
        return df.drop(columns=["position"])
    else:
        raise ValueError("Unknown encoding mode.")


def handle_missing(df, strategy):
    if strategy == "dropna":
        return df.dropna()

    elif strategy == "mean":
        # Impute only numerical columns
        num_cols = df.select_dtypes(include=[np.number]).columns
        imputer = SimpleImputer(strategy="mean")
        df[num_cols] = imputer.fit_transform(df[num_cols])
        return df

    else:
        raise ValueError("Unknown missing data strategy.")


def scale(df, do_scale):
    if not do_scale:
        return df
    scaler = StandardScaler()
    num_cols = df.select_dtypes(include=[np.number]).columns
    df[num_cols] = scaler.fit_transform(df[num_cols])
    return df


def build_formula(args):
    """Build statistical formula based on selected variations."""

    # Outcome
    if args.outcome == "linear":
        outcome = "redCards"
    elif args.outcome == "logit":
        outcome = "red_dummy"
    elif args.outcome == "poisson":
        outcome = "redCards"
    else:
        raise ValueError("Invalid outcome.")

    # Main predictor
    if args.skin == "continuous":
        skin_var = "skin"
    elif args.skin == "binary":
        skin_var = "skin_binary"
    else:
        raise ValueError("Invalid skin type.")

    # Covariates
    if args.cov == "none":
        covariates = ""
    elif args.cov == "physical":
        covariates = " + height + weight + age"
    elif args.cov == "performance":
        covariates = " + games + victories + defeats + goals"
    elif args.cov == "full":
        covariates = " + height + weight + games + goals + victories + age + yellowCards"
    else:
        raise ValueError("Invalid covariate option.")

    formula = f"{outcome} ~ {skin_var}{covariates}"
    return formula, outcome


def run_replication(args):
    df = load_data()
    df = encode_position(df, args.position)
    df = handle_missing(df, args.missing)
    df = scale(df, args.scale)

    formula, outcome = build_formula(args)

    print("\n=== Running model with formula ===")
    print(formula)

    # Model selection
    if args.outcome == "logit":
        model = smf.logit(formula, data=df).fit()
    elif args.outcome == "poisson":
        model = smf.poisson(formula, data=df).fit()
    else:  # linear model
        model = smf.ols(formula, data=df).fit()

    print("\n=== Replication Results ===")
    print(f"Skin variable: {args.skin}")
    print(f"Outcome: {args.outcome}")
    print(f"Model: {args.model}")
    print(f"Covariates: {args.cov}")
    print(f"Missing: {args.missing}")
    print(f"Position: {args.position}\n")

    print(model.summary())


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    # outcome
    parser.add_argument("--outcome", default="logit", choices=["linear", "logit", "poisson"])

    # skin tone type
    parser.add_argument("--skin", default="continuous", choices=["continuous", "binary"])

    # variations
    parser.add_argument("--cov", default="performance")
    parser.add_argument("--missing", default="dropna")
    parser.add_argument("--position", default="onehot")
    parser.add_argument("--scale", action="store_true")
    parser.add_argument("--model", default="glm")

    args = parser.parse_args()
    run_replication(args)
