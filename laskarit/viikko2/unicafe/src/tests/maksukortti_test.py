import unittest
from maksukortti import Maksukortti



class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 10.00 euroa")

    def test_saldo_kasvaa_oikein(self):
        self.maksukortti.lataa_rahaa(1000)
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 20.00 euroa")

    def test_rahan_ottaminen_toimii(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 5.00 euroa")

    def test_rahan_ottaminen_toimii_kaksi(self):
        self.maksukortti.ota_rahaa(2000)
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 10.00 euroa")

    def test_rahan_ottaminen_toimii_kolme(self):
        self.assertIs(self.maksukortti.ota_rahaa(100), True)

    def test_rahan_ottaminen_toimii_nelja(self):
        self.assertIs(self.maksukortti.ota_rahaa(10001), False)
