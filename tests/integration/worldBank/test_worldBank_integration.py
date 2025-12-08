import unittest
import tradingeconomics as te


class TestWorldBankIntegration(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        te.login("guest:guest")

    def test_getWBCategories_none(self):
        res = te.getWBCategories(category=None)
        self.assertIsInstance(res, list)
        self.assertTrue(len(res) > 0)

    def test_getWBCategories_education(self):
        res = te.getWBCategories(category="education")
        self.assertIsInstance(res, list)
        self.assertTrue(any("education" in (str(r).lower()) for r in res))

    def test_getWBIndicator_fr_inr_rinr(self):
        res = te.getWBIndicator(series_code="fr.inr.rinr")
        self.assertIsInstance(res, list)
        self.assertTrue(len(res) > 0)

    def test_getWBIndicator_usa_fr_inr_rinr(self):
        res = te.getWBIndicator(series_code="usa.fr.inr.rinr")
        self.assertIsInstance(res, list)
        self.assertTrue(len(res) > 0)

    def test_getWBCountry_portugal(self):
        res = te.getWBCountry(country="Portugal")
        self.assertIsInstance(res, list)
        self.assertTrue(len(res) > 0)

    def test_getWBIndicator_url(self):
        res = te.getWBIndicator(
            url="/united-states/real-interest-rate-percent-wb-data.html"
        )
        self.assertIsInstance(res, list)
        self.assertTrue(len(res) > 0)

    def test_getWBHistorical_single(self):
        res = te.getWBHistorical(series_code="usa.fr.inr.rinr")
        self.assertIsInstance(res, list)
        self.assertTrue(len(res) > 0)

    def test_getWBHistorical_multiple(self):
        res = te.getWBHistorical(series_code="usa.fr.inr.rinr,prt.ag.con.fert.pt.zs")
        self.assertIsInstance(res, list)
        self.assertTrue(len(res) > 0)


if __name__ == "__main__":
    unittest.main()
