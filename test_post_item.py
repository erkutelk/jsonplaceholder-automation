import pytest
from api_json import ApiResponse
import logging
def test_post_new_post():
    data = {
        'title': 'Erkut',
        'body': 'Elik',
        'userId': 1
    }
    api = ApiResponse('posts')
    response = api.post(data)
    try:
        assert response.status_code == 201, "🟥 POST isteği başarısız oldu"
        json_data = response.json()
        assert json_data['title'] == 'Erkut', "🟥 title uyuşmuyor"
        assert json_data['body'] == 'Elik', "🟥 body uyuşmuyor"
        assert json_data['userId'] == 1, "🟥 userId uyuşmuyor"

        logging.info('🟩 https://jsonplaceholder.typicode.com/posts Testi Yapıldı')
    except AssertionError as e:
        logging.error(f'🟥 https://jsonplaceholder.typicode.com/posts hata meydana geldi\n{e}')
        raise


def test_put_update():
    data={
        'id':1,
        'title':'Güncellenmiş',
        'body':'Güncellenmiş',
        'userId':1
    }

    api=ApiResponse('posts/1')
    response=api.put(data)

    try:
        assert response.status_code==200
        json_data=response.json()

        assert json_data['title']=='Güncellenmiş','🟥 Title güncellenmiyor'
        assert json_data['body']=='Güncellenmiş','🟥 Body güncellenmiyor'
        logging.info('🟩 https://jsonplaceholder.typicode.com/posts/1 Güncelleme yapılıyor')

    except AssertionError as e:
        logging.error(f'🟥 https://jsonplaceholder.typicode.com/posts/1 Hata meydana geldi\n{e}')
        raise


def test_patch_post_title():
    update_data = {"title": "Erkut"}
    api = ApiResponse('posts/1')
    response = api.patch(update_data)
    try:
        assert response.status_code == 200, "🟥 PATCH isteği başarısız"
        json_data = response.json()
        assert json_data['title'] == "Erkut", "🟥 Title güncellenemedi"
        logging.info('🟩 https://jsonplaceholder.typicode.com/posts/1 sadece bir alanı güncelleme yapılıyor')
    except AssertionError as e:
        logging.error(f'🟥 https://jsonplaceholder.typicode.com/posts/1 hata meydana geldi \n {e}')
        raise


def test_delete_post():
    api = ApiResponse('posts/1')
    response = api.delete()
    try:
        assert response.status_code == 200 or response.status_code == 204, "🟥 Delete işlemi başarısız başarısız"
        logging.info('🟩 https://jsonplaceholder.typicode.com/posts/1 silme işlemi yapılıyor')
    except AssertionError as e:
        logging.info(f'🟥 https://jsonplaceholder.typicode.com/posts/1 Hata meydana geldi\n{e}')
        raise
