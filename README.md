Django Rest Framework base64 fields
Installation:
>pip django-rest-framework-base64-fields  

Usage:  

>class MySerializer(serializers.ModelSerializer):
    some_file = Base64FileField()