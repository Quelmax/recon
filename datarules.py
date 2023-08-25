import pandas as pd


def getCrossSell(df):
    df_crossell = df[df['crossell'].notnull()]
    # print(df_crossell['nome'])
    return df_crossell



def getUpSell(df):
    df_upsell = df[df['upsell'].notnull()]
    # print(df_upsell['nome'])
    return df_upsell


