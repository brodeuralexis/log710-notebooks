from __future__ import annotations

from itertools import chain,cycle

import pandas as pd
from IPython.display import display_html

def dataframes(dataframes: dict[str, pd.DataFrame]):
    html_str=''
    for (title, df) in dataframes.items():
        html_str+='<th style="text-align:center"><td style="vertical-align:top">'
        html_str+=f'<h2 style="text-align: center;">{title}</h2>'
        html_str+=df.to_html().replace('table','table style="display:inline"')
        html_str+='</td></th>'
    display_html(html_str,raw=True)
