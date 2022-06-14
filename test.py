import os
import django
django.setup()

from django.contrib.auth.models import User
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "final_year.settings")

from firstapp.models import *
from firstapp.views import *

def main():
	uc = User.objects.get(username="prodigygamer143@gmail.com")
	ur = UserReport(uc)
	print(ur.TotalScore())

if __name__ == '__main__':
    main()