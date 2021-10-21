from django import forms
from .models import Review, Tag


class ReviewForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField( 
        queryset=Tag.objects.all(), 
        widget=forms.CheckboxSelectMultiple, 
        required=False)

    class Meta:
        model = Review
        fields = ['title', 'content','tags']
        labels = {
            'title': 'Título',
            'tags': 'Tags',
            'content': 'Conteúdo',
        }