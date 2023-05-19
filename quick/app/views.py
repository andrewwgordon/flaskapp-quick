from flask_appbuilder.actions import action
from flask import redirect
from flask_appbuilder import ModelView
from flask_appbuilder.models.sqla.interface import SQLAInterface

from . import appbuilder, db
from .models import ProductCategory,Product

class ProductView(ModelView):
    datamodel = SQLAInterface(Product)
    label_columns = {'product_category.name':'Product Category'}
    list_columns = ["name", "product_category.name"]

    @action("add_product_to_order","Add Product to Order","Add Product to Order?","fa-rocket")
    def add_product_to_order(self, item):
        print(item)
        return redirect(self.get_redirect())

class ProductCategoryView(ModelView):
    datamodel = SQLAInterface(ProductCategory)  
    related_views = [ProductView]

db.create_all()

appbuilder.add_view(
    ProductCategoryView, "Product Categories", icon="fa-folder-open-o", category="Products"
)
appbuilder.add_view(
    ProductView, "Products", icon="fa-folder-open-o", category="Products"
)