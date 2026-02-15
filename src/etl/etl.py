"""
etl.py
======

ETL (Extract, Transform, Load) Module

Responsible for:
- Loading raw financial exports
- Validating schema
- Cleaning data
- Producing canonical financial tables

This module must not contain financial modeling logic.
"""

import pandas as pd


def load_raw_csv(path: str) -> pd.DataFrame:
    """
    Loads raw CSV data.

    Parameters
    ----------
    path : str

    Returns
    -------
    pd.DataFrame
    """
    try:
        df = pd.read_csv(path)
        return df
    except Exception as e:
        raise RuntimeError(f"Failed to load CSV: {e}")


def validate_schema(df: pd.DataFrame) -> None:
    """
    Validates required columns exist.

    Raises error if schema invalid.
    """
    raise NotImplementedError("Schema validation not implemented.")


def transform_to_canonical(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforms raw data into canonical financial format.

    Returns
    -------
    pd.DataFrame
    """
    raise NotImplementedError("Transformation logic not implemented.")
