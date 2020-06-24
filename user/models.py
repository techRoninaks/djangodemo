from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user_id', 'group_id'),)


class AuthUserUserPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user_id', 'permission_id'),)


class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    uid = models.CharField(max_length=55)
    is_disabled = models.IntegerField()
    is_active = models.IntegerField()
    created_date = models.DateTimeField()
    created_by = models.IntegerField()
    modified_date = models.DateTimeField()
    modified_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'client'


class Clientcountry(models.Model):
    clientcountry_id = models.AutoField(primary_key=True)
    client_id = models.IntegerField()
    country_id = models.IntegerField()
    is_disabled = models.IntegerField()
    is_active = models.IntegerField()
    created_date = models.DateTimeField()
    created_by = models.IntegerField()
    modified_date = models.DateTimeField()
    modified_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'clientcountry'


class Country(models.Model):
    country_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    flag = models.IntegerField()
    currency_name = models.CharField(max_length=55)
    currency_code = models.CharField(max_length=55)
    is_active = models.IntegerField()
    created_date = models.DateTimeField()
    created_by = models.IntegerField()
    modified_date = models.DateTimeField()
    modified_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'country'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HomeUser(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.IntegerField()
    user_id_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'home_user'


class Permission(models.Model):
    permission_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=55)
    index = models.IntegerField()
    is_active = models.IntegerField()
    created_date = models.DateTimeField()
    created_by = models.IntegerField()
    modified_date = models.DateTimeField()
    modified_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'permission'


class Store(models.Model):
    store_id = models.AutoField(primary_key=True)
    uid = models.CharField(max_length=70)
    client_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'store'


class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=254)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_active = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'user'


class Userpermission(models.Model):
    userpermission_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    is_active = models.IntegerField()
    created_date = models.IntegerField()
    created_by = models.DateTimeField()
    modified_date = models.IntegerField()
    modified_by = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'userpermission'


class Userprofile(models.Model):
    userprofile_id = models.AutoField(primary_key=True)
    user_id = models.IntegerField()
    uid = models.CharField(max_length=50)
    user_type = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    allowed_clients = models.TextField()
    allowed_countries = models.TextField()
    allowed_stores = models.TextField()
    profile_pic = models.IntegerField()
    email_notification = models.IntegerField()
    is_disabled = models.IntegerField()
    is_active = models.IntegerField()
    created_date = models.DateTimeField()
    created_by = models.IntegerField()
    modified_date = models.DateTimeField()
    modified_by = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'userprofile'