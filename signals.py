"""






"""

from django.dispatch import Signal

api_request_started = Signal(providing_args=['request', 'model'])
api_request_started.__doc__ = \
"""
Sent when the API begins processing a request.

Arguments sent with this signal::

    sender:
        The API model class.
    
    request:
        The HttpRequest object for this request.
    
    model:
        The model class of the request.
"""

api_request_finished = Signal(providing_args=['request', 'response'])
api_request_finished.__doc__ = \
"""
Sent when the API finishes processing a request.

Arguments sent with this signal::

    sender:
        The API model class.
    
    request:
        The HttpRequest object for this request.
    
    response:
        The HttpResponse object returned for this request.
"""

# Make sure to call list() on the instances before sending this signal.
api_pre_delete = Signal(providing_args=['user', 'instances'])
api_pre_delete.__doc__ = \
"""
Sent when the API is about to delete a model instance.

Arguments sent with this signal::

    sender:
        The model class of the instances.
    
    user:
        The user requesting the action.
    
    instances:
        The actual instances being deleted.
        
Return either False, or an HttpResponse (or subclass) object if the
instance should not be deleted. If False is returned, an HTTP 403
response with a generic message will be sent to the client. If an
HttpResponse object is returned instead, then it will be sent to the
client.
"""

api_post_delete = Signal(providing_args=['user', 'instances'])
api_post_delete.__doc__ = \
"""
Sent right after the API deletes a model instance.

Arguments sent with this signal::

    sender:
        The model class of the instances.
    
    user:
        The user requesting the action.
    
    instances:
        The actual instances being deleted. Note that the instances
        will no longer be in the database, so be careful with them.
"""

api_pre_save = Signal(providing_args=['user', 'instances'])
api_pre_save.__doc__ = \
"""
Sent when the API is about to delete a model instance.

Arguments sent with this signal::

    sender:
        The model class of the instances.
    
    user:
        The user requesting the action.
    
    instances:
        The actual instances being saved.
        
Return either False, or an HttpResponse (or subclass) object if the
instance should not be saved. If False is returned, an HTTP 403
response with a generic message will be sent to the client. If an
HttpResponse object is returned instead, then it will be sent to the
client.
"""

api_post_save = Signal(providing_args=['user', 'instances', 'created'])
api_post_save.__doc__ = \
"""
Sent right after the API deletes a model instance.

Arguments sent with this signal::

    sender:
        The model class of the instances.
    
    user:
        The user requesting the action.
    
    instances:
        The actual instances being deleted. Note that the instances
        will no longer be in the database, so be careful with them.
    
    created:
        A boolean; True if a new record was created.
"""


sc_model_pre_show = django.dispatch.Signal(providing_args=['model', 'user'])
sc_model_post_show = django.dispatch.Signal(providing_args=['model', 'user'])
sc_model_pre_list = django.dispatch.Signal(providing_args=['model', 'user'])
sc_model_post_list = django.dispatch.Signal(providing_args=['model', 'user'])
sc_model_pre_create = django.dispatch.Signal(providing_args=['model', 'user'])
sc_model_post_create = django.dispatch.Signal(providing_args=['model', 'user'])
sc_model_pre_update = django.dispatch.Signal(providing_args=['model', 'user'])
sc_model_post_update = django.dispatch.Signal(providing_args=['model', 'user'])
sc_model_pre_delete = django.dispatch.Signal(providing_args=['model', 'user'])
sc_model_post_delete = django.dispatch.Signal(providing_args=['model', 'user'])

sc_model_init = django.dispatch.Signal(providing_args=['user', 'args', 'kwargs'])
sc_model_instance_pre_show = django.dispatch.Signal(providing_args=['model_instance', 'user'])
sc_model_instance_pre_save = django.dispatch.Signal(providing_args=['model_instance', 'user'])
sc_model_instance_post_save = django.dispatch.Signal(providing_args=['model_instance', 'user'])
sc_model_instance_pre_delete = django.dispatch.Signal(providing_args=['model_instance', 'user'])






sc_incoming_request = django.dispatch.Signal(providing_args=['request', 'app_name', 'model_name', 'obj_id'])
