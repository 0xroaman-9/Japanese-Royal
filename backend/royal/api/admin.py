from django.contrib import admin

# Register your models here.



# class User(AbstractBaseUser):
#     id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)    
#     email = models.EmailField(verbose_name='email address', unique=True, max_length=255)
#     username = models.CharField(max_length=255, blank=True, null=True, default="")
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELD = []
#     is_superuser = models.BooleanField(default=False)
#     objects = UserManager()
#     def __str__(self):
#         return self.username

#     class Meta:
#         db_table = "User"