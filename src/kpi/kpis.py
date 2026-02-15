"""
kpis.py
=======

KPI Engine Module

Contains financial metric calculations derived from
model outputs.

This module must remain independent of the UI layer.
"""

import pandas as pd


def gross_margin(pnl: pd.DataFrame) -> float:
    """
    Calculates Gross Margin.

    Formula:
        (Revenue - COGS) / Revenue

    Parameters
    ----------
    pnl : pd.DataFrame

    Returns
    -------
    float
    """
    raise NotImplementedError("Gross margin calculation not implemented.")


def ebitda_margin(pnl: pd.DataFrame) -> float:
    """
    Calculates EBITDA Margin.

    Parameters
    ----------
    pnl : pd.DataFrame

    Returns
    -------
    float
    """
    raise NotImplementedError("EBITDA margin calculation not implemented.")


def free_cash_flow_margin(cf: pd.DataFrame, pnl: pd.DataFrame) -> float:
    """
    Calculates Free Cash Flow Margin.

    Parameters
    ----------
    cf : pd.DataFrame
    pnl : pd.DataFrame

    Returns
    -------
    float
    """
    raise NotImplementedError("FCF margin calculation not implemented.")
