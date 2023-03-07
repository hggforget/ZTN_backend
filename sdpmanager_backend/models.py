# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class ClosedConnection(models.Model):
    gateway_sdpid = models.OneToOneField('Sdpid', models.DO_NOTHING, db_column='gateway_sdpid', primary_key=True)
    client_sdpid = models.ForeignKey('Sdpid', models.DO_NOTHING, related_name='+', db_column='client_sdpid')
    service_id = models.IntegerField()
    start_timestamp = models.BigIntegerField()
    end_timestamp = models.BigIntegerField()
    protocol = models.TextField()
    source_ip = models.TextField()
    source_port = models.IntegerField()
    destination_ip = models.TextField()
    destination_port = models.IntegerField()
    nat_destination_ip = models.TextField()
    nat_destination_port = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'closed_connection'
        unique_together = (('gateway_sdpid', 'client_sdpid', 'start_timestamp', 'source_port'),)


class Controller(models.Model):
    sdpid = models.OneToOneField('Sdpid', models.DO_NOTHING, db_column='sdpid', primary_key=True)
    name = models.CharField(max_length=1024)
    address = models.CharField(max_length=4096)
    port = models.IntegerField()
    gateway_sdpid = models.ForeignKey('Sdpid', models.DO_NOTHING, related_name='+', db_column='gateway_sdpid', blank=True, null=True)
    service = models.ForeignKey('Service', models.DO_NOTHING, related_name='+', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'controller'


class Credential(models.Model):
    account = models.CharField(max_length=255, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'credential'


class Environment(models.Model):
    name = models.CharField(max_length=1024)
    mobile = models.IntegerField()
    os_group = models.CharField(max_length=7)
    os_version = models.CharField(max_length=1024)

    class Meta:
        managed = True
        db_table = 'environment'


class Gateway(models.Model):
    sdpid = models.OneToOneField('Sdpid', models.DO_NOTHING, db_column='sdpid', primary_key=True)
    name = models.CharField(max_length=1024)
    address = models.CharField(max_length=1024)
    port = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'gateway'


class GatewayController(models.Model):
    gateway_sdpid = models.ForeignKey('Sdpid', models.DO_NOTHING, related_name='+', db_column='gateway_sdpid')
    controller_sdpid = models.ForeignKey('Sdpid', models.DO_NOTHING, related_name='+', db_column='controller_sdpid')

    class Meta:
        managed = True
        db_table = 'gateway_controller'


class Group(models.Model):
    valid = models.IntegerField()
    name = models.CharField(max_length=1024)
    description = models.CharField(db_column='Description', max_length=4096)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'group'


class GroupService(models.Model):
    group = models.ForeignKey(Group, models.DO_NOTHING, related_name='+')
    service = models.ForeignKey('Service', models.DO_NOTHING, related_name='+')

    class Meta:
        managed = True
        db_table = 'group_service'


class OpenConnection(models.Model):
    gateway_sdpid = models.ForeignKey('Sdpid', models.DO_NOTHING, related_name='+', db_column='gateway_sdpid')
    client_sdpid = models.ForeignKey('Sdpid', models.DO_NOTHING, related_name='+', db_column='client_sdpid')
    service = models.ForeignKey('Service', models.DO_NOTHING, related_name='+')
    start_timestamp = models.BigIntegerField()
    end_timestamp = models.BigIntegerField()
    protocol = models.TextField()
    source_ip = models.TextField()
    source_port = models.IntegerField()
    destination_ip = models.TextField()
    destination_port = models.IntegerField()
    nat_destination_ip = models.TextField()
    nat_destination_port = models.IntegerField()
    gateway_controller_connection_id = models.IntegerField(primary_key=True)

    class Meta:
        managed = True
        db_table = 'open_connection'
        unique_together = (('gateway_controller_connection_id', 'client_sdpid', 'start_timestamp', 'source_port'),)


class RefreshTrigger(models.Model):
    id = models.BigAutoField(primary_key=True)
    timestamp = models.DateTimeField()
    table_name = models.TextField()
    event = models.TextField()

    class Meta:
        managed = True
        db_table = 'refresh_trigger'


class Sdpid(models.Model):
    sdpid = models.AutoField(primary_key=True)
    valid = models.IntegerField()
    type = models.CharField(max_length=10)
    country = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    locality = models.CharField(max_length=128)
    org = models.CharField(max_length=128)
    org_unit = models.CharField(max_length=128, blank=True, null=True)
    alt_name = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=128, blank=True, null=True)
    encrypt_key = models.CharField(max_length=2048, blank=True, null=True)
    hmac_key = models.CharField(max_length=2048, blank=True, null=True)
    serial = models.CharField(max_length=32)
    last_cred_update = models.DateTimeField()
    cred_update_due = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING, related_name='+', blank=True, null=True)
    environment = models.ForeignKey(Environment, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sdpid'


class SdpidService(models.Model):
    sdpid = models.ForeignKey(Sdpid, models.DO_NOTHING, related_name='+', db_column='sdpid')
    service = models.ForeignKey('Service', models.DO_NOTHING)

    class Meta:
        managed = True
        db_table = 'sdpid_service'


class Service(models.Model):
    name = models.CharField(max_length=1024)
    description = models.CharField(max_length=4096)

    class Meta:
        managed = True
        db_table = 'service'


class ServiceGateway(models.Model):
    service = models.ForeignKey(Service, models.DO_NOTHING)
    gateway_sdpid = models.ForeignKey(Sdpid, models.DO_NOTHING, related_name='+', db_column='gateway_sdpid')
    protocol = models.TextField()
    port = models.PositiveIntegerField()
    nat_ip = models.CharField(max_length=128)
    nat_port = models.PositiveIntegerField()

    class Meta:
        managed = True
        db_table = 'service_gateway'


class User(models.Model):
    last_name = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    country = models.CharField(max_length=128, blank=True, null=True)
    state = models.CharField(max_length=128, blank=True, null=True)
    locality = models.CharField(max_length=128, blank=True, null=True)
    org = models.CharField(max_length=128, blank=True, null=True)
    org_unit = models.CharField(max_length=128, blank=True, null=True)
    alt_name = models.CharField(max_length=128, blank=True, null=True)
    email = models.CharField(max_length=128)

    class Meta:
        managed = True
        db_table = 'user'


class UserGroup(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING, related_name='+')
    group = models.ForeignKey(Group, models.DO_NOTHING, related_name='+')

    class Meta:
        managed = True
        db_table = 'user_group'
