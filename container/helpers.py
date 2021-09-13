# Creating a function to appropriately engineer the 'Age' column
def create_age_bins(df):
    '''Engineers age bin variables for the pipeline'''

    # Instantiating the "Age" imputer object
    age_imputer = SimpleImputer(strategy = 'median')

    # Fitting / Transforming the "Age" column with the imputer object
    imputed_age = age_imputer.fit_transform(df['Age'].values.reshape(-1,1))

    # Recreating the "Age" imputed feature as a Pandas DataFrame
    df_imputed_age = pd.DataFrame(data = imputed_age, columns = ['age_imputed'])

    # Establishing our bins values and names
    bin_labels = ['child', 'teen', 'young_adult', 'adult', 'elder']
    bin_values = [-1, 12, 19, 30, 60, 100]

    # Applying "Age" binning with Pandas cut
    age_bins = pd.cut(df_imputed_age['age_imputed'], bins = bin_values, labels = bin_labels)
    df_age_bins = pd.DataFrame(age_bins)

    # Instantiating the "Age" One Hot Encoder (OHE) object
    age_ohe_encoder = one_hot.OneHotEncoder(use_cat_names = True, handle_unknown = 'other')

    # Fitting the age bins DataFrame to the OHE object
    age_dummies = age_ohe_encoder.fit_transform(df_age_bins)

    return age_dummies

# Creating a function to appropriately engineer the 'Embarked' column
def create_embarked_columns(df):
    '''Engineers the embarked variables for the pipeline'''

    # Instantiating the One Hot Encoder object
    embarked_ohe_encoder = one_hot.OneHotEncoder(use_cat_names = True, handle_missing = 'S')

    # Performing one hot encoding on the "Embarked" column
    embarked_dummies = embarked_ohe_encoder.fit_transform(df['Embarked'])

    return embarked_dummies

# Creating a function to appropriate engineer the 'Sex' (gender) column
def create_gender_columns(df):
    '''Engineers the sex (gender) variables for the pipeline'''

    # Changing Sex (gender) to numerical values
    df['Sex'].mask(df['Sex'] == 'male', 0, inplace = True)
    df['Sex'].mask(df['Sex'] == 'female', 1, inplace = True)
    df['Sex'] = df['Sex'].astype(int)

    return df[['Sex']]