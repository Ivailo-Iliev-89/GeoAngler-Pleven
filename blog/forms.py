from django import forms
from .models import Post

BITE_CHOICES = [
    ('', '--- Избери статус на кълване ---'),
    ('кълве', '🔥 Кълве яко'),
    ('слабо', '🐟 Слабо / Редки удари'),
    ('капо', '❌ Капо (Пълна суша)'),
]


class ReportPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'bite_status', 'content']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Заглавие на репортажа...'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Сподели историята на твоя излет...'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['bite_status'].choices = [
            ('', '--- Избери статус на кълване ---')] + Post.BITE_CHOICES
        self.fields['bite_status'].widget.attrs.update(
            {'class': 'form-select'})
