from flask import redirect
from flask_appbuilder.actions import action
from flask_appbuilder import Model
from sqlalchemy import Column, Date, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import relationship


class ProductCategory(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Product(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)
    description = Column(String(250))
    product_category_id = Column(Integer, ForeignKey('product_category.id'), nullable=False)
    product_category = relationship("ProductCategory")

    def __repr__(self):
        return self.name