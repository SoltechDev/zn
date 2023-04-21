from tortoise import fields, models

class User(models.Model):
    
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    display_name = fields.CharField(max_length=50, null=True)
    password = fields.CharField(max_length=255, null=True)
    
    created_at = fields.DatetimeField(auto_now_add = True)
    updated_at = fields.DatetimeField(auto_now = True)

class Post(models.Model):
    
    id = fields.IntField(pk=True)
    author = fields.ForeignKeyField('models.User', on_delete='CASCADE', related_name='posts')
    title = fields.CharField(index=True, max_length=255)
    content = fields.TextField()
    points = fields.IntField(default=0)
    created_at = fields.DatetimeField(auto_now_add = True)
    updated_at = fields.DatetimeField(auto_now = True)