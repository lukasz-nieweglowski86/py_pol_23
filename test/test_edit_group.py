from model.group import Group
import random


def test_edit_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="new", footer="new", header="new"))
    old_groups = db.get_group_list()
    group = Group(name="modified")
    group_id = random.choice(old_groups).id
    app.group.edit_group_by_id(group_id, group)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    for index, i in enumerate(old_groups):
        if i.id == group_id:
            old_groups[index] = group
        else:
            index -= 1
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


# def test_edit_group_header(app):
#     if app.group.count == 0:
#         app.group.create(Group(name="new", footer="new", header="new"))
#     old_groups = app.group.get_group_list()
#     app.group.edit_first_group(Group(header="header changed"))
#     new_groups = app.group.get_group_list()
#     assert len(old_groups) == len(new_groups)
