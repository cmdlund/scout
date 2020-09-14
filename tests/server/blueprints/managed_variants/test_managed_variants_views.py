# -*- coding: utf-8 -*-
from flask import url_for
from scout.server.extensions import store


def test_managed_variants(app, user_obj, institute_obj):
    # GIVEN an initialized app
    # GIVEN a valid user and institute

    with app.test_client() as client:
        # GIVEN that the user could be logged in
        resp = client.get(url_for("auto_login"))
        assert resp.status_code == 200

        # WHEN accessing the cases page
        resp = client.get(url_for("managed_variants.managed_variants"))

        # THEN it should return a page
        assert resp.status_code == 200
