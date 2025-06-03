# news_stock_correlation.py
"""
Modular functions for analyzing correlation between news sentiment and stock price movements.
"""
import pandas as pd
from textblob import TextBlob
from scipy.stats import pearsonr


def normalize_dates(df, date_col):
    """Convert date column to datetime and remove timezone info."""
    df = df.copy()
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce').dt.tz_localize(None)
    return df


def compute_sentiment(df, text_col="headline"):
    """Add sentiment polarity score for each headline using TextBlob."""
    df = df.copy()
    df["sentiment"] = df[text_col].fillna("").apply(lambda x: TextBlob(x).sentiment.polarity)
    return df


def aggregate_daily_sentiment(df, date_col="date"):
    """Aggregate sentiment scores by date (mean)."""
    return df.groupby(date_col)["sentiment"].mean().reset_index(name="avg_sentiment")


def compute_daily_returns(df, date_col="date", price_col="Close"):
    """Compute daily percentage returns from closing prices."""
    df = df.copy()
    df = df.sort_values(date_col)
    df["daily_return"] = df[price_col].pct_change()
    return df[[date_col, "daily_return"]]


def merge_sentiment_returns(sentiment_df, returns_df, date_col="date"):
    """Merge daily sentiment and returns on date."""
    return pd.merge(sentiment_df, returns_df, on=date_col, how="inner")


def compute_correlation(merged_df):
    """Compute Pearson correlation between avg_sentiment and daily_return."""
    merged_df = merged_df.dropna(subset=["avg_sentiment", "daily_return"])
    if len(merged_df) < 2:
        return None, None
    corr, pval = pearsonr(merged_df["avg_sentiment"], merged_df["daily_return"])
    return corr, pval
