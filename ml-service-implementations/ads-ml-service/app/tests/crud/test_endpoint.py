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


import pickle
import typing
import datetime as dt

import sqlalchemy.orm as orm

import app.core.supported_lib as supported_lib
import app.crud as crud
import app.models as models
import app.schemas as schemas
import app.tests.utils.utils as utils


def test_create_endpoint(db: orm.Session, model_in_db: models.Model) -> typing.NoReturn:
    endpoint_name = utils.random_string()
    endpoint_in = schemas.EndpointCreate(name=endpoint_name)
    endpoint = crud.endpoint.create_with_model(db, obj_in=endpoint_in, model_id=model_in_db.id)

    assert endpoint.name == endpoint_name
    assert endpoint.model_id == model_in_db.id
    assert endpoint.deployed_at.date() == dt.datetime.now(tz=dt.timezone.utc).date()
    assert endpoint.deployed_at.hour == dt.datetime.now(tz=dt.timezone.utc).hour
    assert endpoint.deployed_at.minute == dt.datetime.now(tz=dt.timezone.utc).minute


def test_cascade_delete_with_binary(
        db: orm.Session,
        endpoint_in_db: models.Model,
        classification_predictor: object
) -> typing.NoReturn:
    binary_in = schemas.BinaryMlModelCreate(
        model_b64=pickle.dumps(classification_predictor),
        library=supported_lib.MlLib.SKLearn
    )
    binary = crud.binary_ml_model.create_with_endpoint(db, obj_in=binary_in, endpoint_id=endpoint_in_db.id)
    crud.endpoint.delete(db, id=endpoint_in_db.id)
    binary_1 = crud.binary_ml_model.get(db, id=binary.id)

    assert binary_1 is None
