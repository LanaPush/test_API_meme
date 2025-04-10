import allure


class Endpoint:
    url = 'http://167.172.172.115:52355'
    json = None
    response = None
    headers = None
    token = None
    payload = None
    status_code = None
    text = None

    @allure.step('check the status code is 200')
    def check_status_code_is_200(self):
        assert self.response.status_code == 200

    @allure.step('check the status code is 400')
    def check_status_code_is_400(self):
        assert self.response.status_code == 400

    @allure.step('check the status code is 404')
    def check_status_code_is_404(self):
        assert self.response.status_code == 404

    @allure.step('check the status code is 401')
    def check_status_code_is_401(self):
        assert self.response.status_code == 401

    @allure.step('check the response text Bad Request')
    def check_response_text_bad_request(self):
        assert '400 Bad Request' in self.response.text, f'{self.response.text}'

    @allure.step('check the response text Not Found')
    def check_response_text_not_found(self):
        assert "404 Not Found" in self.response.text, f"{self.response.text}"

    @allure.step('check the response text Unauthorized')
    def check_response_text_unauthorized(self):
        assert "401 Unauthorized" in self.response.text, f'{self.response.text}'
