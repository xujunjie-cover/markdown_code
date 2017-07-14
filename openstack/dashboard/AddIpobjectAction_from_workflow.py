class AddIpobjectAction(workflows.Action):
    name = forms.CharField(max_length=80,
                           label=_("Name"))
    description = forms.CharField(max_length=80,
                                  label=_("Description"),
                                  required=False)
    ip_range = forms.IPandRangeField(label=_("Ip Object Address/Subnet"),mask=True)
    def __init__(self, request, *args, **kwargs):
        super(AddIpobjectAction, self).__init__(request, *args, **kwargs)

    class Meta(object):
        name = _("AddIpobject")
        permissions = ('openstack.services.network',)
        help_text = _("Create a firewall ipobject.\n\n"
                      "name and ip_range must be specified.\n\n"
                      "Please input correct ip_range.(incule two types)\n\n"
                      "First Type:IP Address/Netmask. Like 192.168.1.0/24.\n\n"
                      "Second Type:IP Range. Like 192.168.1.0-192.168.1.254.")
