from django import forms
from .models import Category,Product
from django.core.exceptions import ValidationError

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data["name"]
        if not name.strip():
            raise ValidationError("Name can't be empty")
        
        return name
    def clean_image(self):
        image = self.cleaned_data["image"]
        # print(f"image name is {image._name}")
        # print(image.__dir__())

        if not image._name.endswith(".png"):
            raise ValidationError("the image must be in PNG format")
        
        return image



class ProductFrom(forms.ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_title(self):
        title = self.cleaned_data["title"]
        if not title.strip():
            raise ValidationError("Title can not be empty")
        return title
    def clean_price(self):
        price = self.cleaned_data["price"]

        if price < 5:
            raise ValidationError("price can not be less than 5 dollar")
        
        return price
    
    def clean_description(self):
        description = self.cleaned_data["description"]

        if len(description.strip().replace(" ","")) <20:
            raise ValidationError("Description can't be less than 20 character")
        
        return description
    

