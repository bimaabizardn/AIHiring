import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_label_dataset(file_path):
    df = pd.read_csv(file_path)
    # Example labeling (adjust rules as needed)
    def label_text(text):
        text = text.lower()
        if "tidak bisa" in text or "error" in text or "gangguan" in text:
            return "Problem"
        elif "tolong" in text or "mohon" in text or "bisakah" in text:
            return "Request"
        else:
            return "Information"
    df['label'] = df['question'].apply(label_text)
    return df

def split_dataset(df, test_size=0.2):
    train_df, test_df = train_test_split(df, test_size=test_size, random_state=42, stratify=df['label'])
    return train_df, test_df
