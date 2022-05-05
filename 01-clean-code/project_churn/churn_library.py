# library doc string
'''
Churn library.
'''

# import libraries
import os
import pandas as pd
import logging
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

from sklearn.metrics import plot_roc_curve, classification_report

os.environ['QT_QPA_PLATFORM']='offscreen'

logging.basicConfig(
    filename='./logs/churn_library.log',
    level = logging.INFO,
    filemode='w',
    format='%(name)s : %(levelname)s : %(message)s')


def import_data(pth):
    '''
    returns dataframe for the csv found at pth

    input:
            pth: a path to the csv
    output:
            df: pandas dataframe
    '''	
    try:
        df = pd.read_csv(pth)
        logging.info("%s : %s", "import_data", "SUCCESS")
        return df
    except FileNotFoundError as err:
        logging.error("import_data: The file wasn't found")
        return None


def perform_eda(df):
    '''
    perform eda on df and save figures to images folder
    input:
            df: pandas dataframe

    output:
            None
    '''
    # Make sure Attrition_Flag is either 0 or 1
    df['Churn'] = df['Attrition_Flag'].apply(lambda val: 0 if val == "Existing Customer" else 1)
    
    # Plot a Churn histogram.
    plt.figure(figsize=(20,10)) 
    df['Churn'].hist()
    plt.savefig("./images/churn_histogram.png")
    logging.info("%s : %s", "perform_eda: churn histogram", "SUCCESS")

    # Plot a Customer_Age histogram.
    plt.figure(figsize=(20,10)) 
    df['Customer_Age'].hist()
    plt.savefig("./images/customer_age_histogram.png")
    logging.info("%s : %s", "perform_eda: customer_age histogram", "SUCCESS")

    # Plot the marital status counts.
    plt.figure(figsize=(20,10)) 
    df.Marital_Status.value_counts('normalize').plot(kind='bar')
    plt.savefig("./images/marital_status_counts.png")
    logging.info("%s : %s", "perform_eda: plot marital status counts", "SUCCESS")

    # Plot the total transaction histogram.
    plt.figure(figsize=(20,10)) 
    sns.histplot(df['Total_Trans_Ct'], stat='density', kde=True)
    plt.savefig("./images/total_transaction_histogram.png")
    logging.info("%s : %s", "perform_eda: plot total transaction histogram", "SUCCESS")

    # Plot the heat map.
    plt.figure(figsize=(20,10))
    sns.heatmap(df.corr(), annot=False, cmap='Dark2_r', linewidths = 2)
    plt.savefig("./images/heatmap.png")
    logging.info("%s : %s", "perform_eda: plot heatmap", "SUCCESS")


def encoder_helper(df, category_lst, response):
    '''
    helper function to turn each categorical column into a new column with
    propotion of churn for each category - associated with cell 15 from the notebook

    input:
            df: pandas dataframe
            category_lst: list of columns that contain categorical features
            response: string of response name [optional argument that could be used for naming variables or index y column]

    output:
            df: pandas dataframe with new columns for
    '''
    # gender encoded column
    gender_lst = []
    gender_groups = df.groupby('Gender').mean()['Churn']

    for val in df['Gender']:
        gender_lst.append(gender_groups.loc[val])

    df['Gender_Churn'] = gender_lst    
    #education encoded column
    edu_lst = []
    edu_groups = df.groupby('Education_Level').mean()['Churn']

    for val in df['Education_Level']:
        edu_lst.append(edu_groups.loc[val])

    df['Education_Level_Churn'] = edu_lst

    #marital encoded column
    marital_lst = []
    marital_groups = df.groupby('Marital_Status').mean()['Churn']

    for val in df['Marital_Status']:
        marital_lst.append(marital_groups.loc[val])

    df['Marital_Status_Churn'] = marital_lst

    #income encoded column
    income_lst = []
    income_groups = df.groupby('Income_Category').mean()['Churn']

    for val in df['Income_Category']:
        income_lst.append(income_groups.loc[val])

    df['Income_Category_Churn'] = income_lst

    #card encoded column
    card_lst = []
    card_groups = df.groupby('Card_Category').mean()['Churn']
    
    for val in df['Card_Category']:
        card_lst.append(card_groups.loc[val])

    df['Card_Category_Churn'] = card_lst
    
    return df


def perform_feature_engineering(df, response):
    '''
    input:
              df: pandas dataframe
              response: string of response name [optional argument that could be used for naming variables or index y column]

    output:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    '''
    y = df['Churn']
    X = pd.DataFrame()
    keep_cols = ['Customer_Age', 'Dependent_count', 'Months_on_book',
                'Total_Relationship_Count', 'Months_Inactive_12_mon',
                'Contacts_Count_12_mon', 'Credit_Limit', 'Total_Revolving_Bal',
                'Avg_Open_To_Buy', 'Total_Amt_Chng_Q4_Q1', 'Total_Trans_Amt',
                'Total_Trans_Ct', 'Total_Ct_Chng_Q4_Q1', 'Avg_Utilization_Ratio',
                'Gender_Churn', 'Education_Level_Churn', 'Marital_Status_Churn', 
                'Income_Category_Churn', 'Card_Category_Churn']

    X[keep_cols] = df[keep_cols]

    # train test split 
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.3, random_state=42)
    return X_train, X_test, y_train, y_test

def classification_report_image(y_train,
                                y_test,
                                y_train_preds_lr,
                                y_train_preds_rf,
                                y_test_preds_lr,
                                y_test_preds_rf):
    '''
    produces classification report for training and testing results and stores report as image
    in images folder
    input:
            y_train: training response values
            y_test:  test response values
            y_train_preds_lr: training predictions from logistic regression
            y_train_preds_rf: training predictions from random forest
            y_test_preds_lr: test predictions from logistic regression
            y_test_preds_rf: test predictions from random forest

    output:
             None
    '''
    pass


def feature_importance_plot(model, X_data, output_pth):
    '''
    creates and stores the feature importances in pth
    input:
            model: model object containing feature_importances_
            X_data: pandas dataframe of X values
            output_pth: path to store the figure

    output:
             None
    '''
    pass

def train_models(X_train, X_test, y_train, y_test):
    '''
    train, store model results: images + scores, and store models
    input:
              X_train: X training data
              X_test: X testing data
              y_train: y training data
              y_test: y testing data
    output:
              None
    '''
    # grid search
    rfc = RandomForestClassifier(random_state=42)
    # Use a different solver if the default 'lbfgs' fails to converge
    # Reference: https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
    lrc = LogisticRegression(solver='lbfgs', max_iter=3000)

    param_grid = { 
        'n_estimators': [200, 500],
        'max_features': ['auto', 'sqrt'],
        'max_depth' : [4,5,100],
        'criterion' :['gini', 'entropy']
    }

    cv_rfc = GridSearchCV(estimator=rfc, param_grid=param_grid, cv=5)
    cv_rfc.fit(X_train, y_train)

    lrc.fit(X_train, y_train)

    y_train_preds_rf = cv_rfc.best_estimator_.predict(X_train)
    y_test_preds_rf = cv_rfc.best_estimator_.predict(X_test)

    y_train_preds_lr = lrc.predict(X_train)
    y_test_preds_lr = lrc.predict(X_test)

    # scores
    print('random forest results')
    print('test results')
    print(classification_report(y_test, y_test_preds_rf))
    print('train results')
    print(classification_report(y_train, y_train_preds_rf))

    print('logistic regression results')
    print('test results')
    print(classification_report(y_test, y_test_preds_lr))
    print('train results')
    print(classification_report(y_train, y_train_preds_lr))

if __name__ == "__main__":
    df = import_data('./data/bank_data.csv')
    perform_eda(df)
    encoder_helper(df, None, None)
    X_train, X_test, y_train, y_test = perform_feature_engineering(df, None)
    train_models(X_train, X_test, y_train, y_test)
