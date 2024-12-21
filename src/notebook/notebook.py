import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
df=pd.read_csv('/home/ibrahimfadu/Diploma/src/data/comple_n1.csv')

college_names=df.COLLEGE.unique()
Branch_names=df.BRANCH.unique()
Categories_names=df.CATEGORIES.unique()

import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer


# Load data from CSV file
df = pd.read_csv('src/data/comple_n1.csv')

# Handle NaN values by filling with a default value (e.g., 0) or using SimpleImputer
imputer = SimpleImputer(strategy='mean')
df[['Cutoff_2019', 'Cutoff_2020', 'Cutoff_2021', 'Cutoff_2022', 'Cutoff_2023']] = imputer.fit_transform(
    df[['Cutoff_2019', 'Cutoff_2020', 'Cutoff_2021', 'Cutoff_2022', 'Cutoff_2023']]
)

# Prepare features and target
X = df[['COLLEGE', 'BRANCH', 'CATEGORIES', 'Cutoff_2019', 'Cutoff_2020', 'Cutoff_2021', 'Cutoff_2022', 'Cutoff_2023']]
y = df['Cutoff_2024']

# Define the preprocessing steps
preprocessor = ColumnTransformer(
    transformers=[
        ('cat', OneHotEncoder(), ['COLLEGE', 'BRANCH', 'CATEGORIES']),
    ],
    remainder='passthrough'  # Keep other columns (the cutoff columns)
)

# Create a pipeline that combines the preprocessing with the Ridge model
model = Pipeline(steps=[
    ('preprocessor', preprocessor),
    ('regressor', Ridge())
])


model=model.fit(X, y)


