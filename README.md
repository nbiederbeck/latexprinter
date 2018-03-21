# latexprinter
A convenient and simple way to print `pandas.DataFrame` to LaTeX-Code using
`booktabs` and `siunitx`.

## Install
```bash
git clone https://github.com/nonator/latexprinter.git
cd latexprinter
pip install -e .
```

## Usage
```python
import pandas as pd
from latexprinter.latexprinter import lprint

df = pd.DataFrame()
lprint(df)
```
