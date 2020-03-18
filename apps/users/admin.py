# from django.contrib import admin
# from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
# from django.utils.translation import gettext_lazy as _
# from .forms import AdminUserChangeForm, AdminUserCreationForm
# from . import models
#
# import nested_admin
# from django import forms
# from nested_admin.forms import SortableHiddenMixin
#
#
# @admin.register(models.User)
# class UserAdmin(AuthUserAdmin):
#     form = AdminUserChangeForm
#     list_display = (
#         "email",
#         "first_name",
#         "last_name",
#         "user_name",
#         "is_active",
#         "is_staff",
#         "is_superuser",
#         "date_joined",
#         "last_login",
#     )
#
#     list_editable = ("is_active", "is_staff", "is_superuser")
#
#     list_filter = ("is_superuser", "is_active", "is_staff", "date_joined", "last_login", "user_name")
#
#     search_fields = ["email", "first_name", "last_name"]
#     ordering = ("date_joined",)
#
#     fieldsets = (
#         (_("Personal info"), {"fields": ("email", "first_name", "last_name", "user_name", "image")}),
#         (_("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups")},),
#         (_("Important dates"), {"fields": ("last_login", "date_joined", "creation_date", "modified_date")},),
#     )
#
#     add_form = AdminUserCreationForm
#     add_form_template = "admin/auth/user/add_form.html"
#
#     add_fieldsets = (
#         (
#             None,
#             {
#                 "classes": ("wide",),
#                 "fields": ("email", "first_name", "last_name", "user_name", "password1", "password2", "image"),
#             },
#         ),
#     )
#     readonly_fields = ("creation_date", "modified_date")
#
# # class UserManagementForm(forms.ModelForm):
# #     Email = forms.CharField(required=True)
# #     first_name = forms.CharField(required=False, widget=forms.CharField)
# #     last_name = forms.CharField(required=False, widget=forms.CharField)
# #
# #     class Meta:
# #         model = models.User
# #         fields = ("email", "first_name", "last_name",)
# #
# #
# # class UserManagementInline(SortableHiddenMixin, nested_admin.NestedStackedInline):
# #     model = models.User
# #     form = UserManagementForm
# #     # inlines = (OnlineCourseResourceInline,)
# #     extra = 0
# #
# #
# # @admin.register(models.User)
# # class OUserManagementAdmin(nested_admin.NestedModelAdmin):
# #     inlines = (UserManagementInline,)
