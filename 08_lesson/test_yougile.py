from pydash import result

from YouGileProject import YouGileProjectApi
from data import (LOGIN, PASSWORD, COMPANY_ID, NEW_TITLE, TEST_USER, TITLE_GET_TEST, TITLE_EDIT_TEST, EDITED_TITLE, DELETED_STATUS, NEW_TITLE_NEGATIVE, TEST_USER_NEGATIVE)

api = YouGileProjectApi('https://ru.yougile.com/api-v2/', LOGIN, PASSWORD, COMPANY_ID)

def test_create_project_positive():
    projects_before = api.get_project_list()
    len_before = len(projects_before)

    result = api.create_project(NEW_TITLE, TEST_USER)
    new_id = result.json()['id']

    projects_after = api.get_project_list()
    len_after = len(projects_after)

    assert result.status_code == 201
    assert len_after - len_before == 1
    assert projects_after[-1]['title'] ==NEW_TITLE

    assert projects_after[-1]['id'] == new_id

    api.edit_project(new_id, True, NEW_TITLE, TEST_USER)

    def test_create_project_negative():
        projects_before == api.get_project_list()
        len_before = len(projects_before)

        result = api.create_project(NEW_TITLE_NEGATIVE, TEST_USER)

        projects_after = api.get_project_list()
        len_after = len(projects_after)

        assert result.status_code == 400
        assert len_after - len_before == 0

    def test_get_project_with_id_positive():
        result = api.create_project(TITLE_GET_TEST, TEST_USER)
        project_id = result.json()['id']

        new_project = api.get_project_with_id(project_id)

        assert new_project.status_code == 200
        assert new_project.json()['users'] == TEST_USER
        assert new_project.json()['title'] == TITLE_GET_TEST

    def test_get_project_with_negative():
        new_project = api.get_project_with_id()

        assert new_project.status_code == 404
        def test_edit_project_positive():
            result = api.create_project(TITLE_GET_TEST, TEST_USER)
            projects_id = result.json()['id']

            edited = api.edit_project(project_id, DELETED_STATUS, EDITED_TITLE,TEST_USER)

            assert edited.status_code == 200
            projects_title = api.get_project_with_id().json()['title']
            assert projects_title == EDITED_TITLE

            api.edit_project(projects_id, True, EDITED_TITLE, TEST_USER)

        def test_edit_project_negative():
            result = api.create_project(TITLE_GET_TEST, TEST_USER)
            project_id = result.json()['id']

            edited = api.edit_project(project_id, DELETED_STATUS, EDITED_TITLE, TEST_USER_NEGATIVE)

            assert edited.status_code == 400

            api.edit_project(project_id, True, EDITED_TITLE, TEST_USER)

