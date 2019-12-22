
import pandas as pd
import shap


def explains(df_e, mod, xtt, tfs, row_number):

    row = df_e.iloc[[row_number]]

    explainer = shap.LinearExplainer(mod, xtt)
    row_process = tfs.transform(row)
    shap_values = explainer.shap_values(row_process)

    feature_names = row.columns
    feature_values = row.values[0]
    shaps = pd.Series(shap_values[0], zip(feature_names, feature_values))

    pros = shaps.sort_values(ascending=False)[:2].index
    cons = shaps.sort_values(ascending=True)[:2].index

    return pros, cons
