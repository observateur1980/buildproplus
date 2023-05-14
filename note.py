first_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'id': 'first_name', 'name': 'first_name',
                                                                               'class': 'form-control',
                                                                               'required': 'required'}))
    last_name = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'id': 'last_name', 'name': 'last_name',
                                                                              'class': 'form-control',
                                                                              'required': 'required'}))




email_address = forms.EmailField(max_length=120, widget=forms.EmailInput(
        attrs={'id': 'email_address', 'name': 'email_address',
               'class': 'form-control', 'required': 'required'}))

    address = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'id': 'address', 'name': 'address',
                                                                            'class': 'form-control', }))

    city = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'id': 'city', 'name': 'city',
                                                                         'class': 'form-control', }))

    state = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'id': 'state', 'name': 'state',
                                                                          'class': 'form-control', }))

    zip = forms.CharField(max_length=120, widget=forms.TextInput(attrs={'id': 'zip', 'name': 'zip',
                                                                        'class': 'form-control', }))
