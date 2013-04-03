# -*- coding: utf-8 -*-

from django import forms
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _

from triadatv.structure.models import StructureNode, Upload

class StructureNodeAdminForm(forms.ModelForm):

    POSITION_CHOICES = (
        ('','---'),
        (_(u'first-child'), _(u'перывый потомок')),
        (_(u'last-child'), _(u'последний потомок')),
        (_(u'left'), _(u'сосед сверху')),
        (_(u'right'), _(u'сосед снизу')),
    )

    target = forms.ChoiceField(label=_(u'цель'), required=False)
    position = forms.ChoiceField(label=_(u'положение'), choices=POSITION_CHOICES, required=False)

    class Meta:
        model = StructureNode

    def __init__(self, *args, **kwargs):
        super(StructureNodeAdminForm, self).__init__(*args, **kwargs)
        
        if self.instance.pk is None or self.instance.level > 0:
            opts = self.instance._meta
            if self.instance.pk is None:
                valid_targets = StructureNode.objects.all()
            else:
                if self.instance.parent:
                    self.fields['target'].initial = self.instance.parent.pk
                valid_targets = self.instance._tree_manager.exclude(**{
                    opts.tree_id_attr: getattr(self.instance, opts.tree_id_attr),
                    '%s__gte' % opts.left_attr: getattr(self.instance, opts.left_attr),
                    '%s__lte' % opts.right_attr: getattr(self.instance, opts.right_attr),
                    })
            choices = [(
                target.pk, '%s %s (%s)' % (
                    '---' * getattr(target, opts.level_attr), target.get_menu(), target.path)
                ) for target in valid_targets]
            choices.insert(0, (0, 'корневая страница'))
            self.fields['target'].choices = choices

    def clean_target(self):
        target = self.cleaned_data['target'] or None
        if self.instance.pk is None and target is None:
            raise forms.ValidationError
        if target == '0':
            target = None
        elif target is not None:
            target = StructureNode.objects.get(pk=target)
        return target

    def clean_position(self):
        position = self.cleaned_data['position']
        if self.instance.pk is None:
            assert position
        return position

    def save(self, *args, **kwargs):
        target, position = self.cleaned_data['target'], self.cleaned_data['position']
        instance = super(StructureNodeAdminForm, self).save(commit=False)
        if instance.pk and position:
            instance.move_to(target, position)
        elif instance.pk is None:
            instance = StructureNode.objects.insert_node(instance, target, position)
        instance.save()
        return instance

class UploadAdminForm(forms.ModelForm):
    url_path = forms.CharField(label=_(u'URL'), required=False)

    class Meta:
        model = Upload

    def __init__(self, *args, **kwargs):
        super(UploadAdminForm, self).__init__(*args, **kwargs)
        if self.instance.pk is not None:
            self.fields['url_path'].initial = reverse('core_uploads_url', args =['pk', self.instance.pk])

#EOF