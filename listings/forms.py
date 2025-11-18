# listings/forms.py
from django import forms
from .models import Listing, Report, ChatMessage


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = [
            "title",
            "price",
            "category",
            "status",
            "location",
            "image_url",
            "description",
        ]
        widgets = {
            "title": forms.TextInput(
                attrs={
                    "class": "w-full p-3 border border-gray-300 rounded-lg",
                    "placeholder": "제목을 입력하세요",
                }
            ),
            "price": forms.NumberInput(
                attrs={
                    "class": "w-full p-3 border border-gray-300 rounded-lg",
                    "placeholder": "가격(원)",
                    "min": "0",
                }
            ),
            "category": forms.CheckboxSelectMultiple(
                attrs={
                    "class": "mr-2",
                }
            ),
            "status": forms.RadioSelect(),
            "location": forms.TextInput(
                attrs={
                    "class": "w-full p-3 border border-gray-300 rounded-lg",
                    "placeholder": "예: 서울 강남구 역삼동",
                }
            ),
            "image_url": forms.URLInput(
                attrs={
                    "class": "w-full p-3 border border-gray-300 rounded-lg",
                    "placeholder": "이미지 URL (선택)",
                }
            ),
            "description": forms.Textarea(
                attrs={
                    "class": "w-full p-3 border border-gray-300 rounded-lg",
                    "rows": 6,
                    "placeholder": "상품 상세 설명을 입력하세요.",
                }
            ),
        }


class ChatMessageForm(forms.ModelForm):
    class Meta:
        model = ChatMessage
        fields = ["message"]
        widgets = {
            "message": forms.Textarea(
                attrs={
                    "class": "w-full p-2 border border-gray-300 rounded-lg",
                    "rows": 3,
                    "placeholder": "메시지를 입력하세요...",
                }
            )
        }


class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ["report_type", "reason"]
        widgets = {
            "report_type": forms.Select(
                attrs={"class": "w-full p-3 border border-gray-300 rounded-lg"}
            ),
            "reason": forms.Textarea(
                attrs={
                    "class": "w-full p-3 border border-gray-300 rounded-lg",
                    "rows": 5,
                    "placeholder": "신고 사유를 구체적으로 작성해주세요.",
                }
            ),
        }
