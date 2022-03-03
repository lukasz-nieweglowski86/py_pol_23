from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="name changed", header="header changed", footer="footer changed"))
    app.session.logout()
