# pathway_analysis.py

import pandas as pd

def prepare_for_metaboanalyst(z_scores_df: pd.DataFrame) -> pd.DataFrame:
    """
    Formats the z-score data into the required format for MetaboAnalyst.
    - Samples in columns.
    - Metabolites (features) in rows.
    - 'Sample' as the first column header.

    Args:
        z_scores_df (pd.DataFrame): DataFrame containing z-scores.

    Returns:
        pd.DataFrame: A formatted DataFrame ready for upload to MetaboAnalyst.
    """
    # Set Sample_ID as the index, then transpose the DataFrame
    metaboanalyst_df = z_scores_df.set_index('Sample_ID').select_dtypes(include=np.number).T
    
    # Reset index to make metabolite names a column
    metaboanalyst_df = metaboanalyst_df.reset_index()
    metaboanalyst_df = metaboanalyst_df.rename(columns={'index': 'Metabolite'})
    
    print("Data formatted for MetaboAnalyst. Please upload the resulting CSV.")
    print("In MetaboAnalyst, select 'Pathway Analysis' from a list of Z-scores.")
    
    return metaboanalyst_df