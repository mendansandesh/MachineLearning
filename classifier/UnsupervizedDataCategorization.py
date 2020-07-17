import Categorize
from time import time
if __name__ == '__main__':
    #input = 'https://www.voanews.com/science-health/who-ebola-epidemic-dr-congo-may-be-nearing-its-end'
    #input = '/../../../etc/password'
    #input = 'https://www.amazon.in/gp/product/B07S6P5FQ3/ref=ox_sc_act_title_6?smid=A2VQOLRW0XTGMB&psc=1'
    #input = 'SELECT COUNT(DISTINCT p.product_id) AS total FROM oc_category_path cp LEFT JOIN oc_product_to_category p2c ON (cp.category_id = p2c.category_id) LEFT JOIN oc_product p ON (p2c.product_id = p.product_id) LEFT JOIN oc_product_description pd ON (p.product_id = pd.product_id) LEFT JOIN oc_product_to_store p2s ON (p.product_id = p2s.product_id) WHERE pd.language_id = \'1\' AND p.status = \'1\' AND p.date_available <= NOW() AND p2s.store_id = \'0\' AND cp.path_id = \'41\''
    #input = 'https://www.emirates.com/passenger/passport_num=21314351341DFSDF'
    input = 'select * from locations where machine_id = 213'

    start_time = time()
    print('DataCategory is: ', Categorize.detectCategory(input))
    print("Time taken : ", round(time() - start_time, 3), "s")