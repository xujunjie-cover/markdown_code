class UpdateIpobject(forms.SelfHandlingForm):
    name = forms.CharField(max_length=80, label=_("Name"), required=False)
    description = forms.CharField(required=False,
                                  max_length=254, label=_("Description"))
    ip_range = forms.IPandRangeField(label=_("Ip Object Address/Subnet"),mask=True)
    failure_url = 'horizon:project:firewalls:index'

    def handle(self, request, context):
        ipobject_id = self.initial['ipobject_id']
        name_or_id = context.get('name') or ipobject_id
        try:
            ipobject = api.fwaas.ipobject_update(request, ipobject_id, **context)
            msg = _('Ipobject %s was successfully updated.') % name_or_id
            LOG.debug(msg)
            messages.success(request, msg)
            return ipobject
        except Exception as e:
            msg = _('Failed to update ipobject %(name)s: %(reason)s') % {
                'name': name_or_id, 'reason': e}
            LOG.error(msg)
            redirect = reverse(self.failure_url)
            exceptions.handle(request, msg, redirect=redirect)
