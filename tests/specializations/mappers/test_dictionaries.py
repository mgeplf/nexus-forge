from kgforge.core.resources import Resource, Resources
from kgforge.specializations.mappers.dictionaries import DictionaryMapper


class TestJsonMapper:

    def test_apply_scope(self, forge):
        rule = "json.dumps({'value': 1})"
        mapping = f"property: {rule}"
        data = {"name": "Jane Doe"}
        mapper = DictionaryMapper(forge, mapping)
        resource = mapper.apply(data)
        assert resource.property == rule

    def test_apply_on_data_one_flat(self, json_mapper_flat, json_data_one):
        resource = json_mapper_flat.map(json_data_one)
        assert isinstance(resource, Resource)
        assert resource.type == "Person"

    def test_apply_on_data_one_nested(self, json_mapper_nested, json_data_one):
        resource = json_mapper_nested.map(json_data_one)
        assert isinstance(resource, Resource)
        assert resource.type == "Contribution"
        assert resource.agent.type == "Person"

    def test_apply_on_data_many_flat(self, json_mapper_flat, json_data_many):
        resources = json_mapper_flat.map(json_data_many)
        assert isinstance(resources, Resources)
        resource = resources[-1]
        assert isinstance(resource, Resource)
        assert resource.type == "Person"

    def test_apply_on_data_many_nested(self, json_mapper_nested, json_data_many):
        resources = json_mapper_nested.map(json_data_many)
        assert isinstance(resources, Resources)
        resource = resources[-1]
        assert isinstance(resource, Resource)
        assert resource.type == "Contribution"
        assert resource.agent.type == "Person"
