# visualization.py

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_top_pathways(enrichment_results: pd.DataFrame, top_n: int = 10):
    """
    Creates a bar plot of the top N most significant pathways.

    Args:
        enrichment_results (pd.DataFrame): DataFrame from MetaboAnalyst with
                                           pathways, p-values, and impact scores.
        top_n (int): Number of top pathways to plot.
    """
    # Sort by p-value (smallest first)
    top_pathways = enrichment_results.sort_values(by='-log10(p)', ascending=False).head(top_n)

    plt.figure(figsize=(10, 8))
    sns.barplot(
        x='-log10(p)',
        y='Pathway',
        data=top_pathways,
        palette='viridis'
    )
    plt.title(f'Top {top_n} Enriched Metabolic Pathways', fontsize=16)
    plt.xlabel('Significance [-log10(p-value)]', fontsize=12)
    plt.ylabel('Metabolic Pathway', fontsize=12)
    plt.tight_layout()
    plt.show()


def plot_metabolite_heatmap(z_scores_df: pd.DataFrame, significant_metabolites: list, patient_id: str):
    """
    Generates a heatmap of z-scores for significant metabolites.

    Args:
        z_scores_df (pd.DataFrame): DataFrame of z-scores for all samples.
        significant_metabolites (list): A list of metabolites from the key pathway.
        patient_id (str): The ID of the patient sample to highlight.
    """
    # Filter for significant metabolites and set Sample_ID as index
    heatmap_data = z_scores_df[z_scores_df['Sample_ID'].str.contains(f'{patient_id}|Control')].copy()
    heatmap_data = heatmap_data[['Sample_ID'] + significant_metabolites].set_index('Sample_ID')
    
    # Add a color bar for the patient
    patient_color = 'red'
    control_color = 'skyblue'
    row_colors = [patient_color if patient_id in idx else control_color for idx in heatmap_data.index]

    plt.figure(figsize=(12, 6))
    sns.clustermap(
        heatmap_data.T,
        cmap='coolwarm',
        col_colors=row_colors,
        center=0,
        cbar_pos=(0.02, 0.8, 0.05, 0.18),
        dendrogram_ratio=(0.2, 0.05),
        linewidths=.5
    )
    plt.suptitle(f'Z-Scores of Significant Metabolites (Patient: {patient_id})', y=1.02, fontsize=16)
    plt.show()