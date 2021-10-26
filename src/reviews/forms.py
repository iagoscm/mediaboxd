from django import forms
from .models import Review, Tag


class ReviewForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=False
    )

    rating = forms.ChoiceField(
        choices=Review.RATING_CHOICES, label="Nota"
    )
    media_value = forms.CharField(
        label="Procure o nome da mídia (nome do filme, série etc)",
        widget=forms.TextInput(attrs={"class": "form-control", "id": "media"}),
    )
    media_id = forms.CharField(
        widget=forms.HiddenInput(attrs={"id": "media-id"}), required=False
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(), widget=forms.CheckboxSelectMultiple, required=True,
        label="Tags"
    )

    def clean(self):
        cleaned_data = self.cleaned_data
        if not (
            cleaned_data.get("media_value")
            and cleaned_data.get("media_id")
            and cleaned_data.get("media_id") != "0"
        ):
            self.add_error("media_value","Mídia não foi encontrada")
        return cleaned_data

    class Meta:
        model = Review
        fields = ["title", "content"]
        labels = {
            "title": "Título",
            "content": "Conteúdo",
        }
