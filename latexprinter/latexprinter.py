def lprint(df):
    """Convenient way to print a pandas.DataFrame
    in LaTeX booktabs format using siunitx."""
    print(
        df.to_latex(
            column_format='S '*len(df.columns),
            index=False,
        )
    )
