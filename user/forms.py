from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    """
    Login Form
    """

    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your username",
                "autocomplete": "username",
            }
        ),
    )

    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Enter your password",
                "autocomplete": "current-password",
            }
        ),
    )


class RegisterForm(forms.ModelForm):
    """
    Register Form
    """

    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Create a password",
                "autocomplete": "new-password",
            }
        ),
    )

    password2 = forms.CharField(
        label="Confirm Password",
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Confirm your password",
                "autocomplete": "new-password",
            }
        ),
    )

    class Meta:

        model = User

        fields = [
            "username",
            "first_name",
            "last_name",
            "email",
        ]

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Username",
                }
            ),
            "first_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "First Name",
                }
            ),
            "last_name": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Last Name",
                }
            ),
            "email": forms.EmailInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Email Address",
                }
            ),
        }

    def clean_username(self):
        """
        Check duplicate username
        """

        username = self.cleaned_data["username"]

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(
                "This username already exists."
            )

        return username

    def clean_email(self):
        """
        Check duplicate email
        """

        email = self.cleaned_data["email"]

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email already exists."
            )

        return email

    def clean(self):
        """
        Check password confirmation
        """

        cleaned_data = super().clean()

        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2:

            if password1 != password2:

                self.add_error(
                    "password2",
                    "Passwords do not match."
                )

            elif len(password1) < 8:

                self.add_error(
                    "password1",
                    "Password must be at least 8 characters."
                )

        return cleaned_data

    def save(self, commit=True):
        """
        Save User
        """

        user = super().save(commit=False)

        user.set_password(
            self.cleaned_data["password1"]
        )

        if commit:
            user.save()

        return user