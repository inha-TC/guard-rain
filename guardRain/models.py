# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    admin_number = models.AutoField(primary_key=True, db_comment='테이블 SEQ')
    adminid = models.CharField(db_column='adminID', max_length=30, blank=True, null=True, db_comment='아이디')  # Field name made lowercase.
    adminpw = models.CharField(db_column='adminPW', max_length=512, blank=True, null=True, db_comment='패스워드')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
    id = models.BigAutoField(primary_key=True)
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


class Notice(models.Model):
    notice_number = models.AutoField(primary_key=True, db_comment='테이블 SEQ')
    notice_title = models.CharField(max_length=255, blank=True, null=True, db_comment='제목')
    notice_content = models.TextField(blank=True, null=True, db_comment='내용')
    notice_date = models.DateTimeField(blank=True, null=True, db_comment='게시일')

    class Meta:
        managed = False
        db_table = 'notice'


class RentalList(models.Model):
    rent_number = models.AutoField(primary_key=True, db_comment='테이블 SEQ')
    user_profile_number = models.ForeignKey('UserProfile', models.DO_NOTHING, db_column='user_profile_number', blank=True, null=True, db_comment='user_profile 참조키')
    umbrella_number = models.ForeignKey('Umbrella', models.DO_NOTHING, db_column='umbrella_number', blank=True, null=True, db_comment='umbrella 참조키')
    start_date = models.DateTimeField(blank=True, null=True, db_comment='대여일')
    end_date = models.DateTimeField(blank=True, null=True, db_comment='반납일')
    return_check = models.IntegerField(blank=True, null=True, db_comment='반납여부')

    class Meta:
        managed = False
        db_table = 'rental_list'


class Umbrella(models.Model):
    umbrella_number = models.AutoField(primary_key=True, db_comment='테이블 SEQ')
    umbrella_code = models.IntegerField(unique=True, blank=True, null=True, db_comment='우산 고유번호')
    location = models.CharField(max_length=20, blank=True, null=True, db_comment='주소')
    rent = models.IntegerField(blank=True, null=True, db_comment='상태')
    break_or_lost = models.IntegerField(blank=True, null=True, db_comment='상태2')
    model = models.CharField(max_length=1, blank=True, null=True, db_comment='우산 크기')
    color = models.CharField(max_length=20, blank=True, null=True, db_comment='우산 색상')

    class Meta:
        managed = False
        db_table = 'umbrella'


class UserInfo(models.Model):
    user_number = models.AutoField(primary_key=True, db_comment='테이블 SEQ')
    userid = models.CharField(db_column='userID', max_length=30, blank=True, null=True, db_comment='아이디')  # Field name made lowercase.
    userpw = models.CharField(db_column='userPW', max_length=512, blank=True, null=True, db_comment='패스워드')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_info'


class UserProfile(models.Model):
    user_profile_number = models.AutoField(primary_key=True, db_comment='테이블 SEQ')
    user_number = models.ForeignKey(UserInfo, models.DO_NOTHING, db_column='user_number', blank=True, null=True, db_comment='user_info 참조키')
    userhp = models.CharField(db_column='userHP', max_length=30, blank=True, null=True, db_comment='전화번호')  # Field name made lowercase.
    user_gender = models.CharField(max_length=1, blank=True, null=True, db_comment='성별')

    class Meta:
        managed = False
        db_table = 'user_profile'
