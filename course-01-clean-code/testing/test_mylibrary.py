# File: test_mylibrary.py
# Pytest filename starts with "test_...."
import pytest
import pandas as pd
import logging

##################################
"""
Function to test
"""
def import_data(pth):
    df = pd.read_csv(pth)
    return df
##################################


# Test function 
# It uses the built-in request fixture
def test_import_data_3(request):
  try:
      df3 = import_data("./data/iris.csv")
  except FileNotFoundError as err:
      logging.error("File not found")
      raise err
  '''
  Some assertion statements per your requirement.
  '''
  assert(df3.loc[0][0] == 5.1)

  request.config.cache.set("example/bob", "K")
  # request.config.cache.set("cache_df", df3)
  return df3

# Test function
# def test_function_three(request):
#   df = request.config.cache.get("cache_df", None)
#   '''
#   Some assertion statements per your requirement.
#   '''
#   assert(df.loc[0][0] == 5.1)