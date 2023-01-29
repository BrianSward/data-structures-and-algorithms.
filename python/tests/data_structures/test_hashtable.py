import pytest
from python.data_structures.hashtable import Hashtable

# @pytest.mark.skip("TODO")
def test_exists():
    assert Hashtable


# @pytest.mark.skip("TODO")
def test_get_apple():
    hashtable = Hashtable()
    hashtable.set("apple", "Used for apple sauce")
    actual = hashtable.get("apple")
    expected = "Used for apple sauce"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_internals():
    hashtable = Hashtable(1024)
    hashtable.set("ahmad", 30)
    hashtable.set("silent", True)
    hashtable.set("listen", "to me")

    actual = []

    # NOTE: purposely breaking encapsulation to test the "internals" of Hashmap
    for item in hashtable._buckets:
        if item:
            actual.append(item.display())

    expected = [[["silent", True], ["listen", "to me"]], [["ahmad", 30]]]

    assert actual == expected


# @pytest.mark.skip("TODO")
def test_hash_value():
    hashtable = Hashtable()
    actual = hashtable._hash("apple")
    expected = 0
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_return_unique_keys():
    hashtable = Hashtable()
    hashtable.set("name", "brian")
    hashtable.set("name", "tom")
    hashtable.set("hobby", "running")
    hashtable.set("pet_name", "chickpea")
    expected = ['name', 'hobby', 'pet_name']
    actual = hashtable.keys()
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_return_null_for_get():
    hashtable = Hashtable()
    hashtable.set("name", "brian")
    hashtable.set("name", "tom")
    hashtable.set("hobby", "running")
    hashtable.set("pet_name", "chickpea")
    expected = None
    actual = hashtable.get("phil")
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_return_value_from_collision():
    hashtable = Hashtable()
    hashtable.set("name", "brian")
    hashtable.set("name", "running")
    expected = 'brian'
    actual = hashtable.get('name')
    assert actual == expected

