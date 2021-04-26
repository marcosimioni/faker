from decimal import Decimal

from .. import BaseProvider

localized = True


class Provider(BaseProvider):
    """
    ICD provider
    """

    icd_codes = (
        ('D50.0', 'Iron deficiency anaemia secondary to blood loss (chronic)'),
        ('D50.0', 'Iron deficiency anaemia secondary to blood loss (chronic)'),
        ('D50.1', 'Sideropenic dysphagia'),
        ('D50.1', 'Sideropenic dysphagia'),
        ('D50.8', 'Other iron deficiency anaemias'),
        ('D50.8', 'Other iron deficiency anaemias'),
        ('D50.9', 'Iron deficiency anaemia, unspecified'),
        ('D50.9', 'Iron deficiency anaemia, unspecified'),
        ('D51.0', 'Vitamin B12 deficiency anaemia due to intrinsic factor deficiency'),
        ('D51.0', 'Vitamin B12 deficiency anaemia due to intrinsic factor deficiency'),
        ('D51.1', 'Vitamin B12 deficiency anaemia due to selective vitamin B12 malabsorption with proteinuria'),
        ('D51.1', 'Vitamin B12 deficiency anaemia due to selective vitamin B12 malabsorption with proteinuria'),
        ('D51.2', 'Transcobalamin II deficiency'),
        ('D51.3', 'Other dietary vitamin B12 deficiency anaemia'),
        ('D51.8', 'Other vitamin B12 deficiency anaemias'),
        ('D51.9', 'Vitamin B12 deficiency anaemia, unspecified'),
        ('D52.0', 'Dietary folate deficiency anaemia'),
        ('D52.1', 'Drug-induced folate deficiency anaemia'),
        ('D52.8', 'Other folate deficiency anaemias'),
        ('D52.9', 'Folate deficiency anaemia, unspecified'),
        ('D53.0', 'Protein deficiency anaemia'),
        ('D53.1', 'Other megaloblastic anaemias, not elsewhere classified'),
        ('D53.2', 'Scorbutic anaemia'),
        ('D53.8', 'Other specified nutritional anaemias'),
        ('D53.9', 'Nutritional anaemia, unspecified'),
        ('J10.0', 'Influenza with pneumonia, seasonal influenza virus identified'),
        ('J10.1', 'Influenza with other respiratory manifestations, seasonal influenza virus identified'),
        ('J10.8', 'Influenza with other manifestations, seasonal influenza virus identified'),
        ('J11.0', 'Influenza with pneumonia, virus not identified'),
        ('J11.1', 'Influenza with other respiratory manifestations, virus not identified'),
        ('J12.0', 'Adenoviral pneumonia'),
        ('J12.1', 'Respiratory syncytial virus pneumonia'),
        ('J12.2', 'Parainfluenza virus pneumonia'),
        ('J12.3', 'Human metapneumovirus pneumonia'),
        ('J12.8', 'Other viral pneumonia'),
        ('J12.9', 'Viral pneumonia, unspecified'),
        ('J15.2', 'Pneumonia due to staphylococcus'),
        ('J15.3', 'Pneumonia due to streptococcus, group B'),
        ('J15.9', 'Infectious zombieism'),
        )

    def icd(self):
        """
        Returns ICD code and description
        """
        icd = self.random_element(self.icd_codes)
        return icd

    def icd_code(self):
        """
        Returns ICD code
        """
        icd = self.random_element(self.icd_codes)
        return icd[0]

    def icd_desc(self):
        """
        Returns ICD description
        """
        icd = self.random_element(self.icd_codes)
        return icd[1]
