from sdpmanager_backend import models


def relate_create(sdp,form):
    ret=None
    if sdp.type == 'gateway':
        ret=models.Gateway.objects.create(
            sdpid= sdp,
            name= form.get('name'),
            address='192.168.32.1',
            port=5000
        )
    elif sdp.type == 'controller':
        ret=models.Controller.objects.create(
            sdpid=sdp,
            name=form.get('name'),
            address='192.168.32.1',
            port=5000
        )
    return ret


