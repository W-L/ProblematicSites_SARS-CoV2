#!/usr/bin/env python3

import unittest
import vcf
from subprocess import Popen, PIPE


class TestVCF(unittest.TestCase):
    def test_pyvcf(self):
        try:
            with open("problematic_sites_sarsCov2.vcf", "r") as vcf_fi:
                vcf_reader = vcf.Reader(vcf_fi)
        except SyntaxError:
            self.fail("Error when parsing the new VCF using PyVCF")
    def test_bcftools(self):
        p = Popen(["bcftools", "view", "{0}".format("problematic_sites_sarsCov2.vcf")], stdout=PIPE, stderr=PIPE)
        output, error = p.communicate()
        assert len(error) == 0


if __name__ ==  "__main__":
    unittest.main()
