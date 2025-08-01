# database_integration.py

import pandas as pd

def map_metabolites_to_kegg(metabolite_names: list) -> dict:
    """
    Maps common metabolite names to KEGG compound IDs.
    
    NOTE: This is a simplified example. A real implementation would use a comprehensive
    local mapping file or an API from a service like CTS (Chemical Translation Service).

    Args:
        metabolite_names (list): A list of metabolite names from the dataset.

    Returns:
        dict: A dictionary mapping common names to KEGG IDs.
    """
    # Example mapping dictionary. In a real-world scenario, this would be much larger.
    kegg_map = {
        'L-Alanine': 'C00041',
        'L-Leucine': 'C00123',
        'L-Phenylalanine': 'C00079',
        'L-Tyrosine': 'C00082',
        'Orotic acid': 'C00270',
        'Citric acid': 'C00158',
        'Succinic acid': 'C00042'
    }
    
    return {name: kegg_map.get(name, 'N/A') for name in metabolite_names}