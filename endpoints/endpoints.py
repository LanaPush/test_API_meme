class Endpoint:
    url = 'http://167.172.172.115:52355'
    json = None
    response = None
    headers = None
    token = None
    payload = None
    status_code = None
    text = None

    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    def check_status_code_is_400(self):
        assert self.response.status_code == 400

    def check_status_code_is_404(self):
        assert self.response.status_code == 404

    def check_status_code_is_401(self):
        assert self.response.status_code == 401

    def check_response_text_bad_request(self):
        assert '400 Bad Request' in self.response.text, f'{self.response.text}'

    def check_response_text_not_found(self):
        assert "404 Not Found" in self.response.text, f"{self.response.text}"

    def check_response_text_unauthorized(self):
        assert "401 Unauthorized" in self.response.text, f'{self.response.text}'



