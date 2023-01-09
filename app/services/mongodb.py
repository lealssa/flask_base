from typing import List
from pymongo import MongoClient
from decimal import Decimal
from bson.codec_options import CodecOptions
from bson.codec_options import TypeRegistry
from bson.decimal128 import Decimal128
from bson.codec_options import TypeCodec

from config import settings

# from models.investimento import InvestimentoRendaFixaModel

class DecimalCodec(TypeCodec):
     python_type = Decimal    # the Python type acted upon by this type codec
     bson_type = Decimal128   # the BSON type acted upon by this type codec
     def transform_python(self, value):
         """Function that transforms a custom type value into a type
         that BSON can encode."""
         return Decimal128(value)
     def transform_bson(self, value):
         """Function that transforms a vanilla BSON type value into our
         custom type."""
         return value.to_decimal()

class MongoDbService():    

    def __init__(self): 

        self.client = MongoClient(settings.mongodb_dsn)
        self._db = self.client[settings.db_name]

        decimal_codec = DecimalCodec()    
        type_registry = TypeRegistry([decimal_codec])        
        codec_options = CodecOptions(type_registry=type_registry)

        self._collection = self._db.get_collection('my_collection', codec_options=codec_options)