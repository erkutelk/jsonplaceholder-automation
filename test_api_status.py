import pytest
from api_json import ApiResponse

class TestApiResponse:
    @pytest.mark.parametrize("url",[("posts"),("comments"),("albums"),("photos"),("todos"),("users")])
    def test_status_posts(self,url):
        api = ApiResponse(url)
        print('🟩 Status successful',url)
        assert api.get_status() == 200

    

