from django import forms
from .models import PlayerProfile

# Example choices for favorite games
GAME_CHOICES = [
    ('game1', 'Game 1'),
    ('game2', 'Game 2'),
    ('game3', 'Game 3'),
    ('game4', 'Game 4'),
    # Add more games as needed
]


class PlayerProfileForm(forms.ModelForm):
    favorite_game = forms.MultipleChoiceField(
        choices=GAME_CHOICES,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control',
        }),
        required=False
    )

    facebook_link = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your Facebook profile URL',
    }))
    twitter_link = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your Twitter profile URL',
    }))
    linkedin_link = forms.URLField(required=False, widget=forms.URLInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your LinkedIn profile URL',
    }))

    favorite_genre = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your favorite game genre',
    }))
    favorite_platform = forms.CharField(required=False, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Enter your favorite gaming platform',
    }))

    class Meta:
        model = PlayerProfile
        fields = [
            'date_of_birth', 'profile_picture', 'bio', 'location', 'mobile_number',
            'level', 'notifications_enabled', 'is_subscribed', 'receive_newsletter',
            'is_active', 'is_invisible',
        ]
        widgets = {
            'date_of_birth': forms.TextInput(attrs={
                'class': 'form-control datepicker',
                'placeholder': 'Please select your birth date',
            }),
            'profile_picture': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),
            'bio': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Tell us about yourself',
                'rows': 3,
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your location',
            }),
            'mobile_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your mobile number',
            }),
            'level': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your level',
            }),
            'notifications_enabled': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'is_subscribed': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
            'receive_newsletter': forms.CheckboxInput(attrs={
                'class': 'form-check-input',
            }),
        }

    def __init__(self, *args, **kwargs):
        # Extract the instance if it exists
        instance = kwargs.get('instance')
        super().__init__(*args, **kwargs)

        # Populate initial values for social links if instance is provided
        if instance and instance.social_links:
            social_links = instance.social_links
            self.fields['facebook_link'].initial = social_links.get('facebook', '')
            self.fields['twitter_link'].initial = social_links.get('twitter', '')
            self.fields['linkedin_link'].initial = social_links.get('linkedin', '')

            # Populate initial values for game preferences if instance is provided
        if instance and instance.game_preferences:
            game_preferences = instance.game_preferences
            self.fields['favorite_genre'].initial = game_preferences.get('favorite_genre', '')
            self.fields['favorite_platform'].initial = game_preferences.get('favorite_platform', '')
            # Populate initial values for favorite games if instance is provided

        if instance and instance.favorite_game:
            self.fields['favorite_game'].initial = instance.favorite_game.split(',')

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Combine social links into a JSON object
        social_links = {
            'facebook': self.cleaned_data.get('facebook_link', ''),
            'twitter': self.cleaned_data.get('twitter_link', ''),
            'linkedin': self.cleaned_data.get('linkedin_link', ''),
        }
        instance.social_links = social_links

        # Combine game preferences into a JSON object
        game_preferences = {
            'favorite_genre': self.cleaned_data.get('favorite_genre', ''),
            'favorite_platform': self.cleaned_data.get('favorite_platform', ''),
        }
        # Save favorite games as a comma-separated string
        instance.favorite_game = ','.join(self.cleaned_data.get('favorite_game', []))

        if commit:
            instance.save()
        return instance
