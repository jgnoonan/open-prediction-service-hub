#!/usr/bin/env python3
#
# Copyright 2020 IBM
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.IBM Confidential
#


import typing

import pytest
import sqlalchemy.orm as orm

import app.crud as crud
import app.models as models
import app.schemas as schemas
import app.tests.utils.utils as utils


@pytest.fixture()
def model_with_config(
        db: orm.Session,
        classification_config: typing.Dict[typing.Text, typing.Any],
) -> models.Model:
    model = crud.model.create(db, obj_in=schemas.ModelCreate())
    crud.model_config.create_with_model(
        db, obj_in=schemas.ModelConfigCreate(configuration=classification_config), model_id=model.id
    )
    return model


@pytest.fixture()
def model_with_config_and_endpoint(
        db: orm.Session,
        classification_config: typing.Dict[typing.Text, typing.Any],
        model_with_config: models.Model
) -> models.Model:
    crud.endpoint.create_with_model(
        db, obj_in=schemas.EndpointCreate(name=utils.random_string()), model_id=model_with_config.id)
    return model_with_config
