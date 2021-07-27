from model.group import Group
from timeit import timeit


def test_group_list(app, db):
    # print(timeit(lambda: app.group.get_group_list(), number=1)) # измерение время выполнения
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    # print(timeit(lambda: map(clean, db.get_group_list()), number=1000))  # измерение время выполнения
    db_list = map(clean, db.get_group_list())
    # assert False
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)