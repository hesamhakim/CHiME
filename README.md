# CHiME (Child's Hereditary Metabolic Explorer)

**Version 1.0**

## 1. Overview

**CHiME** is a computational pipeline designed to identify potential inborn errors of metabolism in children by analyzing urinary metabolite data. The core objective is to decipher metabolic abnormalities with genetic roots by linking significant changes in metabolite concentrations to specific disruptions in biochemical pathways.

This project leverages curated, publicly available biochemical databases (like KEGG and HMDB), eliminating the need for a large, pre-existing training dataset. By using a pathway-centric enrichment analysis, CHiME provides a rapid, scalable, and clinically interpretable workflow to support diagnostic efforts for pediatric metabolic disorders.

## 2. Scientific Workflow

The CHiME pipeline follows a systematic, multi-step process to translate raw metabolomic data into actionable clinical insights.

```
[Raw Data] -> [Step 1: Preprocessing] -> [Step 2: Enrichment Analysis] -> [Step 3: Visualization] -> [Hypothesis]
     |                 |                             |                           |                    |
 .csv file       Normalization &           Mapping to public             Pathway plots &          Identified
 with patient    Z-Score Calculation       databases (KEGG)              Metabolite Heatmaps      dysregulated
 & control data                                                                                   pathways
```

## 3. Getting Started

Follow these steps to set up your environment and run the analysis.

### Prerequisites

- Python 3.9 or higher
    
- Git command-line tools
    

### Step 1: Clone the Repository

First, clone this repository to your local machine using Git.

```
git clone <repository-url>
cd CHiME
```

### Step 2: Set Up the Python Environment

It is highly recommended to use a virtual environment to manage dependencies and avoid conflicts with other projects.

```
# Create a virtual environment
python3 -m venv venv

# Activate the environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate
```

### Step 3: Install Dependencies

Install all the required Python libraries listed in the `requirements.txt` file.

```
pip install -r requirements.txt
```

### Step 4: Add Your Data

Place your own raw data CSV file into the `/data` directory. The file must adhere to the format specified below.

#### Input Data Structure

The pipeline requires input data to be in a **CSV (Comma-Separated Values)** format. Each row should represent a unique sample, and each column should represent a measured variable.

|Column Name|Data Type|Description|
|---|---|---|
|`Sample_ID`|String|A unique identifier for each sample (e.g., `Patient_01`, `Control_A`).|
|`Group`|String|The group to which the sample belongs. Must contain a `Control` group and one or more patient groups.|
|`Creatinine`|Numeric|The creatinine concentration, used for normalization of urinary metabolites.|
|_Metabolites_|Numeric|One or more columns containing the concentration values for each quantified metabolite.|

**Example (`data/urinary_metabolites.csv`):**

```
Sample_ID,Group,Creatinine,L-Alanine,L-Leucine,Orotic acid,Citric acid
Patient_01,Patient,85,150,45,950,25
Control_01,Control,110,120,55,15,450
Control_02,Control,95,115,50,12,510
```

### Step 5: Run the Analysis

The entire workflow is orchestrated within the `pipeline.ipynb` Jupyter Notebook.

1. **Launch Jupyter Notebook:**
    
    ```
    jupyter notebook
    ```
    
2. **Open the Pipeline:** From the Jupyter interface in your browser, navigate to the `notebooks/` directory and open `pipeline.ipynb`.
    
3. **Update the Filename (if needed):** In the first code cell of the notebook, change the filename from `'urinary_metabolites.csv'` to the name of your data file.
    
4. **Execute the Cells:** Run the notebook cells sequentially from top to bottom. The notebook will guide you through each step of the analysis.
    

## 4. Expected Output

The pipeline generates several outputs, which are saved in the `/results` directory:

- **`metaboanalyst_input.csv`**: A processed data file formatted for direct upload to web-based enrichment tools like [MetaboAnalyst](https://www.metaboanalyst.ca/ "null").
    
- **Pathway Enrichment Plots**: Visualizations saved in `/results/figures` that show the most statistically significant metabolic pathways.
    
- **Metabolite Heatmaps**: Graphical representations of the z-scores for key metabolites, highlighting differences between patient and control samples.
    

By the end of the notebook, you will have a clear, data-driven hypothesis about which metabolic pathways are disrupted, guiding further clinical and genetic investigation.

## 5. Contributing

Contributions are welcome! If you would like to contribute to the development of CHiME, please read our [CONTRIBUTING.md](https://www.google.com/search?q=./CONTRIBUTING.md "null") file for guidelines on how to submit pull requests, report issues, and suggest improvements.

## 6. License

This project is licensed under the MIT License. See the [LICENSE.md](https://www.google.com/search?q=./LICENSE.md "null") file for details.

## 7. Citation

If you use CHiME in your research, please cite it as follows:

> [Your Name/Lab Name]. (2025). _CHiME (Child's Hereditary Metabolic Explorer)_ (Version 1.0) [Software]. Available from [https://github.com/your-repo](https://github.com/your-repo "null").