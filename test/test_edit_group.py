from model.group import Group


def test_edit_group_name(app):
    if app.group.count == 0:
        app.group.create(Group(name="new", footer="new", header="new"))
    app.group.edit_first_group(Group(name="name changed"))


def test_edit_group_header(app):
    if app.group.count == 0:
        app.group.create(Group(name="new", footer="new", header="new"))
    app.group.edit_first_group(Group(header="header changed"))
