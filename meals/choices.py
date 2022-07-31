from model_utils import Choices

MEALS_CATEGORIES = Choices(
    ('starters', 'Starters'),
    ('mains', 'Mains'),
    ('sides', 'Sides'),
    ('drinks', 'Drinks'),
    ('desserts', 'Desserts'),
)

UNIT_CHOICES = Choices(
    ('fl oz', 'floz', 'Fluid Ounce'),
    ('ml', 'ml', 'Milliliters'),
    ('g', 'g', 'Grams'),
    ('mg', 'mg', 'Milligrams'),
    ('mcg', 'mcg', 'Micrograms'),
)
