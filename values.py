MAIN_COMBOBOX_VALUES = ["Mass", "Length", 'Volume', "Pressure"]

SECONDARY_ITEM_MASS = ["Ton", "Kg", "g"]
SECONDARY_ITEM_LENGTH = ["Km", "m", "Cm"]
SECONDARY_ITEM_VOLUME = ['m^3', 'Cm^3', "L", "ml"]
SECONDARY_ITEM_PRESSURE = ["Pascal", "Bar"]

VALUES_DICT = {
    "Ton": "1000000",
    "Kg": "1000",
    "g": "1",
    "Km": "100000",
    "m": '100',
    "Cm": "1",
    "m^3": "1000000",
    "Cm^3": "1",
    "L": "1000",
    "ml": "1",
    "Pascal": "0.00001",
    "Bar": "1"}

MAIN_DICT = {"Mass": SECONDARY_ITEM_MASS,
             "Length": SECONDARY_ITEM_LENGTH,
             "Volume": SECONDARY_ITEM_VOLUME,
             "Pressure": SECONDARY_ITEM_PRESSURE}
