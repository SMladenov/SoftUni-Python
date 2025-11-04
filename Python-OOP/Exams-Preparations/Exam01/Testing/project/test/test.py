from project.gallery import Gallery

import unittest

class GalleryTests (unittest.TestCase):

    def setUp(self):
        self.gallery = Gallery("ArtHouse1", "New York", 150.5, True)

    def test_init(self):
        self.assertEqual(self.gallery.gallery_name, "ArtHouse1")
        self.assertEqual(self.gallery.city, "New York")
        self.assertEqual(self.gallery.area_sq_m, 150.5)
        self.assertTrue(self.gallery.open_to_public)
        self.assertEqual(self.gallery.exhibitions, {})

    def test_invalid_gallery_name(self):
        with self.assertRaises(ValueError) as context:
            Gallery("Art House!", "Paris", 200.0)
        self.assertEqual(str(context.exception), "Gallery name can contain letters and digits only!")

    def test_invalid_city_name(self):
        with self.assertRaises(ValueError) as context:
            Gallery("Gallery1", "1Paris", 200.0)
        self.assertEqual(str(context.exception), "City name must start with a letter!")

    def test_invalid_area(self):
        with self.assertRaises(ValueError) as context:
            Gallery("Gallery1", "Paris", -10)
        self.assertEqual(str(context.exception), "Gallery area must be a positive number!")

    def test_add_exhibition_success(self):
        result = self.gallery.add_exhibition("Modern Art", 2024)
        self.assertEqual(result, 'Exhibition "Modern Art" added for the year 2024.')
        self.assertEqual(self.gallery.exhibitions, {"Modern Art": 2024})


    def test_add_existing_exhibition(self):
        self.gallery.add_exhibition("Impressionism", 2023)
        result = self.gallery.add_exhibition("Impressionism", 2025)
        self.assertEqual(result, 'Exhibition "Impressionism" already exists.')
        self.assertEqual(self.gallery.exhibitions["Impressionism"], 2023)

    def test_remove_exhibition_success(self):
        self.gallery.add_exhibition("Sculptures", 2022)
        result = self.gallery.remove_exhibition("Sculptures")
        self.assertEqual(result, 'Exhibition "Sculptures" removed.')
        self.assertNotIn("Sculptures", self.gallery.exhibitions)

    def test_remove_non_existent_exhibition(self):
        result = self.gallery.remove_exhibition("Photography")
        self.assertEqual(result, 'Exhibition "Photography" not found.')
    
    def test_list_exhibitions_open(self):
        self.gallery.add_exhibition("Abstract Art", 2025)
        self.gallery.add_exhibition("Classic Paintings", 2023)
        result = self.gallery.list_exhibitions()
        expected_output = "Abstract Art: 2025\nClassic Paintings: 2023"
        self.assertEqual(result, expected_output)

    def test_list_exhibitions_closed(self):
        self.gallery.open_to_public = False
        result = self.gallery.list_exhibitions()
        self.assertEqual(result, "Gallery ArtHouse1 is currently closed for public! Check for updates later on.")


if __name__ == '__main__':
    unittest.main()