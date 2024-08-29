"""
This script tests the HF-in-HF energies of sample molecular and periodic systems

Author(s): Minsik Cho
"""

import unittest
from pyscf import gto, scf
from molbe import fragpart, BE

class TestHFinHF(unittest.TestCase):
    def test_h8_be1(self):
        mol = gto.M()
        mol.atom = [['H', (0.,0.,i)] for i in range(8)]
        mol.basis = 'sto-3g'
        mol.charge = 0.; mol.spin = 0.
        mol.build()
        mf = scf.RHF(mol); mf.kernel()
        fobj = fragpart(frag_type='autogen', be_type='be1', mol = mol)
        mybe = BE(mf, fobj)
        self.assertAlmostEqual(mybe.ebe_hf, mf.e_tot, msg = "HF-in-HF energy for H8 (BE1) does not match the HF energy!")

if __name__ == '__main__':
    unittest.main()
