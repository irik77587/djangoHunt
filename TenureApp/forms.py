from django import forms
from .models import Assets

class AssetForm(forms.ModelForm):
    class Meta:
        model=Assets
        fields = "__all__"
        labels = {
            "title" : "Flat/Unit",
            "collection" : "Building Name",
            "type" : "Target Tenent",
            "kitchen" : "Kitchen Type",
            "washroom" : "Washroom Type"
        }
        # fields = ["title", "collection", "type", "kitchen", "washroom"]
"""
class AssetForm(forms.Form):
    title = forms.CharField(label="Flat/Unit", max_length=25)
    collection = forms.CharField(label="Building Name", max_length=50)
    type = forms.ChoiceField(label="Target Tenent", choices=Assets.FLAT_TYPES)
    kitchen = forms.ChoiceField(label="Kitchen Type", choices=Assets.KITCHEN_TYPE)
    washroom = forms.ChoiceField(label="Washroom Type", choices=Assets.WASHROOM_TYPE)
"""