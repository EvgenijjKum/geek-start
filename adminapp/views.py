from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from mainapp.models import ProductCategory, Product
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from cabinet.models import AdvUser

pass_name = 'master'


class ProductListView(UserPassesTestMixin, generic.ListView):
    model = Product
    paginate_by = 4
    template_name = 'all_product_list.html'

    def get_queryset(self):
        return Product.objects.all().order_by('name')

    def test_func(self):
        return self.request.user.username.startswith(pass_name)


class ProductCreate(UserPassesTestMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'product_form.html'

    def test_func(self):
        return self.request.user.username.startswith(pass_name)

    def get_success_url(self):
        return reverse_lazy('adminapp:view-product-detail', args=(self.object.id,))


class ProductDetail(UserPassesTestMixin, generic.DetailView):
    model = Product
    template_name = 'view-product-detail.html'

    def test_func(self):
        return self.request.user.username.startswith(pass_name)


class ProductUpdate(UserPassesTestMixin, UpdateView):
    fields = '__all__'
    template_name = 'product_form.html'

    def get_queryset(self):
        return Product.objects.all()

    def get_success_url(self):
        return reverse_lazy('adminapp:view-product-detail', kwargs={'pk': self.kwargs.get('pk')})

    def test_func(self):
        return self.request.user.username.startswith(pass_name)


class ProductDelete(UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'product_confirm_delete.html'
    success_url = reverse_lazy('adminapp:list-all-product')

    def test_func(self):
        return self.request.user.username.startswith(pass_name)


# -------------------------------------------------------------
class CategoryListView(UserPassesTestMixin, generic.ListView):
    model = ProductCategory
    paginate_by = 5
    template_name = 'productcategory_list.html'

    def get_queryset(self):
        return ProductCategory.objects.all().order_by('name')

    def test_func(self):
        return self.request.user.username.startswith(pass_name)


class ProductCategoryDetail(UserPassesTestMixin, generic.DetailView):
    model = ProductCategory
    template_name = 'productcategory_detail.html'

    def test_func(self):
        return self.request.user.username.startswith(pass_name)


class CategoryCreate(UserPassesTestMixin, CreateView):
    model = ProductCategory
    fields = '__all__'
    template_name = 'productcategory_form.html'

    def test_func(self):
        return self.request.user.username.startswith(pass_name)

    def get_success_url(self):
        return reverse_lazy('adminapp:view-category-detail', args=(self.object.id,))


class CategoryUpdate(UserPassesTestMixin, UpdateView):
    fields = '__all__'
    template_name = 'productcategory_form.html'

    def get_queryset(self):
        return ProductCategory.objects.all()

    def get_success_url(self):
        return reverse_lazy('adminapp:view-category-detail', kwargs={'pk': self.kwargs.get('pk')})

    def test_func(self):
        return self.request.user.username.startswith(pass_name)


class CategoryDelete(UserPassesTestMixin, DeleteView):
    model = ProductCategory
    template_name = 'productcategory_confirm_delete.html'
    success_url = reverse_lazy('adminapp:list-category')

    def test_func(self):
        return self.request.user.username.startswith(pass_name)


# -------------------------------------------------------------
class UserListView(UserPassesTestMixin, generic.ListView):
    model = AdvUser
    paginate_by = 20
    template_name = 'advuser_list.html'

    def test_func(self):
        return self.request.user.username.startswith(pass_name)


class UserDetail(UserPassesTestMixin, generic.DetailView):
    model = AdvUser
    template_name = 'user_detail.html'

    def test_func(self):
        return self.request.user.username.startswith(pass_name)


class UserUpdate(UserPassesTestMixin, UpdateView):
    model = AdvUser
    fields = '__all__'
    template_name = 'user_form.html'

    def get_success_url(self):
        return reverse_lazy('adminapp:view-user-detail', kwargs={'pk': self.kwargs.get('pk')})

    def test_func(self):
        return self.request.user.username.startswith(pass_name)


class UserCreate(UserPassesTestMixin, CreateView):
    model = AdvUser
    fields = '__all__'
    template_name = 'user_form.html'

    def test_func(self):
        return self.request.user.username.startswith(pass_name)

    def get_success_url(self):
        return reverse_lazy('adminapp:view-user-detail', args=(self.object.id,))


class UserDelete(UserPassesTestMixin, DeleteView):
    model = AdvUser
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('adminapp:list-user')

    def test_func(self):
        return self.request.user.username.startswith(pass_name)