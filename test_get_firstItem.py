import pytest
from api_json import ApiResponse

expected_post_1 = {
    'userId': 1,
    'id': 1,
    'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
    'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
}

def test_post_first_data_get():
    api = ApiResponse('posts/1')
    actual_data = api.get_json()
    
    assert actual_data['userId'] == expected_post_1['userId'], "userId uyuşmazlığı"
    assert actual_data['id'] == expected_post_1['id'], "id uyuşmazlığı"
    assert actual_data['title'] == expected_post_1['title'], "title uyuşmazlığı"
    assert actual_data['body'] == expected_post_1['body'], "body uyuşmazlığı"


