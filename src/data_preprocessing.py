# data_preprocessing.py

import pandas as pd
import numpy as np
from scipy import stats

def normalize_by_creatinine(df: pd.DataFrame, metabolite_cols: list, creatinine_col: str = 'Creatinine') -> pd.DataFrame:
    """
    Normalizes metabolite concentrations by the creatinine value for each sample.

    Args:
        df (pd.DataFrame): DataFrame with metabolite and creatinine data.
        metabolite_cols (list): List of column names for metabolites.
        creatinine_col (str): The name of the creatinine column.

    Returns:
        pd.DataFrame: A new DataFrame with creatinine-normalized metabolite values.
    """
    df_normalized = df.copy()
    for col in metabolite_cols:
        # Divide metabolite concentration by creatinine concentration
        df_normalized[col] = df_normalized[col] / df_normalized[creatinine_col]
    return df_normalized.drop(columns=[creatinine_col])


def log_transform(df: pd.DataFrame, metabolite_cols: list) -> pd.DataFrame:
    """
    Applies a natural log transformation to metabolite data to handle skewed distributions.
    A small constant is added to avoid log(0).

    Args:
        df (pd.DataFrame): DataFrame with metabolite data.
        metabolite_cols (list): List of column names for metabolites.

    Returns:
        pd.DataFrame: DataFrame with log-transformed values.
    """
    df_log = df.copy()
    for col in metabolite_cols:
        # Add a small constant (e.g., 1) to avoid issues with zero values
        df_log[col] = np.log1p(df_log[col])
    return df_log


def calculate_z_scores(df: pd.DataFrame, control_group_label: str = 'Control') -> pd.DataFrame:
    """
    Calculates robust z-scores for each metabolite relative to the control group.
    Z-score = (value - control_median) / control_mad

    Args:
        df (pd.DataFrame): DataFrame with preprocessed data, including a 'Group' column.
        control_group_label (str): Label for the control group in the 'Group' column.

    Returns:
        pd.DataFrame: DataFrame of z-scores for each sample and metabolite.
    """
    controls = df[df['Group'] == control_group_label]
    metabolite_cols = df.select_dtypes(include=np.number).columns

    control_median = controls[metabolite_cols].median()
    # MAD: Median Absolute Deviation, a robust measure of variability
    control_mad = stats.median_abs_deviation(controls[metabolite_cols], axis=0)
    
    # Avoid division by zero if a metabolite has zero variance in controls
    control_mad[control_mad == 0] = 1e-9

    z_scores = df.copy()
    for col in metabolite_cols:
        z_scores[col] = (df[col] - control_median[col]) / control_mad[col]
        
    return z_scores