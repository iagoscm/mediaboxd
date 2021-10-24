from django import forms
from .models import Review, Tag


class ReviewForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )

    rating = forms.ChoiceField(
        choices=Review.RATING_CHOICES, required=True, label="Nota"
    )
    media_value = forms.CharField(
        label="Midia",
        widget=forms.TextInput(attrs={"class": "form-control", "id": "media"}),
    )
    media_id = forms.CharField(
        widget=forms.HiddenInput(attrs={"id": "media-id"}), required=False
    )

    class Meta:
        model = Review
        fields = ["title", "content", "tags"]
        labels = {
            "title": "Título",
            "tags": "Tags",
            "content": "Conteúdo",
        }
