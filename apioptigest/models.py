from django.db import models


class Answerdiscussion(models.Model):
    id_students = models.ForeignKey('Students', models.DO_NOTHING, db_column='id_students')
    id_topicdiscussion = models.ForeignKey('Topicdiscussion', models.DO_NOTHING, db_column='id_topicDiscussion')
    message = models.TextField()
    file = models.TextField(blank=True, null=True)
    reactions = models.IntegerField(blank=True, null=True)
    created_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'answerdiscussion'


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


class Categirytopic(models.Model):
    name = models.CharField(max_length=100)
    created_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'categirytopic'


class Categorynote(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorynote'


class Class(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    teacher = models.CharField(max_length=200, blank=True, null=True)
    created_date = models.DateField(blank=True, null=True)
    sector = models.ForeignKey('Sector', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'class'


class Cooperation(models.Model):
    id_students = models.ForeignKey('Students', models.DO_NOTHING, db_column='id_students')
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='id_project')

    class Meta:
        managed = False
        db_table = 'cooperation'


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


class Filesproject(models.Model):
    id_project = models.ForeignKey('Project', models.DO_NOTHING, db_column='id_project')
    link = models.TextField()
    created_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'filesproject'


class Notes(models.Model):
    id_categorynote = models.ForeignKey(Categorynote, models.DO_NOTHING, db_column='id_categoryNote')
    id_students = models.ForeignKey('Students', models.DO_NOTHING, db_column='id_students')
    topic = models.CharField(max_length=200, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    type_note = models.CharField(max_length=100)
    color = models.CharField(max_length=45)
    created_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'notes'


class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    created_date = models.DateField()
    students = models.ForeignKey('Students', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'project'


class Sector(models.Model):
    title = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sector'


class Students(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    pseudo = models.CharField(max_length=100)
    civilite = models.CharField(max_length=45)
    photo = models.TextField(blank=True, null=True)
    email = models.CharField(max_length=320)
    pass_field = models.CharField(db_column='pass', max_length=320)
    sector = models.ForeignKey(Sector, models.DO_NOTHING)
    city = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    date_birth = models.DateField(blank=True, null=True)
    created_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'students'


class Tag(models.Model):
    id_topicforum = models.ForeignKey('Topicforum', models.DO_NOTHING, db_column='id_topicForum')
    title = models.CharField(max_length=100)
    created_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'tag'


class Tasks(models.Model):
    id_students = models.ForeignKey(Students, models.DO_NOTHING, db_column='id_students')
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.IntegerField()
    notification = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    color = models.CharField(max_length=45)
    created_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'tasks'


class CheckMailCode(models.Model):
    students_id = models.ForeignKey(Students, models.DO_NOTHING, db_column='students_id')
    code = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'checkMailCode'


class Topicdiscussion(models.Model):
    id_students = models.ForeignKey(Students, models.DO_NOTHING, db_column='id_students')
    id_topicforum = models.ForeignKey('Topicforum', models.DO_NOTHING, db_column='id_topicForum')
    message = models.TextField()
    reaction = models.IntegerField(blank=True, null=True)
    file = models.TextField(blank=True, null=True)
    created_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'topicdiscussion'


class Topicforum(models.Model):
    id_students = models.ForeignKey(Students, models.DO_NOTHING, db_column='id_students')
    id_categirytopic = models.ForeignKey(Categirytopic, models.DO_NOTHING, db_column='id_categiryTopic')
    title = models.CharField(max_length=200)
    reactions = models.IntegerField()
    status = models.IntegerField()
    created_date = models.DateField()

    class Meta:
        managed = False
        db_table = 'topicforum'
