from typing import NoReturn, Dict
from medicine.models import Inventory
import csv
import logging


class HomeUtils:

    def __init__(self):
        pass

    def search_data(self, medicine_name: str) -> Dict:
        data = {}
        try:
            dt = []
            result = Inventory.objects.filter(sku_name__startswith=medicine_name)
            for entry in result:
                entry = entry.__dict__
                entry.pop('_state')
                dt.append(entry)
                dt.append(entry)

            data = {
                'data': dt
            }
        except Exception as e:
            logging.exception(e)
        return data

    def import_csv(self, filename: str) -> NoReturn:
        try:
            with open('media/%s' % filename, 'r') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                header = []
                for row in reader:

                    if not header:
                        header = row
                    else:
                        try:
                            sku_id, product_id, sku_name, price, manufacturer_name, salt_name, drug_form, \
                            pack_size, strength, product_banned_flag, unit, price_per_unit = row
                            if sku_id == '-':
                                sku_id = None
                            if product_id == '-':
                                product_id = None
                            if product_banned_flag == '-':
                                product_banned_flag = None
                            else:
                                product_banned_flag = bool(product_banned_flag)
                            price = float(str(price).replace(' ', ''))

                            if unit == '-':
                                unit = None
                            if price_per_unit == '-':
                                price_per_unit = None
                            if price_per_unit is not None:
                                price_per_unit = float(str(price_per_unit).replace(' ', ''))

                            c = Inventory.objects.update_or_create(sku_id=sku_id, product_id=product_id,
                                                                   sku_name=sku_name,
                                                                   price=float(price),
                                                                   manufacturer_name=manufacturer_name,
                                                                   salt_name=salt_name,
                                                                   drug_form=drug_form,
                                                                   pack_size=pack_size, strength=strength,
                                                                   product_banned_flag=product_banned_flag, unit=unit,
                                                                   price_per_unit=price_per_unit)

                            if not c:
                                raise Exception("Insertion failed: %s " % c[0])

                        except Exception as e:
                            logging.error("Invalid entry in csv: %s " % row)
                            logging.exception(e)
        except Exception as e:
            logging.exception(e)
