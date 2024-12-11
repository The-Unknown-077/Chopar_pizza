from django.shortcuts import render
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect  # Shablonlarni render qilish va yo'naltirish uchun
from django.http import HttpResponse  # Javob yaratish uchun
from django.contrib import messages  # Foydalanuvchi uchun xabarlar qo'shish
from .models import CustomUser  # CustomUser modelini import qilish
from .models import RegistrationForm  # RegistrationForm formasini import qilish


def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Tasdiqlash kodi emailga yuborildi.")
            return redirect('confirm')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def confirm(request):
    if request.method == "POST":
        email = request.POST.get('email')
        confirmation_code = request.POST.get('confirmation_code')
        try:
            user = CustomUser.objects.get(email=email, confirmation_code=confirmation_code)
            user.is_confirmed = True
            user.save()
            messages.success(request, "Tasdiqlash muvaffaqiyatli amalga oshirildi.")
            return redirect('success')
        except CustomUser.DoesNotExist:
            messages.error(request, "Notogri email yoki tasdiqlash kodi.")
    return render(request, 'confirm.html')

def success(request):
    return HttpResponse("Registratsiya muvaffaqiyatli yakunlandi!")

