import requests
import allure

key = "R13T4BY-PC243PX-MBWKD3V-ZAX56RZ"

@allure.title("Поиск фильмов по 2025 году")
@allure.description("Ввод год")
@allure.severity("critical")
def test_movies_2025():
    with allure.step("отправить запрос на фильмы 2025г"):
        HEADERS = {
            "accept": "application/json",
            "X-API-KEY": key
        }
        response = requests.get("https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&type=movie&year=2025",
                          headers=HEADERS)
    with allure.step("проверить код ответа"):
        assert response.status_code == 200

@allure.title("Поиск кинопремьер по декабрю 2025 года")
@allure.description("Ввод год и месяц")
@allure.severity("critical")
def test_movies_premieres_2025():
    with allure.step("отправить запрос на кинопремьеры декабря 2025г"):
          HEADERS = {
            "accept": "application/json",
            "X-API-KEY": key
          }
          response = requests.get("https://api.kinopoisk.dev/v2.2/films/premieres?year=2025&month=DECEMBER",
                          headers=HEADERS)
    with allure.step("проверить код ответа"):
          assert response.status_code == 200

@allure.title("Поиск актера по имени и фамилии")
@allure.description("Ввод ИФ, страница")
@allure.severity("critical")
def test_movies_actor():
    with allure.step("отправить запрос на актера"):
          HEADERS = {
            "accept": "application/json",
            "X-API-KEY": key
          }
          response = requests.get("https://api.kinopoisk.dev/v1/persons?name=Roman%20Kurtsyn&page=2",
                          headers=HEADERS)
    with allure.step("проверить код ответа"):
          assert response.status_code == 200

@allure.title("Поиск данных об api ключе")
@allure.description("Ввод api key")
@allure.severity("critical")
def test_api_key():
    with allure.step("отправить запрос на апи ключ"):
          HEADERS = {
            "accept": "application/json",
            "X-API-KEY": key
          }
          response = requests.get("https://api.kinopoisk.dev/v1/api_keys/R13T4BY-PC243PX-MBWKD3V-ZAX56RZ",
                          headers=HEADERS)
    with allure.step("проверить код ответа"):
        assert response.status_code == 200

@allure.title("Поиск медиа новостей с сайта")
@allure.description("Ввод номера страницы")
@allure.severity("critical")
def test_media_posts():
    with allure.step("отправить запрос на медиа новости"):
          HEADERS = {
            "accept": "application/json",
            "X-API-KEY": key
          }
          response = requests.get("https://api.kinopoisk.dev/v1/media_posts?page=3",
                          headers=HEADERS)
    with allure.step("проверить код ответа"):
          assert response.status_code == 200