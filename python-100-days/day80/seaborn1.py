import seaborn as sns

sns.set_theme()

tips_df = sns.load_dataset("tips")
# tips_df.info()

sns.histplot(data=tips_df, x="total_bill", kde=True)


# import ssl

# ssl._create_default_https_context = ssl._create_unverified_context
