"""
Fundamentos e como usar a biblioteca Pandas
"""
import pandas as pd
class PandasLib:
    def criar_series_padrao(self):
        notas = pd.Series([7.6, 5.0, 8.5, 9.5, 6.45])
        print(f"Series simples:  {notas}")
        return notas
if __name__ == "__main__":
    inst = PandasLib()
    series_notas = inst.criar_series_padrao()
