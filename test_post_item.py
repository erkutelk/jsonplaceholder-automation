import pytest
from api_json import ApiResponse

def test_post_new_post():
    data = {
        'title': 'Erkut',
        'body': 'Elik',
        'userId': 1
    }
    api = ApiResponse('/posts')
    response = api.post(data)

    assert response.status_code == 201, "🟥 POST isteği başarısız oldu"
    json_data = response.json()
    assert json_data['title'] == 'Erkut', "🟥 title uyuşmuyor"
    assert json_data['body'] == 'Elik', "🟥 body uyuşmuyor"
    assert json_data['userId'] == 1, "🟥 userId uyuşmuyor"
