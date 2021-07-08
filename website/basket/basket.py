from index.models import Product


class Basket():

    def __init__(self, request):
        self.session = request.session
        basket = self.session.get('skey')
        if 'skey' not in request.session:
            basket = self.session['skey'] = {}
        self.basket = basket

    def add(self, product):
        product_id = str(product.id)

        if product_id in self.basket:
            self.basket[product_id]['qty'] = self.basket[product_id]['qty'] + int(1)
            self.basket[product_id]['price'] = float(float(self.basket[product_id]['price']) + float(product.regular_price))
        else:
            self.basket[product_id] = {'price': float(product.regular_price), 'qty': int(1)}

        self.save()



    def __iter__(self):
        product_ids = self.basket.keys()
        products = Product.objects.filter(id__in=product_ids)
        basket = self.basket.copy()

        for product in products:
            basket[str(product.id)]['product'] = product
        
        for item in basket.values():
            yield item
    
    def __len__(self):
        return sum(item['qty'] for item in self.basket.values())




    def get_total_price(self):
        summ = float(sum(float(item['price']) for item in self.basket.values()))
        final_summ = float("{:.2f}".format(summ))
        return final_summ
    

    def delete(self, product):

        product_id = str(product)

        if product_id in self.basket:
            del self.basket[product_id]
            self.save()
    

    def save(self):
        self.session.modified = True
    
    def clear(self):
        self.basket.clear()
        self.save()
