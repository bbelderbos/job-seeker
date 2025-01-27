
import pandas as pd
from tests.conftest import js_instance
from job_seeker.downloader import JobSeeker


def test_params_dic(js_instance):
    assert isinstance(js_instance.params, dict)

def test_total_count(js_instance):
    assert js_instance.total_count == 320

def test_get_total_count(js_instance):
    total_count = js_instance._get_jobs_count() 
    assert total_count == 320

def test_get_pages(js_instance):
    total_count = js_instance._get_jobs_count() 
    pages = js_instance._total_pages(total_count)
    assert pages == 16

def test_df_instance(js_instance):
    df = js_instance.jobs_df
    assert isinstance(df, pd.DataFrame)
    assert df.shape == (320, 14)
    assert df["page"].max() == 16

def test_df_io_output(js_instance):
    io_output = js_instance.df_io
    assert isinstance(io_output, str)
