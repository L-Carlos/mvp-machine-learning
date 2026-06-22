# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "pandas>=3.0.3",
#     "pyarrow>=24.0.0",
# ]
# ///

# Script para consolidar os dados em ./raw_data/dados_prf.zip
# em um unico arquivo .parquet para ser carregado no github

import io
import zipfile

import pandas as pd


def consolidar_arquivos(zip_path: str, out_path: str):
    dfs = []

    print(f"Lendo arquivos em {zip_path} ...")

    with zipfile.ZipFile(zip_path, mode="r") as main_zip:
        for zip_info in main_zip.infolist():
            if not zip_info.filename.lower().endswith(".zip"):
                continue

            sub_zip = main_zip.read(zip_info)

            with zipfile.ZipFile(io.BytesIO(sub_zip), mode="r") as z:
                for file_info in z.infolist():
                    if file_info.is_dir():
                        continue
                    if not file_info.filename.lower().endswith(".csv"):
                        continue

                    with z.open(file_info) as f:
                        temp_df = pd.read_csv(
                            f,
                            encoding="cp1252",
                            sep=";",
                            low_memory=False,
                            # alguns campos causam erro no parquet se deixados como objects
                            # depois serao tratados corretamente na etapa de modelagem
                            dtype={"km": str, "latitude": str, "longitude": str},
                            na_values=["(null)", "null", "NULL", "N/D", "N/A#"],
                        )
                        dfs.append(temp_df)

    if not dfs:
        print("Nenhum CSV encontrado. Verifique a estrutuda do .zip")
        return

    df = pd.concat(dfs, ignore_index=True)

    print(f"DF final: {df.shape[0]} linhas, {df.shape[1]} colunas.")

    print(df.head())

    print(df.info())

    print("Salvando arquivo final ...")

    df.to_parquet(out_path, compression="snappy", index=False)

    print(f"Processamento finalizado, arquivo salvo em {out_path}")


if __name__ == "__main__":
    ZIP_PATH = "./raw_data/dados_prf.zip"
    DESTINATION_PATH = "./data/dados_prf.parquet"

    consolidar_arquivos(ZIP_PATH, DESTINATION_PATH)
