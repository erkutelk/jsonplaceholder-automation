import pytest
from api_json import ApiResponse
import logging

expected_post_1 = {
    'userId': 1,
    'id': 1,
    'title': 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit',
    'body': 'quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto'
}

def test_post_first_data_get():
    api = ApiResponse('posts/1')
    actual_data = api.get_json()
    try:
        assert actual_data['userId'] == expected_post_1['userId'], "🟥 userId uyuşmazlığı"
        assert actual_data['id'] == expected_post_1['id'], "🟥 id uyuşmazlığı"
        assert actual_data['title'] == expected_post_1['title'], "🟥 title uyuşmazlığı"
        assert actual_data['body'] == expected_post_1['body'], "🟥 body uyuşmazlığı"
        logging.info('🟩 https://jsonplaceholder.typicode.com/posts/1 Testi Yapıldı')
    except AssertionError as e:
        logging.error('🟥 https://jsonplaceholder.typicode.com/posts/1 Testi başarısız')
        raise
    
expected_post_commets={'postId': 1,
                        'id': 1, 
                        'name': 'id labore ex et quam laborum', 
                        'email': 'Eliseo@gardner.biz', 
                        'body': 'laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium'}

def test_post_first_comments_get():
    api = ApiResponse('posts/1/comments')
    actual_data = api.get_json()
    try:
        first_comment = actual_data[0]
        assert first_comment['postId'] == expected_post_commets['postId'], "🟥 postId uyuşmazlığı"
        assert first_comment['id'] == expected_post_commets['id'], "🟥 id uyuşmazlığı"
        assert first_comment['name'] == expected_post_commets['name'], "🟥 name uyuşmazlığı"
        assert first_comment['email'] == expected_post_commets['email'], "🟥 email uyuşmazlığı"
        assert first_comment['body'] == expected_post_commets['body'], "🟥 body uyuşmazlığı"

        logging.info('🟩 https://jsonplaceholder.typicode.com/posts/1/comments Testi Yapıldı')
    except AssertionError as e:
        logging.info('🟥 https://jsonplaceholder.typicode.com/posts/1/comments Hata meydana geldi')
        raise

post_id={'postId': 1, 
          'id': 1, 
          'name': 'id labore ex et quam laborum', 
          'email': 'Eliseo@gardner.biz', 
          'body': 'laudantium enim quasi est quidem magnam voluptate ipsam eos\ntempora quo necessitatibus\ndolor quam autem quasi\nreiciendis et nam sapiente accusantium'}

def test_post_first_comments_post_id():
    api = ApiResponse('comments?postId=1')
    actual_data = api.get_json()
    first_adet=actual_data[0]
    try:
        assert first_adet['postId']==post_id["postId"],"🟥 postId Hata meydana geldi"
        assert first_adet['id']==post_id["id"],"🟥 id Hata meydana geldi"
        assert first_adet['name']==post_id["name"],"🟥 name Hata meydana geldi"
        assert first_adet['email']==post_id["email"],"🟥 email Hata meydana geldi"
        assert first_adet['body']==post_id["body"],"🟥 body Hata meydana geldi"
        logging.info('🟩 https://jsonplaceholder.typicode.com/comments?postId=1 Testi Yapıldı')
    except AssertionError as e:
        logging.info('🟥 https://jsonplaceholder.typicode.com/comments?postId=1 Hata meydana geldi')
        raise
