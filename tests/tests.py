import pytest

from pmgr.project import Project, TaskException

@pytest.fixture(scope="function")
def testproj():
    tproj = Project('mytestproj')
    yield tproj
    tproj.delete()

def test_add(testproj):
    testproj.add_task('dosomething')
    assert 'dosomething' in testproj.get_tasks()

def test_add_fail(testproj):
    testproj.add_task("somethingthatalreadyexists")
    with pytest.raises(TaskException):
        assert testproj.add_task("somethingthatalreadyexists")

def test_get_tasks(testproj):
    testproj.add_task('hello')
    testproj.add_task('there')
    assert 'hello' and 'there' in testproj.get_tasks()

def test_remove_task(testproj):
    testproj.add_task('REMOVEME')
    testproj.remove_task('REMOVEME')
    assert 'REMOVEME' not in testproj.get_tasks()

def test_remove_task_fail(testproj):
    with pytest.raises(TaskException):
        assert testproj.remove_task('somethingthatdoesnotexist')
    
def test_delete(testproj):
    testproj.add_task('DELETEME')
    testproj.delete('DELETEME')
    assert 'DELETEME' not in testproj.get_tasks()