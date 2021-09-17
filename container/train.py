# Importing the necessary Python libraries
import os
import cloudpickle
import pandas as pd
from category_encoders.one_hot import OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer

import warnings
warnings.filterwarnings('ignore')



## DIRECTORY INSTANTIATION
## ---------------------------------------------------------------------------------------------------------------------
# Defining how SageMaker
prefix = '/opt/ml/'
input_path = os.path.join(prefix, 'input/data')
output_path = os.path.join(prefix, 'output')
model_path = os.path.join(prefix, 'model')



## HELPER FUNCTIONS
## ---------------------------------------------------------------------------------------------------------------------



## MODEL TRAIN SCRIPT
## ---------------------------------------------------------------------------------------------------------------------
# https://github.com/aws/amazon-sagemaker-examples/blob/master/advanced_functionality/scikit_bring_your_own/container/decision_trees/train