import pytest
from unittest.mock import patch
from project import News

@pytest.fixture
def mock_newsapi_client():
    with patch('project.NewsApiClient') as mock:
        yield mock

def test_get_news_list_with_results(mock_newsapi_client):
    mock_newsapi_client.return_value.get_everything.return_value = {
        "articles": [
            {"title": "Test News", "content": "Content of test news[+100 chars]", "url": "http://example.com"}
        ]
    }

    news = News("fake_key")
    results = news.get_news_list("test")

    assert len(results) == 1
    assert results[0]['title'] == "Test News"
    assert "100 chars" not in results[0]['content']

def test_get_news_list_no_results(mock_newsapi_client):
    mock_newsapi_client.return_value.get_everything.return_value = {"articles": []}

    news = News("fake_key")
    results = news.get_news_list("nothing")

    assert len(results) == 0

def test_get_news_list_removed_news(mock_newsapi_client):
    mock_newsapi_client.return_value.get_everything.return_value = {
        "articles": [{"title": "[Removed]", "content": "Content", "url": "http://example.com"}]
    }

    news = News("fake_key")
    results = news.get_news_list("removed")

    assert len(results) == 0
