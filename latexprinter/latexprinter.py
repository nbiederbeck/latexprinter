"""Provide function lprint to print pd.DataFrames."""


def lprint(dataframe):
    """Print a pandas.DataFrame.

    The LaTeX code uses booktabs and siunitx.
    """
    print(
        dataframe.to_latex(
            column_format='S '*len(dataframe.columns),
            index=False,
        )
    )
