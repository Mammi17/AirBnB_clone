#!/usr/bin/python3
"""TestFileStorage_instantiation
    TestFileStorage_methods"""
import os
import models
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage_inst(unittest.TestCase):
    """testing instantiation of the FileStorage class."""

    def test_FileStorage_inst_no_args(self):
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_FileStorage_inst_with_arg(self):
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_FileStorage_file_path_is_private_str(self):
        self.assertEqual(str, type(FileStorage._FileStorage__file_path))

    def testFileStorage_objects_is_private_dict(self):
        self.assertEqual(dict, type(FileStorage._FileStorage__objects))

    def test_storage_init(self):
        self.assertEqual(type(models.storage), FileStorage)


class TestFileStorage_method(unittest.TestCase):
    """testing methods of the FileStorage class."""

    def setUp(self):
        pass

    def tearDown(self) -> None:
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        self.assertEqual(dict, type(models.storage.all()))

    def test_all_avec_arg(self):
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_nouveau(self):
        base_m = BaseModel()
        u = User()
        ste = State()
        plce = Place()
        cty = City()
        amty = Amenity()
        rview = Review()
        models.storage.new(base_m)
        models.storage.new(u)
        models.storage.new(ste)
        models.storage.new(plce)
        models.storage.new(cty)
        models.storage.new(amty)
        models.storage.new(rview)
        self.assertIn("BaseModel." + base_m.id, models.storage.all().keys())
        self.assertIn(base_m, models.storage.all().values())
        self.assertIn("User." + u.id, models.storage.all().keys())
        self.assertIn(u, models.storage.all().values())
        self.assertIn("State." + ste.id, models.storage.all().keys())
        self.assertIn(ste, models.storage.all().values())
        self.assertIn("Place." + plce.id, models.storage.all().keys())
        self.assertIn(plce, models.storage.all().values())
        self.assertIn("City." + cty.id, models.storage.all().keys())
        self.assertIn(cty, models.storage.all().values())
        self.assertIn("Amenity." + amty.id, models.storage.all().keys())
        self.assertIn(amty, models.storage.all().values())
        self.assertIn("Review." + rview.id, models.storage.all().keys())
        self.assertIn(rview, models.storage.all().values())

    def test_new_avec_args(self):
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

    def test_new_avec_None(self):
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save(self):
        base_m = BaseModel()
        u = User()
        ste = State()
        plce = Place()
        cty = City()
        amty = Amenity()
        rview = Review()
        models.storage.new(base_m)
        models.storage.new(u)
        models.storage.new(ste)
        models.storage.new(plce)
        models.storage.new(cty)
        models.storage.new(amty)
        models.storage.new(rview)
        models.storage.save()
        save_texte = ""
        with open("file.json", "r") as f:
            save_texte = f.read()
            self.assertIn("BaseModel." + base_m.id, save_texte)
            self.assertIn("User." + u.id, save_texte)
            self.assertIn("State." + ste.id, save_texte)
            self.assertIn("Place." + plce.id, save_texte)
            self.assertIn("City." + cty.id, save_texte)
            self.assertIn("Amenity." + amty.id, save_texte)
            self.assertIn("Review." + rview.id, save_texte)

    def test_save_avec_arg(self):
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload(self):
        base_m = BaseModel()
        u = User()
        ste = State()
        plce = Place()
        cty = City()
        amty = Amenity()
        rview = Review()
        models.storage.new(base_m)
        models.storage.new(u)
        models.storage.new(ste)
        models.storage.new(plce)
        models.storage.new(cty)
        models.storage.new(amty)
        models.storage.new(rview)
        models.storage.save()
        models.storage.reload()
        objet = FileStorage._FileStorage__objects
        self.assertIn("BaseModel." + base_m.id, objet)
        self.assertIn("User." + u.id, objet)
        self.assertIn("State." + ste.id, objet)
        self.assertIn("Place." + plce.id, objet)
        self.assertIn("City." + cty.id, objet)
        self.assertIn("Amenity." + amty.id, objet)
        self.assertIn("Review." + rview.id, objet)

    def test_reload_avec_arg(self):
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()
