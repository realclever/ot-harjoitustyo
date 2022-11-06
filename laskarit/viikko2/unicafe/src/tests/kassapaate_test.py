import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti


class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaate_luotu(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_kassapaate_saldo_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edulliset_saldo_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_saldo_oikein(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_maksu_riittava_rahamaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_maukkaat_maksu_riittava_rahamaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_edullinen_maksu_riittava_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(400), 160)

    def test_maukas_maksu_riittava_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_edulliset_kateinen_toimii_luonaat_kasvaa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukkaat_kateinen_toimii_luonaat_kasvaa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_jos_maksu_ei_riittava_rahamaara_ei_muutu_edullinen(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_jos_maksu_ei_riittava_rahamaara_ei_muutu_maukas(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_edullinen_maksu_ei_riittava_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(239), 239)

    def test_maukas_maksu_ei_riittava_vaihtoraha_oikein(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(399), 399)

    def test_edulliset_kateinen_ei_riittava_luonaat_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(239)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_maukkaat_kateinen_ei_riittava_luonaat_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(399)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edulliset_korttimaksu_riittava_veloitus_true(self):
        self.assertIs(self.kassapaate.syo_edullisesti_kortilla(
            self.maksukortti), True)

    def test_maukkaat_korttimaksu_riittava_veloitus_true(self):
        self.assertIs(self.kassapaate.syo_maukkaasti_kortilla(
            self.maksukortti), True)

    def test_edulliset_kortin_saldo_muuttuu(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")

    def test_maukkaat_kortin_saldo_muuttuu(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")

    def test_jos_kortilla_rahaa_lounaat_kasvaa_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_jos_kortilla_rahaa_lounaat_kasvaa_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_rahamaara_ei_muutu_kortilla_ostaessa_edulliset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_rahamaara_ei_muutu_kortilla_ostaessa_maukkaat(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertAlmostEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_jos_kortilla_ei_tarpeeksi_rahaa_edulliset(self):
        self.assertIs(self.kassapaate.syo_edullisesti_kortilla(
            Maksukortti(239)), False)
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_jos_kortilla_ei_tarpeeksi_rahaa_maukkaat(self):
        self.assertIs(self.kassapaate.syo_maukkaasti_kortilla(
            Maksukortti(399)), False)
        self.assertEqual(str(self.maksukortti),
                         "Kortilla on rahaa 10.00 euroa")
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kortin_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.maksukortti.saldo, 1100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_kortin_negatiivinen_lataus(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.maksukortti.saldo, 1000)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
