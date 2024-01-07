from django.urls import path
from Backend import views

urlpatterns=[
    path('indexpage/',views.indexpage,name="indexpage"),
    path('categorypage/',views.categorypage,name="categorypage"),
    path('save_category/',views.save_category,name="save_category"),
    path('display_category/',views.display_category,name="display_category"),
    path('edit_category/<int:cat_id>/',views.edit_category,name="edit_category"),
    path('update_category/<int:dataid>/', views.update_category, name="update_category"),
    path('remv_category/<int:dataid>/',views.remv_category,name="remv_category"),
    path('productpage/',views.productpage,name="productpage"),
    path('save_product/',views.save_product,name="save_product"),
    path('display_products/',views.display_products,name="display_products"),
    path('edit_product/<int:pro_id>/',views.edit_product,name="edit_product"),
    path('Update_product/<int:dataid>/',views.Update_product,name="Update_product"),
    path('rem_product/<int:dataid>/',views.rem_product,name="rem_product"),
    path('adminlogin/',views.adminlogin,name="adminlogin"),
    path('admin_login/',views.admin_login,name="admin_login"),
    path('admin_logout/',views.admin_logout,name="admin_logout"),
    path('display_contact/',views.display_contact,name="display_contact"),
    path('delete_contact/<int:dataid>/',views.delete_contact,name="delete_contact")


]