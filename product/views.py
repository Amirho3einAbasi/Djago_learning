from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

''' *************************************  LIST VIEW  ************************************************************** '''


class product_view_class(ListView):
    template_name = 'product_list.html'
    queryset = Product.objects.filter(product_exist=True)

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        print(context)
        return context
    # def get_queryset(self):
    #     return Product.object.filter(product_exist=True)
    # def get_context_data(self, *args, object_list=None, **kwargs):
    #     context = super().get_context_data(*args,**kwargs)
    #     # print(context)
    #
    #     return context


''' *************************************  DETAIL VIEW  ************************************************************** '''


# product Slug view
class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = "product_list_detail.html"

    # def get_object(self, *args, **kwargs):
    #     request = self.request
    #     slug = self.kwargs.get('slug')
    #     try:
    #         product = Product.objects.get(slug=slug)
    #     except Product.DoesNotExist:
    #         raise Http404("product does not exists ...")
    #     except Product.MultipleObjectsReturned:
    #         qs = Product.objects.filter(slug=slug)
    #         product = qs.first()
    #     except:
    #         raise Http404("not found ...")
    #     return product


def product_detail_view(request, product_id=None):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product
    }
    return render(request, 'product_list_detail.html', context)


class product_cls_detail_view(DetailView):
    template_name = 'product_list_detail.html'
    queryset = Product.objects.get_exist_product()

    # def get_queryset(self):
    #     # return Product.object.filter(product_exist=True)
    #     return Product.objects.get_exist_product()

# def product_view(request):
#     queryset = Product.objects.all()
#     context = {
#         'product': queryset
#     }
#
#     return render(request, "product_list.html", context)
#
# # class products_detail_view(DetailView):
# #
