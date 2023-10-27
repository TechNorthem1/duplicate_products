import requests
import json
from datetime import datetime

def all_products(page):

    url = f"https://titandecko.com.co/wp-json/wc/v3/products?page={page}&per_page=100"

    payload = {}
    headers = {
    'Authorization': 'Basic Y2tfNTdiYTg3MzgyMDNiNTM3N2NjN2E4ZjVmYjI0NDRiY2YzNGQ3MDcxMzpjc182ZmY4NDI3MjAwMjg5MjRhMGJkOGQzMWU1OWE2ZWRlOThjMmI5ODEw',
    'Cookie': 'mailchimp_landing_site=https%3A%2F%2Ftitandecko.com.co%2F%2Fwp-json%2Fwc%2Fv3%2Fproducts%3Forder%3Ddesc%26orderby%3Dprice; wfwaf-authcookie-2ad92c32aa83fb61c55f0195bcbc87d2=2245%7Cadministrator%7Cmanage_options%2Cunfiltered_html%2Cedit_others_posts%2Cupload_files%2Cpublish_posts%2Cedit_posts%2Cread%7C0da8dea9ce81dd685ed65dc71eba81cfc8ede229e6172e12540695aa4e38aedc'
    }

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json()


def get_product_by_id(id):

    url = f"https://titandecko.com.co/wp-json/wc/v3/products/{id}"


    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic Y2tfNTdiYTg3MzgyMDNiNTM3N2NjN2E4ZjVmYjI0NDRiY2YzNGQ3MDcxMzpjc182ZmY4NDI3MjAwMjg5MjRhMGJkOGQzMWU1OWE2ZWRlOThjMmI5ODEw',
        'Cookie': 'mailchimp_landing_site=https%3A%2F%2Ftitandecko.com.co%2F%2Fwp-json%2Fwc%2Fv3%2Fproducts%3Forder%3Ddesc%26orderby%3Dprice; wfwaf-authcookie-2ad92c32aa83fb61c55f0195bcbc87d2=2245%7Cadministrator%7Cmanage_options%2Cunfiltered_html%2Cedit_others_posts%2Cupload_files%2Cpublish_posts%2Cedit_posts%2Cread%7C0da8dea9ce81dd685ed65dc71eba81cfc8ede229e6172e12540695aa4e38aedc'
    }

    response = requests.request("GET", url, headers=headers)
    return response.json()


def delete_product_by_id(id):
    url = f"https://titandecko.com.co/wp-json/wc/v3/products/{id}"


    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic Y2tfNTdiYTg3MzgyMDNiNTM3N2NjN2E4ZjVmYjI0NDRiY2YzNGQ3MDcxMzpjc182ZmY4NDI3MjAwMjg5MjRhMGJkOGQzMWU1OWE2ZWRlOThjMmI5ODEw',
        'Cookie': 'mailchimp_landing_site=https%3A%2F%2Ftitandecko.com.co%2F%2Fwp-json%2Fwc%2Fv3%2Fproducts%3Forder%3Ddesc%26orderby%3Dprice; wfwaf-authcookie-2ad92c32aa83fb61c55f0195bcbc87d2=2245%7Cadministrator%7Cmanage_options%2Cunfiltered_html%2Cedit_others_posts%2Cupload_files%2Cpublish_posts%2Cedit_posts%2Cread%7C0da8dea9ce81dd685ed65dc71eba81cfc8ede229e6172e12540695aa4e38aedc'
    }

    response = requests.request("DELETE", url, headers=headers)
    return response.json()

def create_product(product):
    date_now = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

    product["name"] = f"{product["name"]} (copy)"
    product["sku"] = f"{product["sku"]}n"
    product["date_created"] = date_now
    product["date_created_gmt"] = date_now
    product["date_modified"] = date_now
    product["date_modified_gmt"] = date_now

    product.pop("id", None)


    url = "https://titandecko.com.co/wp-json/wc/v3/products?page=1&per_page=100"
    payload = json.dumps(product)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Basic Y2tfNTdiYTg3MzgyMDNiNTM3N2NjN2E4ZjVmYjI0NDRiY2YzNGQ3MDcxMzpjc182ZmY4NDI3MjAwMjg5MjRhMGJkOGQzMWU1OWE2ZWRlOThjMmI5ODEw',
        'Cookie': 'mailchimp_landing_site=https%3A%2F%2Ftitandecko.com.co%2F%2Fwp-json%2Fwc%2Fv3%2Fproducts%3Forder%3Ddesc%26orderby%3Dprice; wfwaf-authcookie-2ad92c32aa83fb61c55f0195bcbc87d2=2245%7Cadministrator%7Cmanage_options%2Cunfiltered_html%2Cedit_others_posts%2Cupload_files%2Cpublish_posts%2Cedit_posts%2Cread%7C0da8dea9ce81dd685ed65dc71eba81cfc8ede229e6172e12540695aa4e38aedc'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)



if __name__ == "__main__":

    while True:
        page = int(input("Ingrese la pagina de productos: "))

        if page >= 9 or page <= 0:
            break

        products = all_products(page)
        
        for product in products:
            product_to_create = get_product_by_id(product["id"])
            create_product(product_to_create)
            
            
