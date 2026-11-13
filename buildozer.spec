[app]
title = My Calculator
package.name = mycalculator
package.domain = org.test

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3==3.11.5, hostpython3==3.11.5, kivy==2.3.0, cython==0.29.36

orientation = portrait
fullscreen = 0

# تنظیمات اندروید برای جلوگیری از خطا
android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True

# فعال کردن لاگ کامل برای دیباگ
log_level = 2
