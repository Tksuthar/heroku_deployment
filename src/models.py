# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class RegistrationForm(models.Model): #inheri models.Model

   firstname = models.CharField(max_length = 50)
   section = models.CharField(max_length = 50)
   branch = models.CharField(max_length = 50)
   registration_id = models.CharField(max_length = 50)   
