import os
import logging
import churn_library as cl
import pytest

logging.basicConfig(
    filename='./logs/churn_library.log',
    level=logging.INFO,
    filemode='w',
    format='%(name)s - %(levelname)s - %(message)s')


@pytest.fixture(scope="module")
def import_data():
    '''
    Fixture - The test function test_import() will
    use the return of import_data() as an argument
    '''
    return cl.import_data


def test_import(import_data):
    '''
    test data import - this example is completed for you to assist with the other test functions
    '''
    try:
        df = import_data("./data/bank_data.csv")
        logging.info("Testing import_data: SUCCESS")
    except FileNotFoundError as err:
        logging.error("Testing import_eda: The file wasn't found")
        raise err

    try:
        assert df.shape[0] > 0
        assert df.shape[1] > 0
    except AssertionError as err:
        logging.error(
            "Testing import_data: The file doesn't appear to have rows and columns")
        raise err


@pytest.fixture(scope="module")
def perform_eda():
    '''
    Fixture - The test function test_eda() will
    use the return of eda() as an argument
    '''
    return cl.perform_eda


def test_eda(perform_eda):
    '''
    test perform eda function
    '''
    df = cl.import_data('./data/bank_data.csv')
    perform_eda(df)
    assert './images/churn_histogram.png'
    assert './images/heatmap.png'
    assert './images/total_transaction_histogram.png'
    assert './images/customer_age_histogram.png'
    assert './images/marital_status_counts.png'


@pytest.fixture(scope="module")
def encoder_helper():
    '''
    Fixture - The test function test_eda() will
    use the return of eda() as an argument
    '''
    return cl.encoder_helper


def test_encoder_helper(encoder_helper):
    '''
    test encoder helper
    '''
    df = cl.import_data('./data/bank_data.csv')
    cl.perform_eda(df)

    cat_columns = [
        'Gender',
        'Education_Level',
        'Marital_Status',
        'Income_Category',
        'Card_Category'
    ]

    quant_columns = [
        'Customer_Age',
        'Dependent_count',
        'Months_on_book',
        'Total_Relationship_Count',
        'Months_Inactive_12_mon',
        'Contacts_Count_12_mon',
        'Credit_Limit',
        'Total_Revolving_Bal',
        'Avg_Open_To_Buy',
        'Total_Amt_Chng_Q4_Q1',
        'Total_Trans_Amt',
        'Total_Trans_Ct',
        'Total_Ct_Chng_Q4_Q1',
        'Avg_Utilization_Ratio'
    ]

    df = encoder_helper(df, cat_columns, None)
    assert df.shape[0] == 10127


@pytest.fixture(scope="module")
def perform_feature_engineering():
    '''
    Fixture - The test function test_perform_feature_engineering() will
    use the return of perform_feature_engineering() as an argument
    '''
    return cl.perform_feature_engineering


def test_perform_feature_engineering(perform_feature_engineering):
    '''
    test perform_feature_engineering
    '''
    df = cl.import_data('./data/bank_data.csv')
    cl.perform_eda(df)

    cat_columns = [
        'Gender',
        'Education_Level',
        'Marital_Status',
        'Income_Category',
        'Card_Category'
    ]

    quant_columns = [
        'Customer_Age',
        'Dependent_count',
        'Months_on_book',
        'Total_Relationship_Count',
        'Months_Inactive_12_mon',
        'Contacts_Count_12_mon',
        'Credit_Limit',
        'Total_Revolving_Bal',
        'Avg_Open_To_Buy',
        'Total_Amt_Chng_Q4_Q1',
        'Total_Trans_Amt',
        'Total_Trans_Ct',
        'Total_Ct_Chng_Q4_Q1',
        'Avg_Utilization_Ratio'
    ]

    df = cl.encoder_helper(df, cat_columns, None)

    X_train, X_test, y_train, y_test = perform_feature_engineering(df, None)
    assert X_train.shape[0] == 7088


@pytest.fixture(scope="module")
def train_models():
    '''
    Fixture - The test function test_perform_feature_engineering() will
    use the return of perform_feature_engineering() as an argument
    '''
    return cl.train_models


def test_train_models(train_models):
    '''
    test train_models
    '''


if __name__ == "__main__":
    pass
