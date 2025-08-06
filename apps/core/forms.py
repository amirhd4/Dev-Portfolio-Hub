from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        label="نام شما",
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500',
            'placeholder': 'نام کامل'
        })
    )
    email = forms.EmailField(
        label="ایمیل شما",
        widget=forms.EmailInput(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500',
            'placeholder': 'example@email.com'
        })
    )
    subject = forms.CharField(
        label="موضوع",
        max_length=200,
        widget=forms.TextInput(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500',
            'placeholder': 'درخواست همکاری، مشاوره فنی، ...'
        })
    )
    message = forms.CharField(
        label="پیام شما",
        widget=forms.Textarea(attrs={
            'class': 'w-full p-3 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500',
            'rows': 6,
            'placeholder': 'لطفاً پیام خود را با جزئیات بنویسید...'
        })
    )