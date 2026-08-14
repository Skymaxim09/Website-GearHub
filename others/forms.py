from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    content = forms.CharField(widget=forms.Textarea)
    
    def clean_content(self):
        data = self.cleaned_data["content"]

        forbidden_words = ['ăn cắp', 'tuồn kho', 'lừa đảo', 'hack', 'scam', 'fake', 'hàng giả']

        if any(word in data for word in forbidden_words):
            raise forms.ValidationError("Vui lòng sử dụng ngôn từ lịch sự!")

        return data