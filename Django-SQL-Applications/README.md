# Django Database Operations Cheat Sheet

## Define a Model

```python
from django.db import models

class MyModel(models.Model):
    field1 = models.CharField(max_length=100)
    field2 = models.IntegerField()
```

## Create Database Tables

```bash
python manage.py makemigrations
python manage.py migrate
```

## Retrieve All Instances

```python
MyModel.objects.all()
```

## Filter Objects

```python
MyModel.objects.filter(field1="value")
MyModel.objects.filter(field2__gt=5)
```

## Retrieve a Single Instance

```python
MyModel.objects.get(field1="value")
```

## Create & Save an Instance

```python
obj = MyModel(field1="value", field2=5)
obj.save()
```

## Update & Save

```python
obj.field1 = "new value"
obj.save()
```

## Delete an Object

```python
obj.delete()
```

## Retrieve Related Model

```python
obj.related_model
```

## Fetch All Related Objects

```python
obj.model_set.all()
```

## Filter Based on Related Model's Field

```python
MyModel.objects.filter(related_model__field="value")
```

## Exact Match

```python
MyModel.objects.filter(field__exact="value")
```

## Case-Insensitive Match

```python
MyModel.objects.filter(field__iexact="value")
```

## Substring Match

```python
MyModel.objects.filter(field__contains="value")
```
