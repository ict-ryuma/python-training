import pandas as pd
from pathlib import Path

SAVE_DIR = Path(__file__).parent / "survey_responses"
SAVE_DIR.mkdir(exist_ok=True)

def save_response(response: dict):
    import datetime
    today = datetime.date.today().strftime("%Y-%m")

    csv_path = SAVE_DIR / f"{today}.csv"

    # 既存ファイルがあり、かつ中身が空でない時だけ読み込む
    if csv_path.exists() and csv_path.stat().st_size > 0:
        df_existing = pd.read_csv(csv_path)
    else:
        df_existing = pd.DataFrame()

    df_new = pd.DataFrame([response])
    df_all = pd.concat([df_existing, df_new], ignore_index=True)
    df_all.to_csv(csv_path, index=False)
