from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new", footer="new", header="new"))
    old_groups = db.get_group_list()
    group = Group(name="dupa")
    random_old_group = random.choice(old_groups)
    group_id = random_old_group.id
    app.group.edit_group_by_id(group_id, group)
    for elem in old_groups:
        if elem.id == group_id:
            elem.name = group.name
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_edit_group_header(app):
#     if app.group.count == 0:
#         app.group.create(Group(name="new", footer="new", header="new"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(header="header changed"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
