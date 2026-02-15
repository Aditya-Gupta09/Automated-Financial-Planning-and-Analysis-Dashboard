"""
nvidia_3stmt.py
================

Core Deterministic 3-Statement Financial Engine

This module will contain the financial logic required to construct:

- Income Statement (P&L)
- Balance Sheet
- Cash Flow Statement

The engine will operate on canonical financial tables and structured
assumptions to produce reconciled financial outputs.

Design Principles:
- Deterministic (no randomness)
- Testable (supports invariant checks)
- Modular (no UI dependencies)
- Finance-first logic
"""

from typing import Dict
import pandas as pd


class ThreeStatementModel:
    """
    Core financial modeling engine.

    This class will eventually encapsulate all logic related to:
    - Revenue drivers
    - Margin assumptions
    - Working capital mechanics
    - Capex and depreciation
    - Cash flow reconciliation
    """

    def __init__(self, historical_data: pd.DataFrame, assumptions: Dict):
        """
        Parameters
        ----------
        historical_data : pd.DataFrame
            Canonical historical financial data.
        assumptions : Dict
            Financial assumptions from config/assumptions.json
        """
        self.historical_data = historical_data
        self.assumptions = assumptions

    def build_income_statement(self) -> pd.DataFrame:
        """
        Constructs projected Income Statement.

        Returns
        -------
        pd.DataFrame
        """
        raise NotImplementedError("Income statement logic not implemented yet.")

    def build_balance_sheet(self) -> pd.DataFrame:
        """
        Constructs projected Balance Sheet.

        Returns
        -------
        pd.DataFrame
        """
        raise NotImplementedError("Balance sheet logic not implemented yet.")

    def build_cash_flow_statement(self) -> pd.DataFrame:
        """
        Constructs projected Cash Flow Statement.

        Returns
        -------
        pd.DataFrame
        """
        raise NotImplementedError("Cash flow logic not implemented yet.")

    def run(self) -> Dict[str, pd.DataFrame]:
        """
        Executes the full 3-statement model.

        Returns
        -------
        dict
            {
                "pnl": DataFrame,
                "bs": DataFrame,
                "cf": DataFrame
            }
        """
        pnl = self.build_income_statement()
        bs = self.build_balance_sheet()
        cf = self.build_cash_flow_statement()

        return {
            "pnl": pnl,
            "bs": bs,
            "cf": cf
        }
