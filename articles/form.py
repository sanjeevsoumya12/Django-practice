
from importlib.resources import contents
from django import forms 
from .models import Article





# ModelForm
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title","content"]

# form
# class ArticleFormOld(forms.Form):
#     title = forms.CharField()
#     content = forms.CharField()

    # def clean_title(self):
    #     # after subbmiting the form,we have another attribute called cleaned_data,where we get the data
    #     cleaned_data = self.cleaned_data # this is dictionary data we will get 
    #     #this cleaned_dat containing the form data
    #     # print(cleaned_data)
    #     title = cleaned_data.get("title")
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError("This title is already been used")
    #     # print(title)
    #     return  title
# now we going to validate or clean the field using the clean field.
# we can clean data for all field also

    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get("title")
        content = cleaned_data.get("content")

        if title.lower().strip() == "the office":
            self.add_error("title","this ttile is taken") # error list
            # raise forms.ValidationError("This title is already been used") #non-field errors
        if "office" in content or "office" in title.lower():
            self.add_error("content","office cannot be in content")# field errorrs
            raise forms.ValidationError('office is not allowed')# non-field errors
        return cleaned_data


