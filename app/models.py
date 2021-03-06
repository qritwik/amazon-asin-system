from django.db import models

# Create your models here.

class asinDetail(models.Model):
    asin = models.CharField(max_length=100, blank=True ,primary_key=True)
    status = models.BooleanField(default=False, blank=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    extracted = models.BooleanField(default=False, blank=True)
    def __str__(self):
	    return self.asin

# ===================================================

class newProductDetail(models.Model):
    asin = models.CharField(max_length=10000, blank=True, null=True)
    title = models.CharField(max_length=1000, null=True)
    bp1 = models.CharField(max_length=10000, null=True)
    bp2 = models.CharField(max_length=10000, null=True)
    bp3 = models.CharField(max_length=10000, blank=True, null=True)
    bp4 = models.CharField(max_length=10000, null=True)
    bp5 = models.CharField(max_length=10000, null=True)
    bp6 = models.CharField(max_length=10000, null=True)
    bp7 = models.CharField(max_length=10000, null=True)
    bp8 = models.CharField(max_length=10000, blank=True, null=True)
    comments = models.CharField(max_length=10000, blank=True, null=True)


    def __str__(self):
	    return self.asin
# ===================================================


class oldProductDetail(models.Model):
    asin = models.CharField(max_length=10000, blank=True, null=True)
    current_Title = models.CharField(max_length=1000,blank=True, null=True)
    revised_Title = models.CharField(max_length=1000,blank=True, null=True)


    def __str__(self):
	    return self.asin
# ===================================================


class empDetail(models.Model):
    name = models.CharField(max_length=10000, blank=True, null=True)
    asin_done_c = models.IntegerField(default=0,blank=True, null=True)
    email = models.CharField(max_length=1000,blank=True, null=True)
    roles = models.CharField(max_length=1000,blank=True, null=True)


    def __str__(self):
	    return self.email
# ===================================================


class oldDetailAmazon(models.Model):
    old_name = models.CharField(max_length=10000, blank=True, null=True)
    old_url = models.CharField(max_length=10000, blank=True, null=True)
    old_desc = models.CharField(max_length=100000, blank=True, null=True)
    old_brand = models.CharField(max_length=10000, blank=True, null=True)
    old_product_desc = models.CharField(max_length=100000, blank=True, null=True)
    old_from_manufacture_h = models.CharField(max_length=1000000, blank=True, null=True)
    old_from_manufacture_p = models.CharField(max_length=1000000, blank=True, null=True)

    asin = models.CharField(max_length=10000, blank=True, null=True)
    status = models.BooleanField(default=False)

    def __str__(self):
	    return self.asin



# ===================================================


class featureImage(models.Model):
    asin = models.CharField(max_length=10000, blank=True, null=True)
    screen_size_resolution = models.CharField(max_length=10000, blank=True, null=True)
    connectivity_ports = models.CharField(max_length=10000, blank=True, null=True)
    display_and_refresh_rate = models.CharField(max_length=10000, blank=True, null=True)
    sound_output = models.CharField(max_length=10000, blank=True, null=True)
    smart_tv = models.CharField(max_length=10000, blank=True, null=True)
    warranty = models.CharField(max_length=10000, blank=True, null=True)

    def __str__(self):
	    return self.asin
